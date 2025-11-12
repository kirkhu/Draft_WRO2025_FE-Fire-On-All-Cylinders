<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Vehicle Parking Procedure Guide - 車輛停車程序指南</div>
###  **Code Logic Description: Parking Task After Three Laps - 程式碼邏輯說明：三圈後停車任務。**
- ### Parking program-停車計劃
    ### 中文:
    1.  **停車區識別與入庫準備 (Jetson Orin Nano)**
      * 在車輛行駛過程中，**Jetson Orin Nano 系統**持續透過攝影機偵測**洋紅色方塊**以識別**停車場的精確位置**。
      * 當車輛**完成第三圈**時，自駕車會執行**轉彎動作進入停車區**，並持續**向前行駛**，直到**紅外線感測器偵測到牆壁**。此時，車輛隨即執行**後退轉彎**，並開始調整車體朝向停車場的精確方向。
    2.  **精準定位與入庫起始 (Jetson Orin Nano)**
      * 車輛朝向停車場區域後，**Jetson Orin Nano** 透過攝影機**即時測量**車輛與**洋紅色停車位標記**之間的**橫向距離**，以確保維持適當的進場間距。
      * 為確認車輛已抵達**精確的入庫起始位置**，程式持續監測攝影機所擷取的**洋紅色標誌面積**。
      * 一旦**洋紅色區域的面積小於 100**，即確認完成定位。車輛隨即**沿牆邊線循跡 100 度**，隨後執行**轉入停車位的動作**。
    3.  **平行倒車入庫與姿態控制 (Raspberry Pi Pico W)**
      * 在確認目標停車方向後，系統將執行**模擬真實世界的平行停車**動作。
      * 首先，**Jetson Orin Nano** 計算並設定轉向**伺服馬達的起始角度**及**直流驅動馬達的數值**。
      * 在倒車入庫過程中，**主控單元 (Raspberry Pi Pico W)** 負責**讀取來自 Jetson Orin Nano 的陀螺儀角度數據**（或直接執行姿態控制），以**精確控制車輛的姿態與轉向角度**，並**同步調整伺服馬達**，從而**完成自動平行倒車入庫動作**。
    ### 英文:
    1.  **Parking Zone Identification and Entry Preparation (Jetson Orin Nano)**
      * While the vehicle is driving, the **Jetson Orin Nano system** continuously identifies the **precise location of the parking lot** by detecting the **magenta square** via the camera.
      * When the vehicle **completes the third lap**, the autonomous car executes a **turn to enter the parking zone** and continues to **drive forward** until the **infrared sensor detects a wall**. At this point, the vehicle immediately performs a **reverse turn** and adjusts its body orientation towards the parking lot's precise direction.

    2.  **Precise Positioning and Bay Entry Start (Jetson Orin Nano)**
      * Once the vehicle is oriented towards the parking area, the **Jetson Orin Nano** **measures the lateral distance** between the vehicle and the **magenta parking bay marker** in real-time via the camera, ensuring an appropriate entry gap is maintained.
      * To confirm the vehicle has reached the **precise entry starting position**, the program continuously monitors the **area of the magenta marker** captured by the camera.
      * Once the **area of the magenta region is less than 100**, the positioning is confirmed. The vehicle then continues to **follow the wall line for 100 degrees** , followed by executing the **turning action to enter the parking bay**.

    3.  **Parallel Reverse Parking and Attitude Control (Raspberry Pi Pico W)**
      * After confirming the target parking direction, the system executes a maneuver that **simulates real-world parallel parking**.
      * First, the **Jetson Orin Nano** calculates and sets the **initial angle of the steering servo motor** and the **value for the DC drive motor**.
      * During the reverse parking maneuver, the **main control unit (Raspberry Pi Pico W)** is responsible for **reading the gyroscope angle data** from the Jetson Orin Nano (or directly implementing attitude control), which allows for **precise control over the vehicle's posture and steering angle**. The Pico W simultaneously adjusts the servo motor, thereby **completing the automatic parallel reverse parking action**.
    

