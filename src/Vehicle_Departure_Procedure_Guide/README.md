<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Operational Procedure Guide for Vehicle Departure from the Parking Zone - 車輛從停車區出發的操作程序指南</div>
  **Parking Lot Exit Overview - 停車區出發概述。**
- ### Parking Lot Exit program-出發計劃
    ### 中文:
    1.  **系統啟動與方向判斷 (Jetson Orin Nano 職責)**
    - * 車輛啟動時，**主控系統 (Jetson Orin Nano)** 會透過攝影機執行影像識別，首先**確定車輛的預設行駛方向**（逆時針或順時針），隨後識別並鎖定**目標賽道路線的顏色**，作為整個任務的基礎。

    2.  **逆時針方向 (Counter-Clockwise) 行駛邏輯**
    -   * **偵測到綠柱時：** 車輛執行**向左轉 90 度**的換道動作，**前進至綠柱的內側**。隨後，車輛會**向右轉 90 度**，**後退至預定位置**（完成內側換道）。
    -   * **偵測到紅柱時：** 車輛執行**前進**，接著**向左轉 90 度**，**前進至紅柱的外側**。隨後，車輛會**後退並向右轉 90 度**，**後退至預定位置**（完成外側換道或避障）。
    -   * **未偵測到任何柱子時：** 系統將預設車輛**行駛於車道的外側**。

    3.  **順時針方向 (Clockwise) 行駛邏輯**
    -   * **偵測到綠柱時：** 車輛執行**向右轉 90 度**的換道動作，**前進至綠柱的外側**。隨後，車輛會**向左轉 90 度**，**前進至預定位置**（完成外側換道）。
    -   * **偵測到紅柱時：** 車輛執行**向右轉 90 度**的換道動作，**前進至紅柱的內側**。隨後，車輛會**向左轉 90 度**，**前進至預定位置**（完成內側換道）。
    -   * **未偵測到任何柱子時：** 系統將預設車輛**行駛於車道的外側**。
    ### 英文:
    1.  **System Startup and Direction Determination (Jetson Orin Nano Responsibility)**
    - * When the vehicle starts, the **main control system (Jetson Orin Nano)** performs image recognition via the camera to first **determine the vehicle's default driving direction** (Counter-Clockwise or Clockwise). Subsequently, it identifies and locks onto the **color of the target track line**, which serves as the basis for the entire mission.

    2.  **Counter-Clockwise (CCW) Driving Logic**
    - * **Upon detecting a Green Pillar:** The vehicle executes a **90-degree turn to the left** for a lane change, **driving forward to the inner side of the Green Pillar**. Subsequently, the vehicle **turns 90 degrees to the right** and **reverses to a predetermined position** (completing the inner lane change).
    - * **Upon detecting a Red Pillar:** The vehicle **drives forward**, then **turns 90 degrees to the left**, **driving forward to the outer side of the Red Pillar**. Subsequently, the vehicle **reverses, turns 90 degrees to the right**, and **reverses to a predetermined position** (completing the outer lane change or avoidance).
    - * **When no pillars are detected:** The system defaults the vehicle to **drive on the outer side of the lane**.

    3.  **Clockwise (CW) Driving Logic**
    - * **Upon detecting a Green Pillar:** The vehicle executes a **90-degree turn to the right** for a lane change, **driving forward to the outer side of the Green Pillar**. Subsequently, the vehicle **turns 90 degrees to the left** and **drives forward to a predetermined position** (completing the outer lane change).
    - * **Upon detecting a Red Pillar:** The vehicle executes a **90-degree turn to the right** for a lane change, **driving forward to the inner side of the Red Pillar**. Subsequently, the vehicle **turns 90 degrees to the left** and **drives forward to a predetermined position** (completing the inner lane change).
    - * **When no pillars are detected:** The system defaults the vehicle to **drive on the outer side of the lane**.
