<div align=center> <img src="../../../other/img/logo.png" width = 300 alt=" logo"> </div>

## <div align="center">Obstacle_Challenge Code Overview</div> 
根據各控制板的特點，我們對賽車所需的複雜操作進行了分配：

Based on the characteristics of each control board, we distributed the complex operations required for the race vehicle:

   ### 中文:
   1. 這次，Jetson Orin Nano除了具備影像辨識和方向偵測功能外，還新增了障礙物辨識功能。憑藉其強大的運算能力，Jetson Orin Nano能夠進行即時影像分析與處理，精準偵測車輛行駛方向，同時快速辨識並避開路徑上的障礙物，進而提升自動駕駛的穩定性與安全性。
   2. 此外，這次樹莓派 Pico W 不僅要控制直流馬達轉速和車輛轉向，還需要使用紅外線偵測車輛與牆壁的距離。憑藉其高效的 GPIO 控制能力，樹莓派 Pico W 可以進行精確的距離測量和硬體管理，確保車輛安全停放在停車場內，並保持適當的安全距離。
   ### 英文:
   <ol>
   <li>
    This time, in addition to handling sidewall image recognition and direction detection, the Jetson Orin Nano has added an obstacle block recognition feature. Leveraging its powerful computing capabilities, the Jetson Orin Nano can perform real-time image analysis and processing, accurately detecting the vehicle's direction while also quickly recognizing and avoiding obstacles in its path, thereby enhancing the stability and safety of autonomous driving. 
   </li>
   <li>
    Additionally, this time, the Raspberry Pi Pico not only controls the DC motor speed and vehicle steering but also needs to detect the distance to the parking lot sidewall. Utilizing its efficient GPIO control capabilities, the Raspberry Pi Pico can perform precise distance measurements and hardware management, ensuring the vehicle parks safely in the lot while maintaining an appropriate distance.
   </li>
   </ol>

 - ### Jetson Orin Nano library-Jetson Orin Nano 庫
    ### 中文:
    影像辨識、影像處理與視覺辨識函式等功能已整合到functions.py模組中，可直接導入使用。這些模組的功能如下：

    detect_color_final()該系統透過偵測地面標線的顏色來實現路徑或車道追蹤等應用。此外，該系統還能偵測交通標誌的座標，並將這些座標資料記錄下來以便進一步分析和處理。
    ### 英文:
    The functions for image recognition, front-wheel servo motor proportional steering control, and ground line color recognition have been integrated into the [function.py](../common/function.py) module and can be directly imported for use.
    The functions of these modules are as follows:
    - The explanations for `process_roi()` and `pd_control()` can be found in the **[Open Challenge Code Overview](../Open_Challenge/README.md) section**, so they will not be repeated here.

    - `detect_color_final()`: The system detects the color of ground lines to enable applications such as path or lane tracking. Additionally, the system detects the coordinates of traffic signs and records this coordinate data for further analysis and processing.
       ```
          def detect_color_final(undistorted_frame, last_diffs, start_points, end_points, slope_values, curvature_factors, colors):
              """Detect specific color regions, return the Y coordinates of color centers, and calculate X differences for red and green curves."""
              hsv_frame = cv2.cvtColor(undistorted_frame, cv2.COLOR_BGR2HSV)
              color_y_positions = []
              pink_positions = [0] * 4
              center_x, center_y = 0, 0
              diffs = {'Red': 0, 'Green': 0, 'Pink_Red': 0, 'Pink_Green': 0}

              for color, (lower, upper, bgr) in color_ranges_final.items():
                  lower = np.array(lower, dtype=np.uint8)
                  upper = np.array(upper, dtype=np.uint8)
                  color_mask = cv2.inRange(hsv_frame, lower, upper)
                  contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                  if contours:
                      if color == 'Pink':
                          sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
                          top_two_contours = [cnt for cnt in sorted_contours[:2] if cv2.contourArea(cnt) > 500]
                          for i, cnt in enumerate(top_two_contours):
                              x, y, w, h = cv2.boundingRect(cnt)
                              center_x = x + w // 2
                              center_y = y + h // 2
                              pink_positions[2*i:2*i+2] = [center_x, center_y]
                              cv2.rectangle(undistorted_frame, (x, y), (x + w,  y + h), bgr, 2)
                              cv2.circle(undistorted_frame, (center_x, center_y), 5, bgr, -1)
                          else:
                              largest_contour = max(contours, key=cv2.contourArea)
                              if cv2.contourArea(largest_contour) > 600:
                                  x, y, w, h = cv2.boundingRect(largest_contour)
                                  center_x = x + w // 2
                                  center_y = y + h // 2
                                  color_y_positions.append(center_y)
                                  cv2.rectangle(undistorted_frame, (x, y), (x + w, y + h), bgr, 2)
                                  cv2.circle(undistorted_frame, (center_x, center_y), 5, bgr, -1)
                              else:
                                  color_y_positions.append(0)

                    red_curve_points, green_curve_points = draw_multiple_curves(undistorted_frame, start_points, end_points, slope_values, curvature_factors, colors)
            
                if color == 'Red':
                    diffs['Red'] = calculate_x_diff(center_x, center_y, red_curve_points, last_diffs['Red'], undistorted_frame, (0, 0, 255))
                elif color == 'Green':
                    diffs['Green'] = calculate_x_diff(center_x, center_y, green_curve_points, last_diffs['Green'], undistorted_frame, (0, 255, 0))
                elif color == 'Pink':
                    diffs['Pink_Red'] = calculate_x_diff(pink_positions[0], pink_positions[1], red_curve_points, last_diffs['Pink_Red'], undistorted_frame, (255, 192, 203))
                    diffs['Pink_Green'] = calculate_x_diff(pink_positions[0], pink_positions[1], green_curve_points, last_diffs['Pink_Green'], undistorted_frame, (255, 192, 203))
            else:
                color_y_positions.append(0)
                pink_positions[:] = [0, 0, 0, 0]
        
          return color_y_positions, pink_positions, diffs['Red'], diffs['Green'], diffs['Pink_Red'], diffs['Pink_Green']
        ```
     - `calculate_x_diff`: Using the coordinates of traffic signs along with **raw_multiple_curves**, calculate the current coordinates and the ideal coordinates to enable `pd_control()` for PD tracking.
        ```
            def calculate_x_diff(center_x, center_y, curve_points, last_diff, frame, color):
                """Calculate the X difference between the center point and curve point."""
                max_curve_y = max(pt[1] for pt in curve_points)
                if center_y < max_curve_y:
                    for curve_x, curve_y in curve_points:
                        if abs(curve_y - center_y) < 2:
                            cv2.circle(frame, (curve_x, curve_y), 6, color, -1)
                            return curve_x - center_x
                    return last_diff
                return 0
       ```

    - `draw_multiple_curves`: Use `detect_color_final()` to obtain and calculate the coordinates of the traffic sign blocks, then use Bézier curves to determine the x-values of the traffic sign blocks at the same y-coordinate. This will allow the calculation of deviation errors.
       ```
        def draw_multiple_curves(undistorted_frame, start_points, end_points, slope_values, curvature_factors, colors, thickness=2):
        """
        Draw multiple curves with different starting points, endpoints, slopes, and curvatures on the image, and return the coordinate list of the red curve.
        """
        red_curve_points = []  # store the coordinates of the points on the red curve.
        green_curve_points = []  # store the coordinates of the points on the green curve.


        for start_point, end_point, slope, curvature, color in zip(start_points, end_points, slope_values, curvature_factors, colors):
            x1, y1 = start_point
            x2, y2 = end_point

            # Calculate the position of the intermediate control points to control the curvature.
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
           control_x = mid_x
           control_y = int(mid_y - curvature * slope * (x2 - x1))  # Use curvature and slope to adjust the intermediate control points.

           # Draw using Bézier curves.
           curve_points = []
           for t in np.linspace(0, 1, 100):
               xt = (1 - t)**2 * x1 + 2 * (1 - t) * t * control_x + t**2 * x2
               yt = (1 - t)**2 * y1 + 2 * (1 - t) * t * control_y + t**2 * y2
               curve_points.append((int(xt), int(yt)))

           #  If it is a red curve, save the point coordinates.
           if color == (0, 0, 255):  # Red curve.
               red_curve_points = curve_points
           if color == (0, 255, 0):  # Green curve.
               green_curve_points = curve_points

           # Draw the curve.
           for i in range(len(curve_points) - 1):
               cv2.line(undistorted_frame, curve_points[i], curve_points[i + 1], color, thickness)

       return red_curve_points,green_curve_points  # Return the coordinates of the points on the red curve.

      ```


 - ### Obstacle_Challenge Code Overview of Jetson Orin Nano-Jetson Orin Nano 障礙挑戰程式碼概述
   - #### Obstacle_Challenge Code Program Jetson Orin Nano Libraries-障礙挑戰程式碼程式 Jetson Orin Nano 函式庫
    
      ```
      import time
      import os, sys, math, json, threading, asyncio
      import cv2
      import numpy as np
      import websockets
      import Jetson.GPIO as GPIO
      from websockets.exceptions import ConnectionClosed
      from smbus2 import SMBus
      import functions_jetson as fj
      sys.path.append(os.path.abspath(os.path.dirname(__file__)))
      from masks import rMagenta, rRed, rGreen, rBlue, rOrange, rBlack
      from functions_jetson import *
      ```  

   - #### Introduction to running programs on the Jetson Orin Nano controller:-Jetson Orin Nano 控制器程式運作簡介：

      - ##### [jetson_Orin_Nano_final.py](./jetson_orin_nano_final.py)
      ### 中文:
        - jetson_Orin_Nano_final.py程序主要負責控制整個任務流程，包括避開牆壁、控制方向、躲避障礙物和圈數計數，以確保車輛按計劃完成所有任務。

        - 程序啟動時，車輛會先進行停車區出發模式。在此模式下，會先將車子開出來再進行壁障模式，避障系統將計算出柱子或是離邊牆範圍轉換為伺服馬達的角度，並利用該角度
        進行PD轉向控制，以確保車輛不會與牆壁發生碰撞。當車輛接近轉彎區域時，系統會偵測藍色或橘色線條，以判斷是否切換到轉彎模式。

        - 直線循跡模式：系統優先以紅色和綠色柱子(透過 detect_color_final() 計算出的中心偏差)作為主要校正依據；僅在未檢測到色塊時（cPillar.area == 0），才啟用兩側牆壁的面積差作為輔助校正參考。

        - 系統主要負責偵測賽道上的藍線或橘線，並以此觸發轉彎信號（設定 rTurn 或 lTurn 旗標）。轉彎一旦開始，舵角即被鎖定；而判斷轉彎是否完成並切換回直線循跡模式
        ### 英文:
        - The `jetson_Orin_Nano_final.py` program is primarily responsible for controlling the entire task flow, including avoiding walls, steering control, dodging block obstacles, and lap counting to ensure the vehicle completes all tasks as planned.

        - When the program starts, the vehicle is set to straight-driving mode by default. In this mode, the system converts the boundary range calculated by `process_roi()` into the angle for the servo motor and uses `pd_control()` to perform PD steering control to ensure the vehicle does not collide with the sidewall. As the vehicle approaches a turning area, the system uses `detect_color_final()` to detect blue or orange lines to determine whether to switch to turning mode.

        - **In straight-driving mode**, the system primarily uses the deviation of red and green blocks from the track curve, calculated by `detect_color_final()`, as a reference for correction, and uses the sidewall as a secondary correction reference when necessary.

        - **In turning mode**, the servo motor angle remains fixed. The system determines whether it has reached the next turning point based on changes in the gyroscope angle and elapsed time, allowing it to decide when to return to straight-driving mode and avoid repeated detection.

      __Program operation flow__ - 程式運行流程
        ### 中文:
        - jetson_Orin_Nano_final.py程式開始執行，初始化所有變量，並進入循環，持續從 find_contours 和 max_contour 函數中獲取數據，然後根據當前狀態進入不同的條件分支以執行相應的控制操作。在每個循環中，程式將jetson_Orin_Nano_final.py計算出的直流馬達值、伺服馬達角度和當前狀態打包成二進位數據，並透過WebSockets將其發送到 Raspberry Pi Pico W。
        ### 英文:
        - `jetson_nano_main_fianl.py` starts execution, initializes all variables, and enters a loop, continuously retrieving data from process_roi and detect_color, then entering different conditional branches based on the current state to perform the appropriate control actions. In each loop, `jetson_nano_main_final.py` packages the calculated DC motor value, servo motor angle, and current status into binary data and sends it to the Raspberry Pi Pico via UART. 

   - ##### Program Operation flowchart of the Jetson Orin Nano controller
     ![Obstacle_Challenge_Jetson_nano](./img/FE-obstacle_challenge_Jetson_nano.jpg)

 - ### Obstacle_Challenge Code Overview of Raspberry Pi Pico W-樹莓派 Pico W 障礙挑戰代碼概述
   - ####  Obstacle_Challenge Code Program Raspberry Pi Pico W Libraries-障礙挑戰程式碼程式 Raspberry Pi Pico W函式庫
    
      ```
      from machine import Pin, PWM, ADC, time_pulse_us
      import time, network, usocket as socket, ubinascii, uos, ujson as json
      ```  
     
   - #### Introduction to running programs on the Raspberry Pi Pico W controller:-樹莓派 Pico W 控制器程式運作簡介：
      ### 中文:
      - `pico_main_final.py` 程式運行在 Raspberry Pi Pico 控制器上，作為自動駕駛車輛的中間控制系統，管理直流馬達和伺服馬達的運作。該程式透過 WebSockets 從 Jetson Orin Nano 控制器接收計算結果，並控制後輪直流馬達的轉速、前輪伺服馬達的角度，同時監控車輛狀態參數。


      - 在控制後輪直流馬達時，我們使用 L293D 驅動晶片，透過 PWM 的佔空比調節電壓，實現後輪直流馬達的轉速控制。此外，透過設定 L293D 上的兩個控制引腳（20 和 21）的高低電平，可以控制後輪直流馬達的正反轉。

      - 在控制前輪伺服馬達時，我們直接利用PWM訊號的佔空比來調節輸出，從而控制伺服馬達的轉向角度， PWM訊號佔空比的變化對應伺服馬達的不同角度設置，實現精準轉向。

      - 當程式運作至count=1時，系統接管直流馬達的控制權，並開始轉彎撞牆猴退轉彎追蹤停車區域的洋紅色。在追蹤過程中，當如果洋紅色面積<100，然後使用牆壁循跡往前100度，在使用陀螺儀轉彎進入停車區，以確保精準停車。
      ### 英文:
      - ##### [pico_main_final.py](./pico_main_final.py)
        - The `pico_main_final.py` program runs on the Raspberry Pi Pico controller as an intermediary control system for an autonomous vehicle, managing the operation of the DC motor and servo motor. This program receives computation results from the Jetson Orin Nano controller via UART and controls the speed of the rear-wheel DC motor, the angle of the front-wheel servo motor, while also monitoring vehicle status parameters.
        -  When the start switch is pressed, the Raspberry Pi Pico controller receives a start signal and sends a high-level signal to initiate the main program `jetson_nano_main_final.py` on the Jetson Orin Nano.
        - When controlling the rear-wheel DC motor, we adjust the voltage through the duty cycle of PWM, using the L293D driver chip to achieve speed control of the rear-wheel DC motor. Additionally, by setting the high and low levels of the two control pins (20,21) on the L293D, we can control the forward and reverse rotation of the rear-wheel DC motor.
        - When controlling the front-wheel servo motor, we directly use the duty cycle of the PWM signal to adjust the output and control the steering angle of the servo motor, without the need for an L293D driver. Changes in the PWM signal’s duty cycle correspond to different angle settings for the servo motor, allowing for precise steering.
        - When the program reaches state five, the system takes over the control of the DC motor and begins tracking the pink sidewall of the parking area. During tracking, the ultrasonic distance sensor detects the parking area; when the sensor detects that the sidewall is pink, the system simultaneously takes control of both the servo motor and the DC motor. It then uses `run_encoder_Auto()` to adjust the forward angle of the DC motor to ensure precise parking.
      

      __Program operation flow__-程式運行流程
        ### 中文:
        - Jetson Orin Nano程式啟動後，樹莓派 Pico w 會進入等待狀態，直到Jetson Orin Nano按下按鈕後進入 jetson_Orin_Nano_final.py程式，並透過 WebSockets發送馬達數據給樹莓派 Pico w 運行。
        ### 英文:
        - When  `pico_main_final.py` starts, it sends a high-frequency signal to the Jetson Orin Nano to trigger the execution of the `jetson_nano_main_final.py` program. Then, `pico_main_final.py` enters a waiting mode until the button is pressed. After pressing the button,`pico_main_final.py` enters the main loop, starts receiving data transmitted via UART from the Jetson Orin Nano, and continues running. When it receives a status value of 5, the Pico takes over vehicle control and performs the parking operation.

    - ##### Program Operation flowchart of the Raspberry Pi Pico W controller-樹莓派 Pico W 控制器的程式操作流程圖
        ![FE-obstacle_challenge_Pico](./img/FE-obstacle_challenge_Pico.jpg)

       **set_servo_angle():** <br>
          - 計算並轉換±180度的角度值到伺服馬達所需的PWM佔空比範圍（0到65535），並將其輸出到前輪伺服馬達。

        __control_motor():__<br>
          - 取-100到100範圍內一個數的絕對值，轉換為PWM佔空比。同時，根據該值的符號設定兩個引腳的高低狀態，以控制馬達的正反轉或停止。

          __ws_send_text(sock, text):__<br>
          - Jetson Orin Nano 控制器透過 WebSockets 協定將更新後的值傳送到佇列，確保流程持續運行，以保持資料即時更新。


        __run_encoder_Auto():__<br>
          - 在此函數中run_encoder()，伺服馬達角度被設定為固定值，以車輛操作期間保持車輛位置和方向的穩定控制。
       </ol>
# <div align="center">![HOME](../../../other/img/home.png)[Return Home](../../../)</div>  
