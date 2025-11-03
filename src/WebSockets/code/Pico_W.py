def connect_ws_with_retry(host, port, retry_delay=2):
    attempt = 0
    while True:
        attempt += 1
        s = None
        try:
            if DEBUG:
                print("connect attempt #{}".format(attempt))
            addr = socket.getaddrinfo(host, port)[0][-1]
            s = socket.socket()
            s.settimeout(5)
            s.connect(addr)
            ws_client_handshake(s, host, port)
            s.settimeout(0.01)
            if DEBUG:
                print("connect_ws_with_retry: connected and handshake ok")
            return s
        except Exception as e:
            if DEBUG:
                print("connect_ws_with_retry: failed:", e)
            try:
                if s:
                    s.close()
                    del s
            except:
                pass
            try:
                gc.collect()
            except:
                pass
            time.sleep(retry_delay)

def ws_client_handshake(sock, host, port):
    key_b64 = ubinascii.b2a_base64(uos.urandom(16)).strip().decode()
    req = (
        "GET / HTTP/1.1\r\n"
        "Host: {}:{}\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Key: {}\r\n"
        "Sec-WebSocket-Version: 13\r\n\r\n"
    ).format(host, port, key_b64)
    sock.send(req.encode())
    resp = b""
    sock.settimeout(5)
    while b"\r\n\r\n" not in resp:
        part = sock.recv(256)
        if not part: break
        resp += part
    if b"101 Switching Protocols" not in resp:
        raise OSError("WS handshake failed")

def _recvn(sock, n):
    data = b""
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk: raise OSError("socket closed")
        data += chunk
    return data

def ws_send_text(sock, text):
    payload = text.encode("utf-8")
    plen = len(payload)
    header = bytearray([0x81])
    mask_bit = 0x80
    if plen <= 125:
        header.append(mask_bit | plen)
    elif plen <= 65535:
        header.append(mask_bit | 126); header.extend(bytes([(plen>>8)&0xFF, plen&0xFF]))
    else:
        raise ValueError("payload too long")
    mask_key = uos.urandom(4); header.extend(mask_key)
    masked = bytearray(plen)
    for i in range(plen): masked[i] = payload[i] ^ mask_key[i%4]
    sock.send(header + masked)

def ws_recv_text(sock, timeout=WS_RECV_TIMEOUT):
    sock.settimeout(timeout)
    try:
        b1b2 = _recvn(sock, 2)
    except OSError:
        return None
    b1, b2 = b1b2[0], b1b2[1]
    plen = (b2 & 0x7F)
    if plen == 126:
        plen = int.from_bytes(_recvn(sock, 2), "big")
    elif plen == 127:
        _ = _recvn(sock, 8)
        raise ValueError("Too long frame")
    masked = (b2 & 0x80) != 0
    if masked:
        mask_key = _recvn(sock, 4)
    payload = _recvn(sock, plen) if plen else b""
    if masked:
        payload = bytes([payload[i] ^ mask_key[i % 4] for i in range(plen)])
    text = payload.decode("utf-8")
    if DEBUG and text:
        print("RX_FRAME:", text)
    return text