- **Code running on the Raspberry Pi Pico W controller.-在 Raspberry Pi Pico W 控制器上執行的程式碼。**
    ```python
    # --- Execute rotation based on turn ---
    if turn == 1:
        print("Turning right") # Right turn message
        run_encoder_Auto(500, 45, 180) # Move with encoder and turn
    else:
        print("Turning left") # Left turn message
        run_encoder_Auto(1550, 45, -200) # Move with encoder and turn

    # --- mode 1: Color Decision ---
    mode = 1 # Change mode
    LAST_COLOR = 0 # Reset last color
    color = 0 # Reset color
    print(mode, color) # Debug print
    print('Waiting for color (M,<1..6>[,<...>] or JSON {"color":n})...') # Status message

    while mode == 1 and color == 0: # Loop until color is detected
        json_obj, m_tuple, got_stop = pump_uart(s) # Pump UART for data

        if json_obj:
            v = None # Value variable
            try:
                if "color" in json_obj:
                    v = int(json_obj["color"]) # Get color from JSON
                elif "c" in json_obj:
                    v = int(json_obj["c"]) # Get color from JSON (short key)
            except:
                v = None # Set to None on error
            if v is not None:
                if 1 <= v <= 6:
                    color = v # Set color
                    LAST_COLOR = color # Update last color
                    print("[JSON] color =", color) # Confirmation message
                    break # Break the loop
                else:
                    if DEBUG: print("[IGNORE] JSON color out of range:", v) # Debug print: ignore out of range
                    extract_magenta_from_json(json_obj) # Update magenta data

        if m_tuple:
            first = m_tuple[0] # First value of M command
            if 1 <= first <= 6:
                color = first # Set color
                LAST_COLOR = color # Update last color
                print("[M] color =", color, "raw:", m_tuple) # Confirmation message
                break # Break the loop
            else:
                if DEBUG: print("[IGNORE] M packet in mode1 (not color):", m_tuple) # Debug print: ignore M packet

        if json_obj is None and m_tuple is None:
                    time.sleep(0.002) # Short sleep if no new data
            
    # --- Color-based actions (Skipped for brevity, same as original) ---
    if color == 1:
        print("Color=1") # Status message
        run_encoder_Auto(1900, 70, 0) # Encoder move
        run_encoder_Auto(1500, 70, 180) # Encoder move
        run_encoder_Auto(1200, -45, 0) # Encoder move
    elif color == 2:
        print("Color=2") # Status message
        run_encoder_Auto(1700, 70, 0) # Encoder move
        run_encoder_Auto(1150, -50, -180) # Encoder move
    elif color == 3:
        print("Color=3") # Status message
        run_encoder_Auto(1700, 70, 0) # Encoder move
        run_encoder_Auto(1150, -50, -180) # Encoder move
    elif color == 4:
        print("Color=4") # Status message
        run_encoder_Auto(600, 40, 180) # Encoder move
        run_encoder_Auto(400, 50, 0) # Encoder move
        run_encoder_Auto(1100, 40, -180) # Encoder move
        run_encoder_Auto(800, 50, 0) # Encoder move
    elif color == 5:
        print("Color=5") # Status message
        run_encoder_Auto(600, 40, 180) # Encoder move
        run_encoder_Auto(2200, 60, 0) # Encoder move
        run_encoder_Auto(1400, 40, -180) # Encoder move
        run_encoder_Auto(500, 50, 0) # Encoder move
    elif color == 6:
        print("Color=6") # Status message
        run_encoder_Auto(600, 40, 180) # Encoder move
        run_encoder_Auto(400, 50, 0) # Encoder move
        run_encoder_Auto(1400, 40, -180) # Encoder move
        run_encoder_Auto(800, 50, 0) # Encoder move

    control_motor(0) # Stop motor
    set_servo_angle(0) # Center servo


    ```
