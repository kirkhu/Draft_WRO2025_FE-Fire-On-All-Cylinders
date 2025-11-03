<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Explanation of the parking method-出發方法說明</div>
  **The following is the code for "Departure". - 以下是出發出發的程式碼。**
- ### Parking program-出發計劃
    ### 中文:
    - 車輛啟動時，主控系統 (Jetson Orin Nano) 透過攝影機執行影像識別，首先判斷車輛的預設行駛方向，隨後識別並鎖定目標賽道路線的顏色。
    - 逆時針方向:若行車方向為逆時針方向，當車輛偵測到綠柱時：車輛向左轉90度，往前進到綠柱內側，車輛會向右轉90度，後退至預定位置。偵測到紅柱時：車輛前進，車輛向左轉90度，往前進到紅柱外側，車輛會後退向右轉90度，後退至預定位置。未偵測到任何柱子時：則預設行駛於車道外側。
    - 順時針方向:若行車方向為順時針方向，當車輛偵測到綠住時：車輛會向右轉90度，往前進到綠柱外側，車輛會向左轉90度，前進至預定位置。偵測到紅柱車輛時：車輛會向右轉90度，往前進到紅柱內側，車輛會向左轉90度，前進至預定位置。若未偵測到任何柱子時：則預設行駛於車道外側。


# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
