<div align=center> <img src="../../other/img/logo.png" width=300 alt=" logo"> </div>

## <div align="center">Overview of Parking Lot Departure Steering Control-停車場出發轉向控制概述</div> 

- ## 判斷行車方向
  ### 中文:
    - 我們首先判斷車輛的行駛方向是順時針還是逆時針，如果ROI2面積大於ROI1面積判斷是逆時針，ROI1面積大於ROI2面積是順時針。接著，車輛會朝柱子進行顏色辨識。
- program code:

```
        a = 0
        start_turn = 0
        while a == 0:
            rightArea = leftArea = areaFront = tArea = 0
            ok, img = cap.read()
            if not ok:
                continue
            img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
            img_lab = cv2.GaussianBlur(img_lab, (3,3), 0)

            contours_left  = pOverlap(img_lab, ROI1)
            contours_right = pOverlap(img_lab, ROI2)
            leftArea  = max_contour(contours_left,  ROI1)[0]
            rightArea = max_contour(contours_right, ROI2)[0]

            if leftArea - rightArea > 0:
                print("右轉"); start_turn = 1; a = 1
            else:
                print("左轉"); start_turn = 2; a = 1

        write(start_turn)     
```
<div align=center>

  |Counterclockwise_direction|The color and X, target coordinates of traffic signal blocks.|
  |:---:|:---:|
  |<div align="center"> <img src="./img/Counterclockwise_direction.png"  alt="Detecting_nearby_obstacles"></div>|<div align="center"> <img src="./img/clockwise_direction.png"  alt="Detecting_nearby_obstacles"></div>|

</div> 

- ## 判斷顏色行駛路線
    ### 中文:
    - 若為逆時針方向，偵測到綠色柱子則行駛於內側，偵測到紅色柱子則行駛於外側；若未偵測到柱子，則預設行駛外側。
    - 若為順時針方向，偵測到綠色柱子則行駛於外側，偵測到紅色柱子則行駛於內側；若未偵測到顏色，則同樣行駛外側。
    - program code:
    ```
        mode = 1
        LAST_COLOR = 0
        color = 0
        print(mode, color)
        print('等待 color（M,<1..6>[,<...>] 或 JSON {"color":n}）...')

        while mode == 1 and color == 0:
            json_obj, m_tuple, got_stop = pump_ws(s)

            if json_obj:
                v = None
                try:
                        if "color" in json_obj:
                            v = int(json_obj["color"])
                        elif "c" in json_obj:
                            v = int(json_obj["c"])
                    except:
                        v = None
                    if v is not None:
                        if 1 <= v <= 6:
                            color = v
                            LAST_COLOR = color
                            print("[JSON] color =", color)
                            break
                        else:
                            if DEBUG: print("[IGNORE] JSON color out of range:", v)
                    extract_magenta_from_json(json_obj)

                if m_tuple:
                    first = m_tuple[0]
                    if 1 <= first <= 6:
                        color = first
                        LAST_COLOR = color
                        print("[M] color =", color, "raw:", m_tuple)
                        break
                    else:
                        if DEBUG: print("[IGNORE] M packet in mode1 (not color):", m_tuple)

                if json_obj is None and m_tuple is None:
                    time.sleep(0.002)

            # --- 顏色對應動作（略，以你原本流程為準） ---
            if color == 1:
                print("顏色=1")
                run_encoder_Auto(2100, 60, 0)
                run_encoder_Auto(1400, 40, 180)
                run_encoder_Auto(1200, -45, 0)
            elif color == 2:
                print("顏色=2")
                run_encoder_Auto(1700, 60, 0)
                run_encoder_Auto(1150, -40, -180)
            elif color == 3:
                print("顏色=3")
                run_encoder_Auto(1700, 60, 0)
                run_encoder_Auto(1150, -40, -180)
            elif color == 4:
                print("顏色=4")
                run_encoder_Auto(600, 40, 180)
                run_encoder_Auto(400, 50, 0)
                run_encoder_Auto(1100, 40, -180)
                run_encoder_Auto(800, 50, 0)
            elif color == 5:
                print("顏色=5")
                run_encoder_Auto(600, 40, 180)
                run_encoder_Auto(2200, 60, 0)
                run_encoder_Auto(1150, 40, -180)
                run_encoder_Auto(800, 50, 0)
            elif color == 6:
                print("顏色=6")
                run_encoder_Auto(600, 40, 180)
                run_encoder_Auto(1500, 60, 0)
                run_encoder_Auto(1150, 40, -180)

            control_motor(0)
            set_servo_angle(0)
    ```
    

    <div align=center>
        <table>
          <tr>
            <th>Front Assembly</th>
            <th>Steering Knuckle</th>
            <th>Bearing Holder</th>
          </tr>
          <tr>
            <td align=center><img src="./img/Counterclockwise_green.png" width=400 /></td>
            <td align=center><img src="./img/Counterclockwise_red.png" width=400 /></td>
            <td align=center><img src="./img/Counterclockwise_NO.png" width=400 /></td>
          </tr>
        </table>
      </div>
<div align=center>

 

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  