## <div align="center">Counter-clockwise green departure process-逆時針綠色出發流程</div>
<div align=center>
<table>
<tr>
<th align="center" width="50%">Preparing to turn left(準備左轉)</th>
<th align="center" width="50%">Start_reversing(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Start_in_green_counterclockwise-1.png"  /></td>
<td align="center" width="50%"><img src="./img/Start_in_green_counterclockwise-2.png"  /></td>
</tr>

<tr>
<th align="center" width="50%">reparing to turn right(準備右轉)</th>
<th align="center" width="50%">Preparing to retreat(準備後退)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Start_in_green_counterclockwise-3.png"  /></td>
<td align="center" width="50%"><img src="./img/Start_in_green_counterclockwise-4.png"  /></td>
</tr>

<tr>
<th align="center" width="50%">Arrive at the designated location(到達預定位子)</th>
<th align="center" width="50%">Video Documentation of the Autonomous Vehicle's Actual Run(自動駕駛車輛實際運行的影片記錄)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Start_in_green_counterclockwise-5.png"  /></td>
<td><a href="https://youtu.be/dxmBH97Rha0" ><img src="./img/01_Counter_clockwise_green_departure_process.jpg" /></a></td>
</tr>
</table>
</div>

## <div align="center">Counter-clockwise red departure process-逆時針紅色出發流程</div>
<div align=center>
<table>
<tr>
<th align="center" width="50%">Preparing to turn left(準備左轉)</th>
<th align="center" width="50%">Start_reversing(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Start_in_red_counterclockwise-1.png"  /></td>
<td align="center" width="50%"><img src="./img/Start_in_red_counterclockwise-2.png"  /></td>
</tr>

<tr>
<th align="center" width="50%">Prepare to back up and turn left(準備後退向左轉)</th>
<th align="center" width="50%">Arrive at the designated location(到達預定位子)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Start_in_red_counterclockwise-3.png"  /></td>
<td align="center" width="50%"><img src="./img/Start_in_green_counterclockwise-4.png"  /></td>
</tr>

<tr>
<th colspan=2>Video Documentation of the Autonomous Vehicle's Actual Run(自動駕駛車輛實際運行的影片記錄)</th>
</tr>
<tr align=center>
<td colspan=2><a href="https://youtu.be/3sPefphX0xI" ><img src="./img/02_Counter_clockwise_red_departure_process.jpg" /></a></td>
</tr>
</table>
</div>

## <div align="center">Counter-clockwise, no color starting process-逆時針沒有顏色出發流程</div>
<div align=center>
<table>
<tr>
<th align="center" width="50%">Preparing to turn left(準備左轉)</th>
<th align="center" width="50%">Start_reversing(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Start_in_no_counterclockwise-1.png"  /></td>
<td align="center" width="50%"><img src="./img/Start_in_no_counterclockwise-2.png"  /></td>
</tr>

<tr>
<th align="center" width="50%">Prepare to back up and turn left(準備後退向左轉)</th>
<th align="center" width="50%">Arrive at the designated location(到達預定位子)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Start_in_no_counterclockwise-3.png"  /></td>
<td align="center" width="50%"><img src="./img/Start_in_no_counterclockwise-4.png"  /></td>
</tr>

<tr>
<th colspan=2>Video Documentation of the Autonomous Vehicle's Actual Run(自動駕駛車輛實際運行的影片記錄)</th>
</tr><tr align=center>
<td colspan=2><a href="https://youtu.be/kS-VRQUwHtw" ><img src="./img/03_Counter_clockwis_no_color_starting_process.jpg" /></a></td>
</tr>
</table>
</div>

## <div align="center">Clockwise Green Departure Process-順時針綠色出發流程</div>
<div align=center>
<table>
<tr>
<th align="center" width="50%">Preparing to turn right(準備右轉)</th>
<th align="center" width="50%">Ready to move forward(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Clockwise Green Departure Process-1.png"  /></td>
<td align="center" width="50%"><img src="./img/Clockwise Green Departure Process-2.png"  /></td>
</tr>

<tr>
<th align="center" width="50%">Preparing to turn left(準備向左轉)</th>
<th align="center" width="50%">Ready to move forward(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Clockwise Green Departure Process-3.png"  /></td>
<td align="center" width="50%"><img src="./img/Clockwise Green Departure Process-4.png"  /></td>
</tr>

<tr>
<th>Arrive at the designated location(到達預定位子)</th>
<th width=50%>Video Documentation of the Autonomous Vehicle's Actual Run(自動駕駛車輛實際運行的影片記錄)</th>
</tr><tr align=center>
<td><img src="./img/Clockwise Green Departure Process-5.png"  /></td>
<td width=50%><a href="https://youtu.be/RobF20wQFs8"><img src="./img/04_Clockwise_Green_Departure_Process.jpg" /></a></td>
</tr>
</table>
</div>

## <div align="center">Clockwise Red Departure Process-順時針紅色出發流程</div>
<div align=center>
<table>
<tr>
<th align="center" width="50%">Preparing to turn right(準備右轉)</th>
<th align="center" width="50%">Ready to move forward(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Clockwise red Departure Process-1.png"  /></td>
<td align="center" width="50%"><img src="./img/Clockwise red Departure Process-2.png"  /></td>
</tr>

<tr>
<th align="center" width="50%">Preparing to turn left(準備向左轉)</th>
<th align="center" width="50%">Ready to move forward(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Clockwise red Departure Process-3.png"  /></td>
<td align="center" width="50%"><img src="./img/Clockwise red Departure Process-4.png"  /></td>
</tr>

<tr>
<th>Arrive at the designated location(到達預定位子)</th>
<th>Video Documentation of the Autonomous Vehicle's Actual Run(自動駕駛車輛實際運行的影片記錄)</th>
</tr><tr align=center>
<td><img src="./img/Clockwise red Departure Process-5.png"  /></td>
<td><a href="https://youtu.be/_NSuhBujNAg"><img src="./img/05_Clockwise_Red_Departure_Process.jpg" /></a></td>
</tr>
</table>
</div>

## <div align="center">Clockwise green center departure process-順時針綠色中間出發流程</div>
<div align=center>
<table>
<tr>
<th align="center" width="50%">Preparing to turn right(準備右轉)</th>
<th align="center" width="50%">Preparing to turn left(準備向左轉)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Clockwise green center departure process-1.png"  /></td>
<td align="center" width="50%"><img src="./img/Clockwise green center departure process-2.png"  /></td>
</tr>

<tr>
<th align="center" width="50%">Ready to move forward(準備向前)</th>
<th align="center" width="50%">Arrive at the designated location(到達預定位子)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Clockwise green center departure process-3.png"  /></td>
<td align="center" width="50%"><img src="./img/Clockwise green center departure process-4.png"  /></td>
</tr>

<tr>
<th colspan=2>Video Documentation of the Autonomous Vehicle's Actual Run(自動駕駛車輛實際運行的影片記錄)</th>
</tr>
<tr align=center>
<td colspan=2><a href="https://youtu.be/J43t55lzJF8" ><img src="./img/06_Clockwise_green_center_departure_process.jpg" /></a></td>
</tr>
</table>
</div>

## <div align="center">Clockwise red center departure process-順時針紅色中間出發流程</div>
<div align=center>
<table>
<tr>
<th align="center" width="50%">Preparing to turn right(準備右轉)</th>
<th align="center" width="50%">Ready to move forward(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Clockwise red center departure process-1.png"  /></td>
<td align="center" width="50%"><img src="./img/Clockwise red center departure process-2.png"  /></td>
</tr>

<tr>
<th align="center" width="50%">Preparing to turn left(準備向左轉)</th>
<th align="center" width="50%">Ready to move forward(準備向前)</th>
</tr><tr>
<td align="center" width="50%"><img src="./img/Clockwise red center departure process-3.png"  /></td>
<td align="center" width="50%"><img src="./img/Clockwise red center departure process-4.png"  /></td>
</tr>

<tr>
<th>Arrive at the designated location(到達預定位子)</th>
<th>Video Documentation of the Autonomous Vehicle's Actual Run(自動駕駛車輛實際運行的影片記錄)</th>
</tr><tr align=center>
<td><img src="./img/Clockwise red center departure process-5.png"  /></td>
<td><a href="https://youtu.be/4ebtIaPdVeI" ><img src="./img/07_Clockwise_red_center_departure_process.jpg" /></a></td>
</tr>
</table>
</div>


# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
