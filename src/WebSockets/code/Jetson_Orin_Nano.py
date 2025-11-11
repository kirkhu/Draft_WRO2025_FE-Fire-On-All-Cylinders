class WsHub:
    def __init__(self, host="0.0.0.0", port=8765):
        self.host = host
        self.port = port
        self.clients = set()
        self._loop = None
        self._thread = None
        self._stop_evt = threading.Event()
        self.started_evt = threading.Event()
        self._last_angle_rel = 0
        self._last_angle_servo = rel_to_servo_deg(0)
        self._last_speed_pct = 0

    def start(self):
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop_evt.set()
        if self._loop:
            asyncio.run_coroutine_threadsafe(self._shutdown(), self._loop)
        if self._thread:
            self._thread.join(timeout=1)

    def wait_for_start(self, timeout=None):
        return self.started_evt.wait(timeout)

    def write(self, value):
        if isinstance(value, float) and value < 10.0:
            time.sleep(float(value))
            return
        if isinstance(value, tuple) and len(value) == 2 and value[0] == "S":
            self._last_speed_pct = int(value[1])
        elif isinstance(value, int) and value >= 1000:
            self._last_speed_pct = pwm_to_percent(value)
        else:
            rel = int(value)
            rel = clamp(rel, -180, 180)
            self._last_angle_rel = rel
            self._last_angle_servo = rel_to_servo_deg(rel)
        self.broadcast(f"M,{self._last_angle_rel},{self._last_speed_pct}\n")

    def multi_write(self, seq):
        for v in seq:
            self.write(v)

    def stop_car(self):
        self._last_angle_rel = 0
        self._last_angle_servo = rel_to_servo_deg(0)
        self._last_speed_pct = 0
        self.broadcast("STOP\n")

    def broadcast(self, text):
        if self._loop:
            asyncio.run_coroutine_threadsafe(self._async_broadcast(text), self._loop)

    # ★可附加額外欄位，方便發給 Pico W
    def broadcast_json(self, leftArea, rightArea, yaw, angle, speed, **extra):
        msg = {
            "leftArea": int(leftArea),
            "rightArea": int(rightArea),
            "yaw": float(yaw),
            "angle": int(angle),
            "speed": int(speed),
        }
        if extra:
            msg.update(extra)
        self.broadcast(json.dumps(msg) + "\n")

    def _run_loop(self):
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._loop.run_until_complete(self._main())

    async def _main(self):
        async def handler(ws):
            self.clients.add(ws)
            print("WS client connected:", ws.remote_address)
            try:
                await ws.send('{"from":"jetson","status":"ready"}\n')
                async for msg in ws:
                    if isinstance(msg, (bytes, bytearray)):
                        msg = msg.decode("utf-8", errors="ignore")
                    if "START" in msg:
                        self.started_evt.set()
            except ConnectionClosed as e:
                print(f"WS disconnected: {e.code} {e.reason}")
            finally:
                self.clients.discard(ws)

        async with websockets.serve(
            handler, self.host, self.port,
            ping_interval=None, compression=None, max_size=None, close_timeout=1.0
        ):
            print(f"WebSocket server at ws://{self.host}:{self.port}")
            while not self._stop_evt.is_set():
                await asyncio.sleep(0.1)

    async def _async_broadcast(self, text):
        dead = []
        for ws in list(self.clients):
            try:
                await ws.send(text)
            except Exception:
                dead.append(ws)
        for ws in dead:
            self.clients.discard(ws)

    async def _shutdown(self):
        for ws in list(self.clients):
            try:
                await ws.close()
            except:
                pass
        self.clients.clear()