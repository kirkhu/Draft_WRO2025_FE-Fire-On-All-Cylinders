<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Ultrasonic rangefinder Introduction-超聲波測距儀簡介</div> 

- ### __Instruction to HC-SR04 ultrasonic distance sensor-HC-SR04 超聲波距離感測器說明__
    <div align="center">
    <table>
    <tr>  
    <td>
    <ol>

    ### 中文:
    * **關於 HC-SR04 超聲波距離感測器的功能性描述**
    HC-SR04 超聲波距離感測器 是一種高成本效益且易於整合的距離測量解決方案。其原理是透過發射超聲波脈衝，並精確測量聲波來回的飛行時間（Time-of-Flight, TOF）來判斷與物體之間的距離。該感測器的有效量測範圍為 2公分到400公分，並可達到 3毫米 的高精度。這使得它能夠提供高度準確且可靠的距離數據，非常適用於避障、自主導航以及車輛周遭的物體偵測等多種應用情境。
    
    * **HC-SR04 在自駕車任務中的應用**
    HC-SR04 超聲波距離感測器在我們的自駕車任務中扮演了關鍵角色，尤其是在執行 停車操作 時。它被用於即時偵測車輛與側牆或障礙物之間的距離，從而極大地提升了停車的便利性與精確度。透過程式設計，我們可以根據感測器回傳的精確距離數據進行閉環控制，順利引導車輛以適當的角度和速度進入指定的停車區，這對於任務的成功完成具有實質性的助益。
    
    ### 英文:
    ### Functional Description of the HC-SR04 Ultrasonic Distance Sensor

    The **HC-SR04 Ultrasonic Distance Sensor** is a **cost-effective and easily integrated** solution for distance measurement. Its operation relies on **emitting an ultrasonic pulse** and precisely measuring the **Time-of-Flight (TOF)** of the sound wave to determine the distance to an object. The sensor provides an effective measurement range from 2cm up to 400 with a high accuracy of 3mm. This capability ensures **highly accurate and reliable** distance data, making it well-suited for various applications such as **obstacle avoidance, autonomous navigation,** and perimeter **object detection**.

    ### Application of the HC-SR04 in the Autonomous Vehicle Mission

    The HC-SR04 ultrasonic distance sensor plays a **critical role** in our autonomous vehicle mission, particularly during the **parking operation**. It is utilized for the **real-time detection of the distance between the vehicle and the side wall or obstacles**, which significantly enhances the ease and precision of parking. By programming **closed-loop control** based on the **precise distance data** returned by the sensor, we can smoothly guide the vehicle at the appropriate angle and velocity into the designated **parking lot**, providing **substantial assistance** toward the successful completion of this mission task.
        
    </ol>
    </td>
    <td width=300 align="center"><p>
    <strong>Supports 3.3V operating voltage-支援3.3伏特操作電壓</strong>
    </p>
        <img src="./img/HC-SR04.png" alt="HC-SR04" width="250" />
        <img src="./img/HC-SR04back.png" alt="HC-SR04" width="250" />
    </td>
    </tr>
    </table>
    </div>
   <ol>

    ### 中文:

    ### 雙側測距與數據處理

    1.  為了精確掌握車輛周遭環境，我們在車輛的**左側及右側**均安裝了 **HC-SR04 超聲波距離感測器**，並將其連接至 **Raspberry Pi Pico W** 下位控制器。這些感測器的核心任務是**即時偵測車輛與側牆之間的距離**。

    ### 關鍵的電壓相容性與保護

    1.  然而，在系統整合時必須**嚴格遵守電壓規範**：**Raspberry Pi Pico W 控制器** 的 GPIO 腳位僅能安全讀取**最高 $3.3 \text{V}$ 的訊號電壓**。
    2.  鑑於市售的 **HC-SR04 超聲波距離感測器** 通常會輸出高達 **$5 \text{V}$ 的訊號電壓**，因此在選用或使用此感測器時，我們**必須採取電壓匹配措施**。
    3.  此舉是為了**避免因電壓不符導致的訊號讀取錯誤、操作異常，甚至控制器硬體永久損壞**。

    ### Dual-Sided Ranging and Data Processing

    1.  To ensure precise situational awareness, we installed **HC-SR04 ultrasonic distance sensors** on both the **left side and the right side** of the vehicle, connecting them to the **Raspberry Pi Pico W** sub-controller. The primary role of these sensors is the **real-time detection of the distance between the vehicle and the side walls**.


    ### Critical Voltage Compatibility and Protection

    1.  However, **strict adherence to voltage specifications is required** during system integration: the GPIO pins on the **Raspberry Pi Pico W controller** can safely read a **maximum signal voltage of 3.3V**.
    2.  Given that commercially available **HC-SR04 ultrasonic distance sensors** typically output a signal voltage of up to **5V**, we **must implement voltage matching solutions** when selecting and utilizing this sensor.
    3.  This measure is **essential to prevent signal reading errors, operational issues, or even permanent damage to the controller hardware** that could result from voltage mismatch.

   
    ### 英文:
    1. We installed HC-SR04 ultrasonic distance sensors on the left, right, and rear of the vehicle and connected them to the Raspberry Pi Pico controller to detect the distance between the vehicle and the side walls. The measured distance data is transmitted to the main program for processing, serving as a basis for parking maneuvers.
   2. It is worth noting that the maximum signal voltage read by the Raspberry Pi Pico controller is 3.3V, while commercially available HC-SR04 ultrasonic distance sensors typically output a maximum signal voltage of 5V. Therefore, when selecting or using the sensor, special attention should be paid to its operating voltage to avoid operational issues or potential damage to the controller due to voltage mismatch.
    </ol>
