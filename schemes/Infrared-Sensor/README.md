<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Introduction to TCRT5000 Infrared Line Tracking Sensor</div>

- ### __Introduction to TCRT5000 Infrared Line Tracking Sensor__

<div align=center width=100%>
    <table>
        <tr>
            <td align=left width=500>
            TCRT5000是一款常見的反射型紅外線感測器( Infrared Reflective Sensor )，內部由紅外線發射二極體( IR LED )與光電晶體( Phototransistor )組成。它的工作原理是透過紅外線發射端發出不可見光，當光線遇到前方物體表面時，會反射回感測器的接收器。若接收端偵測到反射光，即可判斷前方是否有物體存在。
            </td>
            <td align=center width=500>
            <p><strong>Supports 3.3V operating voltage</strong></p>
            <img src="./img/TCRT5000 front.png" width=300 />
            <img src="./img/TCRT5000 back.png" width=300 />
            </td>
        </tr>
    </table>
</div>

<div align=center width=100%>
    <table>
        <tr align=center>
            <th colspan=2>TCRT5000 Infrared Sensor Placement Diagram on Vehicle</th>
        </tr>
        <tr align=center>
            <th>Front</th>
            <th>Rear</th>
        </tr>
        <tr>
            <td align=center><img src="./img/Car Front TCRT5000.png" width=500 /></td>
            <td align=center><img src="./img/Car Back TCRT5000.png" width=500 /></td>
        </tr>
    </table>
</div>

- ### TCRT5000 連接到 Raspberry Pi Pico W 的接線步驟：
    - TCRT5000 的 GND 腳位連接到 Raspberry Pi Pico W 的接地腳位。
    - TCRT5000 的 A0 腳位連接到 Raspberry Pi Pico W 的 GPIO 腳位：
        - 腳位26(前方)
        - 腳位27(後方)，用於輸出紅外反射量的電壓訊號。
    - 以下是 MicroPython 撰寫的程式碼，以類別形式呈現，能透過 Raspberry Pi Pico W 讀取 TCRT5000 紅外線循線感測器的紅外反射量電壓訊號。

- ### MicroPython 程式碼：
    ```python
    class TCRT5000:
        def __init__(self, adc_pin):
            try:
                self.adc = ADC(Pin(adc_pin))
            except:
                self.adc = None

        def read_raw(self):
            try:
                return self.adc.read_u16()
            except:
                return -1

        def read_percentage(self):
            try:
                raw = self.read_raw()
                if raw == -1:
                    return -1
                percentage = (raw / 65535) * 100
                return round(percentage, 1)
            except:
                return -1
    ```

- ### 範例使用方法：
    ```python
    if __name__ == "__main__":
        sensor = TCRT5000(adc_pin=26)
        while True:
            raw_val = sensor.read_raw()
            percent = sensor.read_percentage()
            print("Raw ADC:", raw_val, " 反射強度百分比:", percent, "%")
            time.sleep(0.2)
    ```

- ### 說明：
    此程式碼包含一個名為 TCRT5000 的類別，透過定義模擬輸出（A0）腳位來測量紅外線反射強度。read_raw() 方法會回傳原始 ADC 數值，read_percentage() 方法會回傳反射強度的百分比（0~100%），可用於判斷黑線或白線。若讀取過程發生錯誤，則可回傳 -1。

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div> 