- **Code Executed on the Raspberry Pi Pico W Controller- Raspberry Pi Pico W 控制器上執行的程式碼。**
    ```python
    while mode == 3:
        json_obj, _, got_stop = pump_uart(s) # Pump UART for data
        extract_magenta_from_json(json_obj) # Update magenta data
        while abs(yaw) < 85: # Loop while yaw is less than 85 degrees
            json_obj, _, got_stop = pump_uart(s) # Pump UART for data
            if json_obj:
                if "yaw" in json_obj:
                    try:
                        yaw = float(json_obj["yaw"]) # Update yaw
                    except:
                        pass
                extract_magenta_from_json(json_obj) # Update magenta data
            if turn == 2: # Turn 2 (e.g., Left start)
                set_servo_angle(45) # Set servo angle
                control_motor(35) # Set motor speed
            else: # Turn 1 (e.g., Right start)
                set_servo_angle(-40) # Set servo angle
                control_motor(35) # Set motor speed                 
        motor_brake() # Stop motor
        set_servo_angle(0) # Center servo
        mode = 4 # Change mode
                
            
    while mode == 4:
        a0_value = A0.read_u16() # Read ADC A0 value
        time_a0=time.time() # Record start time
        while a0_value > 64800 and time.time()- time_a0 < 5: # Loop while A0 value is high and time limit not reached
            a0_value = A0.read_u16() # Read ADC A0 value
            extract_magenta_from_json(json_obj) # Update magenta data 
            json_obj, _, got_stop = pump_uart(s) # Pump UART for data
            if json_obj:
                if "yaw" in json_obj:
                    try:
                        yaw = float(json_obj["yaw"]) # Update yaw
                    except:
                        pass
                extract_magenta_from_json(json_obj) # Update magenta data  
            set_servo_angle(0) # Center servo
            control_motor(30) # Drive motor forward
        control_motor(-40) # Drive motor backward
        time.sleep(0.1) # Wait for a short time
        control_motor(0) # Stop motor
        mode = 5 # Change mode

    while mode == 5:
        json_obj, _, got_stop = pump_uart(s) # Pump UART for data
        while abs(yaw) < 177: # Loop while yaw is less than 177 degrees
            extract_magenta_from_json(json_obj) # Update magenta data
            json_obj, _, got_stop = pump_uart(s) # Pump UART for data
            if json_obj:
                if "yaw" in json_obj:
                    try:
                        yaw = float(json_obj["yaw"]) # Update yaw
                    except:
                        pass
            if turn == 2: # Turn 2
                set_servo_angle(-180) # Set servo angle
                control_motor(-40) # Drive motor backward
            else: # Turn 1
                set_servo_angle(180) # Set servo angle
                control_motor(-40) # Drive motor backward                  
        motor_brake() # Stop motor
        set_servo_angle(0) # Center servo
        mode = 6 # Change mode
                
    while mode == 6:
        json_obj, m_tuple, got_stop = pump_uart(s) # Pump UART for data
        extract_magenta_from_json(json_obj) # Update magenta data
        while magArea > 70: # Loop while magenta area is greater than 70
            extract_magenta_from_json(json_obj) # Update magenta data
            json_obj, m_tuple, got_stop = pump_uart(s) # Pump UART for data
            if json_obj:
                try:
                    if "leftArea" in json_obj:
                        leftArea = int(json_obj.get("leftArea", leftArea)) # Update left area
                    if "rightArea" in json_obj:
                        rightArea = int(json_obj.get("rightArea", rightArea)) # Update right area
                        except:
                            pass
            if turn ==2: # Turn 2
                if magArea > 3000:
                    error = magCX - 202 # Calculate error based on CX
                    Servo_angle = int(error*0.15 + (error - error1)*0.2) # PD control
                    error1 = error # Update previous error
                    set_servo_angle(Servo_angle) # Set servo angle
                    control_motor(40) # Drive motor forward
                else:
                    error = leftArea - 6500 # Calculate error based on left area
                    Servo_angle = int(error*0.005 + (error - error1)*0.01) # PD control
                    error1 = error # Update previous error
                    set_servo_angle(Servo_angle) # Set servo angle
                    control_motor(40) # Drive motor forward
            else: # Turn 1
                if magArea > 3000:
                    error = magCX - 490 # Calculate error based on CX
                    Servo_angle = int(error*0.13 + (error - error1)*0.2) # PD control
                    error1 = error # Update previous error
                    set_servo_angle(Servo_angle) # Set servo angle
                    control_motor(40) # Drive motor forward
                else:
                    error = 7000 - rightArea # Calculate error based on right area
                    Servo_angle = int(error*0.005 + (error - error1)*0.008) # PD control
                    error1 = error # Update previous error
                    set_servo_angle(Servo_angle) # Set servo angle
                    control_motor(40) # Drive motor forward
        control_motor(-50) # Drive motor backward
        time.sleep(0.1) # Wait for a short time
        control_motor(0) # Stop motor
        time.sleep(0.5) # Wait for a short time
        mode = 7 # Change mode

    while mode == 7:
        json_obj, _, got_stop = pump_uart(s) # Pump UART for data
        while abs(yaw) > 110: # Loop while yaw is greater than 110 degrees
            json_obj, _, got_stop = pump_uart(s) # Pump UART for data
            if json_obj:
                if "yaw" in json_obj:
                    try:
                        yaw = float(json_obj["yaw"]) # Update yaw
                    except:
                        pass
            if turn == 2: # Turn 2  
                set_servo_angle(-180) # Set servo angle
                control_motor(-38) # Drive motor backward
            else: # Turn 1
                set_servo_angle(180) # Set servo angle
                control_motor(-38) # Drive motor backward
        control_motor(50) # Drive motor backward
        time.sleep(0.1) # Wait for a short time
        control_motor(0) # Stop motor
        mode =8 # Change mode 
    while mode == 8:
        json_obj, _, got_stop = pump_uart(s) # Pump UART for data
        a1_value = A1.read_u16() # Read ADC A1 value
        while abs(yaw) < 140 and a1_value > 64800: # Loop while yaw < 140 and A1 is high
            a1_value = A1.read_u16() # Read ADC A1 value
            json_obj, _, got_stop = pump_uart(s) # Pump UART for data
            if json_obj:
                if "yaw" in json_obj:
                    try:
                        yaw = float(json_obj["yaw"]) # Update yaw
                    except:
                        pass
            if turn == 2: # Turn 2  
                set_servo_angle(180) # Set servo angle
                control_motor(-35) # Drive motor backward
            else: # Turn 1
                set_servo_angle(-180) # Set servo angle
                control_motor(-35) # Drive motor backward  
        control_motor(40) # Drive motor forward
        time.sleep(0.1) # Wait for a short time
        control_motor(0) # Stop motor
        set_servo_angle(0) # Center servo
        mode =9 # Change mode
    while mode == 9:
        json_obj, _, got_stop = pump_uart(s) # Pump UART for data
        a0_value = A0.read_u16() # Read ADC A0 value
        while abs(yaw) < 160 : # Loop while yaw is less than 160 degrees
            a0_value = A0.read_u16() # Read ADC A0 value
            json_obj, _, got_stop = pump_uart(s) # Pump UART for data
            if json_obj:
                if "yaw" in json_obj:
                    try:
                        yaw = float(json_obj["yaw"]) # Update yaw
                    except:
                        pass
            if turn == 2: # Turn 2  
                set_servo_angle(-180) # Set servo angle
                control_motor(35) # Drive motor forward
            else: # Turn 1
                set_servo_angle(180) # Set servo angle
                control_motor(35) # Drive motor forward  
        control_motor(-40) # Drive motor backward
        time.sleep(0.1) # Wait for a short time
        control_motor(0) # Stop motor
        set_servo_angle(0) # Center servo
        mode =10 # Change mode 
    while mode == 10:
        json_obj, _, got_stop = pump_uart(s) # Pump UART for data
        a0_value = A0.read_u16() # Read ADC A0 value
        while abs(yaw) < 177 : # Loop while yaw is less than 177 degrees
            a0_value = A0.read_u16() # Read ADC A0 value
            json_obj, _, got_stop = pump_uart(s) # Pump UART for data
            if json_obj:
                if "yaw" in json_obj:
                    try:
                        yaw = float(json_obj["yaw"]) # Update yaw
                    except:
                        pass
            if turn == 2: # Turn 2  
                set_servo_angle(180) # Set servo angle
                control_motor(-35) # Drive motor backward
            else: # Turn 1
                set_servo_angle(-180) # Set servo angle
                control_motor(-35) # Drive motor backward  
        control_motor(40) # Drive motor backward
        time.sleep(0.1) # Wait for a short time
        control_motor(0) # Stop motor
        set_servo_angle(0) # Center servo
        mode =11 # Change mode
    while mode == 11:
        motor_brake() # Apply motor brake
    ```