<br>
    <div align="center" width=100%>
    <table >
    <tr align="center">
    <th colspan="2">HC-SR04 Ultrasonic Distance Sensor Placement Diagram on Vehicle-HC-SR04 超聲波距離感測器在車輛上的安裝位置示意圖

</th>
    </tr>
    <tr align="center">
      <th>Left</th>
      <th>Right</th>
      </tr>
    <tr>
      <td align=center><img src="../../v-photos/img/left.png" alt="HC-SR04_left" width="50%" /></td>
      <td align=center><img src="../../v-photos/img/right.png" alt="HC-SR04_right" width="50%" /></td>
      </tr>
    </table>
    </div>

- #### HC-SR04 連接至 Raspberry Pi Pico W的接線步驟：  
    - HC-SR04 的 VCC 連接到 Raspberry Pi Pico W的 3.3V（腳位 36）：為超聲波感測器提供電源。
    - HC-SR04 的 GND 連接到 Raspberry Pi Pico W的接地腳位：確保兩者共用接地。
    - HC-SR04 的 Trig 腳位連接到 Raspberry Pi Pico W的 GPIO 腳位：
        - 腳位 12（左側），
        - 腳位 13（右側），用於發送超聲波脈衝信號。
    - HC-SR04 的 Echo 腳位連接到 Raspberry Pi Pico W的 GPIO 腳位：
        - 腳位 8（左側），
        - 腳位 9（右側），用於接收回聲信號。
    - 以下是使用 MicroPython 撰寫的程式碼，以類別形式實現，能透過 Raspberry Pi Pico W讀取 HC-SR04 超聲波感測器的偵測距離。

- #### Wiring steps for connecting the HC-SR04 to the Raspberry Pi Pico:

    - VCC (HC-SR04) connects to the 3.3V (pin 36) on the Raspberry Pi Pico W: Provides power to the ultrasonic sensor.
    - GND (HC-SR04) connects to the GND pin on the Raspberry Pi Pico W: Ensures a common ground between both devices.
    - Trig (HC-SR04) connects to the GPIO pins on the Raspberry Pi Pico W:
         - pin 12 (left),
        - pin 13 (right), used for sending ultrasonic pulse signals.
    - Echo (HC-SR04) connects to the GPIO pins on the Raspberry Pi Pico W:
        - pin 8 (left),
        - pin 9 (right), used for receiving the echo signal.

    - Below is the code written in MicroPython, implemented as a class to read the detection distance from the HC-SR04 ultrasonic sensor using the Raspberry Pi Pico W.

   - #### MicroPython code-MicroPython 程式碼 
   ```
            from machine import Pin, time_pulse_us
            import time
            class HCSR04:
                def __init__(self, trigger_pin, echo_pin, echo_timeout_us=30000):
                    self.trigger = Pin(trigger_pin, Pin.OUT)
                    self.echo = Pin(echo_pin, Pin.IN)
                    self.echo_timeout_us = echo_timeout_us
                    self.trigger.low()
                    time.sleep(0.05)  # Stabilize the sensor

                def distance_cm(self):
                    # Send a 10us pulse to trigger the measurement
                    self.trigger.high()
                    time.sleep_us(10)
                    self.trigger.low()

                    # Wait for the echo response and measure its duration
                    try:
                        pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
                    except OSError as ex:
                        pulse_time = -1

                    # Calculate distance in cm (pulse time in microseconds)
                    if pulse_time > 0:
                        distance = (pulse_time / 2) / 29.1  # Speed of sound ~343 m/s
                    else:
                        distance = -1  # Return -1 if timeout or error

                    return distance
   ```
   - #### Example usage-範例使用方法  
   ```
            sensor = HCSR04(trigger_pin=3, echo_pin=2)  # Assign pins accordingly
            while True:
                distance = sensor.distance_cm()
                if distance == -1:
                    print("Out of range or error")
                else:
                    print("Distance: {:.2f} cm".format(distance))
                time.sleep(1)
   ```
   - #### Explanation-說明  
        此程式碼包含一個名為 HC-SR04 的類別，透過定義觸發（trigger）和回聲（echo）腳位來測量距離。distance_cm() 方法會回傳以公分為單位的距離值，若發生測量錯誤或距離超出範圍，則會回傳 -1。


        This code includes a class named <strong>HC-SR04</strong> that measures distance by defining trigger and echo pins. The distance_cm() method returns the distance in centimeters, and if a measurement error occurs or the distance is out of range, it returns -1.


# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
