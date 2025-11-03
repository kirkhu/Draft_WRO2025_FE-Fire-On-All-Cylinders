<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Explanation of the parking method-出發方法說明</div>
  **The following is the code for "Departure".-以下是出發出發的程式碼。**
- ### Parking program-出發計劃
    ### 中文:
    - 在車輛從停車區啟動之前，我們會利用 CSI 鏡頭擷取的畫面，並結合感興趣區域 (ROI) 來預判行車方向。此判斷邏輯是透過比較 ROI_1 和 ROI_2 的面積：若 ROI_1 面積大於 ROI_2 面積，則判定本次行車方向為順時針方向；反之，若 ROI_2 面積大於 ROI_1 面積，則判定為逆時針方向。一旦行車方向確定，車輛隨即駛出停車區，之後系統會立即偵測車道上是否存在交通標誌積木 (即紅 、綠色交通標誌)，並根據偵測到的顏色執行相應的變道 (Lane Change) 決策。


# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