## <div align="center">Counter-Clockwise Vehicle Parking Procedure - 逆時針方向車輛停車流程</div>
<div align=center>
<table>
<tr>
<th align="center" width="50%">The vehicle proceeds forward through the parking area. </th>
<th align="center"  width="50%"> The vehicle turns to the right, with its front facing the outer wall at a 90-degree azimuth.</th>
</tr>
<tr>
<td align="center"  width="50%"><img src="img/parking_1-1.png" /> </td>
<td align="center"  width="50%"><img src="img/parking_1-2.png" /></td>

</tr>
<tr>
<th align="center"  width="50%">The vehicle drives straight toward the 90-degree azimuth until the infrared sensor detects the outer wall, then brakes.</th>
<th align="center"  width="50%">The vehicle reverses towards the left-rear until its yaw angle exceeds 177 degrees.</th>
</tr>
<tr>
<td align="center"  width="50%"><img src="img/parking_1-3.png" /></td>
<td align="center"  width="50%"><img src="img/parking_1-4.png" /></td>
</tr>

<tr>
<th align="center"  width="50%"> The vehicle follows the outer wall until the area of the magenta wall contour is less than 100, then the vehicle moves forward another 100 degrees.</th>
<th align="center"  width="50%">The vehicle reverses towards the rear-left into the parking area until its heading angle reaches 123 degrees.</th>
</tr>
<tr>
<td align="center"  width="50%"><img src="img/parking_1-5.png" /> </td>
<td align="center"  width="50%"><img src="img/parking_1-6.png" /> </td>
</tr>
<tr>
<th align="center"  width="50%">The vehicle reverses towards the rear-right into the parking area until its heading angle reaches 177 degrees.</th>
<th align="center"  width="50%">Vehicle Parking Finished </th>
</tr>
<tr>
<td align="center"  width="50%"><img src="img/parking_1-7.png" /> </td>
<td align="center"  width="50%"><img src="img/parking_1-8.png" /> </td>
</tr>
<tr>
<th colspan = 2>Video Documentation of the Autonomous Vehicle's Actual Run</th>
</tr>
<tr align=center>
<td align=center colspan = 2><a href="https://youtu.be/ZJdazgHVCGY" ><img src="./img/Clockwise_Vehicle_Parking_Procedure.jpg" ALT="Clockwise_Vehicle_Parking_Procedure"/></a></td>
</tr>


