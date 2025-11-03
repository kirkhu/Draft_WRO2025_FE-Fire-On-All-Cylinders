<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Web Sockets Introduction</div>

- 根據過往參賽經驗，我們的主控制器與下位控制器透過 UART 協定進行資料傳輸。由於 UART 為非同步通訊方式，發送端與接收端必須預先設定相同的鮑率 (Baud Rate)，且誤差需控制在 10% 以內，否則容易產生時序錯誤，造成資料失真或遺失。此限制不僅增加實務調校難度，也可能導致車輛判斷偏差、路線失準，進而影響比賽表現。因此，今年我們著手尋找更高穩定性與可靠性的通訊替代方案，以確保自駕車系統能在競賽環境中維持精確與即時的運作。

- 以下將針對三種常見的資料傳輸協定進行特性比較。

<div align=center>
    <table width=1200>
        <tr>
            <th colspan=4>WebSockets vs HTTP vs UART 比較</th>
        </tr>
        <tr>
            <th rowspan=2 width=20%>特性</th>
            <th width=25%><div align=center><img src="img/HTTP.png" width=150/></div></th>
            <th width=25%><div align=center><img src="img/WebSockets.png" width=150/></div></th>
            <th width=25%><div align=center><img src="img/UART.png" /></div></th>
        </tr>
        <tr>
            <th>HTTP</th>
            <th>WebSockets</th>
            <th>UART</th>
        </tr>
        <tr>
            <th>通訊型態</th>
            <td>請求 - 回應(半雙工)</td>
            <td>持續連線(全雙工)</td>
            <td>點對點(全雙工)</td>
        </tr>
        <tr>
            <th>建立連線</th>
            <td>每次請求都重新建立</td>
            <td>只需一次握手，保持連線</td>
            <td>物理層面直接連線</td>
        </tr>
        <tr>
            <th>即時性</th>
            <td>低(需重複請求)</td>
            <td>高(伺服器可主動推送)</td>
            <td>高(即時傳輸)</td>
        </tr>
        <tr>
            <th>傳輸媒介</th>
            <td>網路(TCP/HTTP)</td>
            <td>網路(TCP/WebSocket協定)</td>
            <td>實體線路（UART TX/RX）</td>
        </tr>
        <tr>
            <th>適用場景</th>
            <td>網頁瀏覽、API 請求</td>
            <td>即時聊天、線上遊戲、IoT</td>
            <td>裝置間資料傳輸</td>
        </tr>
        <tr>
            <th>延遲</th>
            <td>高</td>
            <td>低</td>
            <td>低</td>
        </tr>
    </table>
</div>

由上表分析比較WebSockets通訊協定具
- WebSockets 是一種長連線、雙向即時通訊技術，它讓用戶端和伺服器建立起一條持續開通的資料通道，雙方都能主動發送訊息，不需要像傳統 HTTP 那樣反覆重新建立連線，想像它像是在兩台設備之間架了一條隨時能說話的通訊線，速度快、延遲低、很適合需要反應時間短的系統，適合應用於IOT場域。
- WebSockets 是一種長連線、雙向即時通訊技術。它能讓用戶端與伺服器建立一條持續開通的資料通道，雙方可隨時主動傳送訊息，而不需像傳統 HTTP 那樣反覆建立連線。可以將其想像成一條始終保持連接的通訊線路，具備高速與低延遲的特性，非常適合需要快速反應的系統，例如 IoT 裝置即時監控、機器人控制等應用場景。
- 在程式實作層面，前端多以 JavaScript 的 WebSocket 物件建立連線，而伺服器端則可採用 Python（WebSockets、FastAPI）、Node.js 或 Go 等框架實現 WebSocket 服務。

而在此次比賽中我們就使用的Web Sockets這種通訊協定，使Jetson Orin Nano和Raspberry Pi Pico W可以進行資訊交換，像是傳送底盤控制參數，感測器數值交換等。
### WebSockets 的優勢重點
 - 即時雙向通訊
   - 一旦握手成功，伺服器與用戶端可隨時互相發送資料，不必等待請求。
   - 適合需要即時通訊的專案。
 - 降低網路負荷
   - 不需要一直重新請求HTTP連線可以降低Jetson Orin Nano的負荷。
 - 低延遲
   - 傳輸延遲僅為數毫秒，幾乎跟UART的速度馳平。
 - 基於網路層面傳輸
   - 透過網路傳輸不需要實體傳輸線可以避免傳輸線損壞而無法運作。
 - 總結
   - WebSockets幾乎就是物聯網的UART協定，完全目前我們目前的需求，因此我們決定使用WebSockets代替UART傳輸。

 # <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  