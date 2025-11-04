<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Explanation of the parking method-出發方法說明</div>
  **The following is the code for "Departure". - 以下是出發出發的程式碼。**
- ### Parking program-出發計劃
    ### 中文:
    - 車輛啟動時，主控系統 (Jetson Orin Nano) 透過攝影機執行影像識別，首先判斷車輛的預設行駛方向，隨後識別並鎖定目標賽道路線的顏色。
    - 逆時針方向:若行車方向為逆時針方向，當車輛偵測到綠柱時：車輛向左轉90度，往前進到綠柱內側，車輛會向右轉90度，後退至預定位置。偵測到紅柱時：車輛前進，車輛向左轉90度，往前進到紅柱外側，車輛會後退向右轉90度，後退至預定位置。未偵測到任何柱子時：則預設行駛於車道外側。
    - 順時針方向:若行車方向為順時針方向，當車輛偵測到綠住時：車輛會向右轉90度，往前進到綠柱外側，車輛會向左轉90度，前進至預定位置。偵測到紅柱車輛時：車輛會向右轉90度，往前進到紅柱內側，車輛會向左轉90度，前進至預定位置。若未偵測到任何柱子時：則預設行駛於車道外側。
- **Code running on the Raspberry Pi Pico W controller.-在 Raspberry Pi Pico W 控制器上執行的程式碼。**
    ```

    ```
  - ## Counter-clockwise green departure process-逆時針綠色出發流程
<div align=center>
<table>
<tr>
<th>Preparing to turn left(準備左轉)</th>
<th>Start_reversing(準備向前)</th>
</tr><tr>
<td align=center><img src="./img/Start_in_green_counterclockwise-1.png" width=400 /></td>
<td align=center><img src="./img/Start_in_green_counterclockwise-2.png" width=400 /></td>
</tr>
</table>
</div>
<div align=center>
<table>
<tr>
<th>reparing to turn right(準備右轉)</th>
<th>Start_reversing(準備向前)</th>
</tr><tr>
<td align=center><img src="./img/Start_in_green_counterclockwise-3.png" width=400 /></td>
<td align=center><img src="./img/Start_in_green_counterclockwise-4.png" width=400 /></td>
</tr>
</table>
</div>
<div align=center>
<table>
<th>reparing to turn right(準備右轉)</th>
</tr><tr>
<td align=center><img src="./img/Start_in_green_counterclockwise-3.png" width=400 /></td>
</table>
</div>

  

- ## Counter-clockwise red departure process-逆時針紅色出發流程
<div align=center>

  |Preparing to turn left(準備左轉)|Start_reversing(開始倒車)|Parking_ends(停車處結束)|
  |:---:|:---:|:---:|
  |<div align="center"> <img src="./img/Prepare_to_reverse.png"  alt="Prepare_to_reverse"></div>|<div align="center"> <img src="./img/Start_reversing.png"  alt="Start_reversing"></div>|<div align="center"> <img src="./img/Parking_ends.png"  alt="Parking_ends"></div>|

- ## Counter-clockwise, no color starting process-逆時針沒有顏色出發流程
<div align=center>

  |Preparing to turn left(準備左轉)|Start_reversing(開始倒車)|Parking_ends(停車處結束)|
  |:---:|:---:|:---:|
  |<div align="center"> <img src="./img/Prepare_to_reverse.png"  alt="Prepare_to_reverse"></div>|<div align="center"> <img src="./img/Start_reversing.png"  alt="Start_reversing"></div>|<div align="center"> <img src="./img/Parking_ends.png"  alt="Parking_ends"></div>| 

- ## Clockwise Green Departure Process-順時針綠色出發流程
<div align=center>

  |Preparing to turn right(準備右轉)|Start_reversing(開始倒車)|Parking_ends(停車處結束)|
  |:---:|:---:|:---:|
  |<div align="center"> <img src="./img/Prepare_to_reverse.png"  alt="Prepare_to_reverse"></div>|<div align="center"> <img src="./img/Start_reversing.png"  alt="Start_reversing"></div>|<div align="center"> <img src="./img/Parking_ends.png"  alt="Parking_ends"></div>| 

- ## Clockwise Green Departure Process-順時針紅色出發流程
<div align=center>

  |Preparing to turn right(準備右轉)|Start_reversing(開始倒車)|Parking_ends(停車處結束)|
  |:---:|:---:|:---:|
  |<div align="center"> <img src="./img/Prepare_to_reverse.png"  alt="Prepare_to_reverse"></div>|<div align="center"> <img src="./img/Start_reversing.png"  alt="Start_reversing"></div>|<div align="center"> <img src="./img/Parking_ends.png"  alt="Parking_ends"></div>| 

- ## Clockwise, the green departure process in the middle-順時針中間綠色出發流程
<div align=center>

  |Preparing to turn right(準備右轉)|Start_reversing(開始倒車)|Parking_ends(停車處結束)|
  |:---:|:---:|:---:|
  |<div align="center"> <img src="./img/Prepare_to_reverse.png"  alt="Prepare_to_reverse"></div>|<div align="center"> <img src="./img/Start_reversing.png"  alt="Start_reversing"></div>|<div align="center"> <img src="./img/Parking_ends.png"  alt="Parking_ends"></div>|

- ## Clockwise, red starting process-順時針中間紅色出發流程
<div align=center>

  |Preparing to turn right(準備右轉)|Start_reversing(開始倒車)|Parking_ends(停車處結束)|
  |:---:|:---:|:---:|
  |<div align="center"> <img src="./img/Prepare_to_reverse.png"  alt="Prepare_to_reverse"></div>|<div align="center"> <img src="./img/Start_reversing.png"  alt="Start_reversing"></div>|<div align="center"> <img src="./img/Parking_ends.png"  alt="Parking_ends"></div>|


# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