</table>
</div>

## <div align="center">Clockwise Vehicle Parking Procedure - 順時針方向停車輛車流程</div>

<table>
<tr>
<th align="center"  width="50%"> The vehicle proceeds forward through the parking area.</th>
<th align="center"  width="50%"> The vehicle turns to the left, with its front facing the outer wall at a 90-degree azimuth.</th>
</tr>
<tr>
<td align="center"  width="50%"> <img src="img/parking_2-1.png" /></td>
<td align="center"  width="50%"> <img src="img/parking_2-2.png" /></td>
</tr>

<tr>
<th align="center"  width="50%">The vehicle drives straight toward the 90-degree azimuth until the infrared sensor detects the outer wall, then brakes. </th>
<th align="center"  width="50%">The vehicle reverses towards the right-rear until its yaw angle exceeds 177 degrees. </th>
</tr>
<tr>
<td align="center"  width="50%"><img src="img/parking_2-3.png" /> </td>
<td align="center"  width="50%"><img src="img/parking_2-4.png" /> </td>
</tr>


<tr>
<th align="center"  width="50%"> The vehicle follows the outer wall until the area of the magenta wall contour is less than 100, then the vehicle moves forward another 100 degrees.</th>
<th align="center"  width="50%">The vehicle reverses towards the rear-right into the parking area until its heading angle reaches 123 degrees. </th>
</tr>
<tr>
<td align="center"  width="50%"><img src="img/parking_2-5.png" /></td>
<td align="center"  width="50%"><img src="img/parking_2-6.png" /> </td>
</tr>


<tr>
<th align="center"  width="50%">The vehicle reverses towards the rear-left into the parking area until its heading angle reaches 177 degrees. </th>
<th align="center"  width="50%">Vehicle Parking Finished </th>
</tr>
<tr>
<td align="center"  width="50%"><img src="img/parking_2-7.png"  /> </td>
<td align="center"  width="50%"><img src="img/parking_2-8.png"  /> </td>
</tr>

<tr>
<th colspan = 2>Video Documentation of the Autonomous Vehicle's Actual Run</th>
</tr>
<tr>
<td align=center colspan = 2><a href="https://youtu.be/eZsEFtIm0SM" ><img src="./img/Counter_Clockwise_Vehicle_Parking_Procedure.jpg" ALT="Counter_Clockwise_Vehicle_Parking_Procedure"/></a></td>
</tr>


</table>
</div>
  
  

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
