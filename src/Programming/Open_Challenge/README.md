<div align=center> <img src="../../../other/img/logo.png" width = 300 alt=" logo"> </div>

## <div align="center">Open Challenge Code Overview</div> 
  Based on the characteristics of each control board, we distributed the complex operations required for the race vehicle:
  ### 中文:
   1. Jetson Orin Nano 負責影像辨識和方向偵測，利用其強大的運算能力進行即時影像分析。
   2. 同時，樹莓派 Pico W 負責馬達驅動和車輛轉向，利用其高效的  GPIO 控制功能進行精確的硬體管理。
   3. 這種分工最大限度地發揮了每個控制板的優勢，使整個系統更加穩定有效率。
   ### 英文:
   <ol>
   <li>
    The Jetson Nano is responsible for image recognition and direction detection, leveraging its powerful computing 
   capability to process real-time image analysis.    
   </li>
   <li>
    Meanwhile , the Raspberry Pi Pico handles motor driving, and vehicle steering, utilizing its efficient GPIO control features for precise hardware management.
   </li>
   <li>
    This division of labor maximizes the advantages of each control board, making the overall system more stable and efficient.
   </li>
   </ol>

 - ### Jetson Nano library
    The functions for image recognition, front-wheel servo motor proportional steering control, and ground line color recognition have been integrated into the [function.py](../common/function.py) module and can be directly imported for use.
    The functions of these modules are as follows:
    - `process_roi()`: Processes image data to recognize objects or features within a scene.
      ```
      def find_contours(img_lab, lab_range, ROI):
        x1, y1, x2, y2 = ROI
        seg = img_lab[y1:y2, x1:x2]
        lo = np.array(lab_range[0]); hi = np.array(lab_range[1])
        mask = cv2.inRange(seg, lo, hi)
        k = np.ones((5,5), np.uint8)
        mask = cv2.erode(mask, k, iterations=1)
        mask = cv2.dilate(mask, k, iterations=1)
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        return contours

      def max_contour(contours, ROI):
          maxArea = 0; maxY = 0; maxX = 0; mCnt = 0
          for cnt in contours:
              area = cv2.contourArea(cnt)
              if area > 150:
                  approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
                  x,y,w,h = cv2.boundingRect(approx)
                  x += ROI[0] + w//2
                  y += ROI[1] + h
                  if area > maxArea:
                      maxArea = area; maxY = y; maxX = x; mCnt = cnt
          return [maxArea, maxX, maxY, mCnt]

      def pOverlap(img_lab, ROI, add=False):
          x1, y1, x2, y2 = ROI
          seg = img_lab[y1:y2, x1:x2]
          from masks import rBlack, rMagenta
          loB, hiB = np.array(rBlack[0]),   np.array(rBlack[1])
          loM, hiM = np.array(rMagenta[0]), np.array(rMagenta[1])
          mB = cv2.inRange(seg, loB, hiB)
          mM = cv2.inRange(seg, loM, hiM)
          if add:
              mask = cv2.add(mB, mM)
          else:
              mask = cv2.bitwise_and(mB, cv2.bitwise_not(mM))
          k_open  = np.ones((3,3), np.uint8)
          k_close = np.ones((7,7), np.uint8)
          mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,  k_open,  iterations=1)
          mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k_close, iterations=1)
          contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
          return contours

      ```             

    - `pd_control()`: Controls the steering of the servo motor based on calculated ratios to ensure precise and stable steering.
      ```
      def pd_control(target, current, kp, kd):
          global current_last  # Use a global variable
          error = current - target
          derivative = current - current_last
          control_signal = -(kp * error + kd * derivative)
          current_last = current  # Update current_last before returning
          return control_signal
      ```

    - `detect_color()`: Detects the color of lines on the ground, used for applications such as path or lane tracking.
      ```
      def detect_color(undistorted_frame):
          hsv_frame = cv2.cvtColor(undistorted_frame, cv2.COLOR_BGR2HSV)
          color_y_positions = []
          for color, (lower, upper, bgr) in color_ranges.items():
              lower = np.array(lower, dtype=np.uint8)
              upper = np.array(upper, dtype=np.uint8)
              color_mask = cv2.inRange(hsv_frame, lower, upper)
              contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
              if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                if cv2.contourArea(largest_contour) > 500:  # Filter out small noise areas
                    x, y, w, h = cv2.boundingRect(largest_contour)
                    center_y = y + h // 2
                    cv2.rectangle(undistorted_frame, (x, y), (x + w, y + h), bgr, 2)
                    cv2.circle(undistorted_frame, (x + w // 2, center_y), 5, bgr, -1)  # Mark center point
                    color_y_positions.append(center_y)
                else:
                    color_y_positions.append(0)  # If no valid contour is found, return 0
              else:
                    color_y_positions.append(0)  # If no contours are found, return 0
          return color_y_positions
      ```

 - ### Open Challenge Code Overview of Jetson nano
   - #### Open Challenge Code Program Jetson nano Libraries
    
      ```
      import cv2
      import numpy as np
      import serial as AC
      import struct
      import Adafruit_BNO055.BNO055 as BNO055 
      # Program module for loading the BNO055 gyroscope orientation sensor
      
      import time
      from function import process_roi, detect_color, pd_control
      # Load custom program modules for image recognition, front-wheel servo
        motor steering ratio control, and ground line color recognition.

      import Jetson.GPIO as GPIO 
      # Enable GPIO pin control on the Jetson Nano.
      ```  

   - #### Introduction to running programs on the Jetson nano controller:

      - ##### [jetson_nano_main.py](./jetson_nano_main.py)
        - The  `jetson_nano_main.py` program is primarily responsible for controlling the overall task flow, including wall avoidance, steering control, and lap counting.

        - When the program starts, the vehicle defaults to a straight-line mode. In this mode, the boundary range calculated by `process_roi()` is converted into an angle for the servo motor, and PD steering control is executed via `pd_control()` to ensure the vehicle does not hit the sidewall. When the vehicle approaches a turn, `detect_color()` detects blue or orange lines to determine whether to enter turning mode.

        - In turning mode, the servo motor angle remains fixed, and the vehicle uses the gyroscope angle and elapsed time to determine if it has reached the next turning point, thereby deciding when to return to straight-line mode to avoid repeated detections.

      __Program operation flow__
        - `jetson_nano_main.py` starts execution, initializes all variables, and enters a loop, continuously retrieving data from process_roi and detect_color, then entering different conditional branches based on the current state to perform the appropriate control actions. In each loop, `jetson_nano_main.py` packages the calculated DC motor value, servo motor angle, and current status into binary data and sends it to the Raspberry Pi Pico via UART. 

   - ##### Program Operation flowchart of the Jetson Nano controller
     ![flowchart_open](./img/open_challange_Jetson_nano.jpg)

 - ### Open Challenge Code Overview of Raspberry Pi Pico
   - ####  Open Challenge Code Program Raspberry Pi Pico Libraries
    
      ```
      from machine import Pin, PWM, I2C, UART  
      # In MicroPython, you can import relevant modules to enable 
        GPIO pin control, Pulse Width Modulation (PWM), I2C, and 
        UART communication protocols on the Raspberry Pi Pico.

      import struct
      import time
      ```  
     
   - #### Introduction to running programs on the Raspberry Pi Pico controller:

      - ##### [pico_main.py](./pico_main.py)
        - The `pico_main.py` program runs on the Raspberry Pi Pico controller as an intermediary control system for an autonomous vehicle, managing the operation of the DC motor and servo motor. This program receives computation results from the Jetson Nano controller via UART and controls the speed of the rear-wheel DC motor, the angle of the front-wheel servo motor, while also monitoring vehicle status parameters.
        -  When the start switch is pressed, the Raspberry Pi Pico controller receives a start signal and sends a high-level signal to initiate the main program `jetson_nano_main.py` on the Jetson Nano.
        - When controlling the rear-wheel DC motor, we adjust the voltage through the duty cycle of PWM, using the L293D driver chip to achieve speed control of the rear-wheel DC motor. Additionally, by setting the high and low levels of the two control pins (20,21) on the L293D, we can control the forward and reverse rotation of the rear-wheel DC motor.
        - When controlling the front-wheel servo motor, we directly use the duty cycle of the PWM signal to adjust the output and control the steering angle of the servo motor, without the need for an L293D driver. Changes in the PWM signal’s duty cycle correspond to different angle settings for the servo motor, allowing for precise steering.
      
      __Program operation flow__
        - `pico_main.py` starts running, it sends a high-frequency signal to the Jetson Nano to initiate the `jetson_nano_main.py` program. Then, `pico_main.py` enters a waiting state until a button is pressed. Once pressed, `pico_main.py` enters the main loop, beginning to receive data sent by the Jetson Nano via UART, and continues running until it receives a value with a status of 5.

      - ##### Program Operation flowchart of the Raspberry Pi Pico controller
        ![flowchart_open](./img/open_challange_Pico.jpg)
        
          __set_servo_angle():__<br>
           Calculate and convert the angle value from ±180 degrees to the PWM duty cycle range required by the servo motor (0 to 65535) and output it to the front-wheel servo motor.
        
          __control_motor():__<br>
            Take the absolute value of a number in the range of -100 to 100 and convert it to the PWM duty cycle. Meanwhile, set the high and low states of two pins based on the sign of the value to control forward and reverse rotation or to stop.。

          __jetson_all():__<br>
            The Jetson Nano controller sends updated values to the queue via the UART protocol, ensuring that this process runs continuously to keep the data updated in real-time. 

          __run_encoder():__<br>
            By reading the current value of the DC motor to calculate its rotation angle, conditions are set based on the calculation results to control the motor to move straight to the specified rotation angle. This design allows for precise motor adjustments, ensuring that the vehicle moves steadily during operation and accurately reaches the intended target angle.

 

# <div align="center">![HOME](../../../other/img/home.png)[Return Home](../../../)</div>  
