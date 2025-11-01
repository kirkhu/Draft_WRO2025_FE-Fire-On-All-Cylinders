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
  |<div align="center"> <img src="./img/Counterclockwise_direction.png" width="400"  alt="Detecting_nearby_obstacles"></div>|<div align="center"> <img src="./img/clockwise_direction.png" width="400" alt="Detecting_nearby_obstacles"></div>|

</div> 

- ## 判斷顏色行駛路線
    ### 中文:
    - 若為逆時針方向，偵測到綠色柱子則行駛於內側，偵測到紅色柱子則行駛於外側；若未偵測到柱子，則預設行駛外側。
    - 若為順時針方向，偵測到綠色柱子則行駛於外側，偵測到紅色柱子則行駛於內側；若未偵測到顏色，則同樣行駛外側。
- program code:
    ```
        color = 0
        detect_start = time.time()
        TIMEOUT = 2.0
        while a == 1:
            ok, img = cap.read()
            if not ok:
                continue
            img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
            img_lab = cv2.GaussianBlur(img_lab, (3,3), 0)

            contours_left  = pOverlap(img_lab, ROI1, True)
            contours_right = pOverlap(img_lab, ROI2, True)
            leftArea  = max_contour(contours_left,  ROI1)[0]
            rightArea = max_contour(contours_right, ROI2)[0]

            contours_red   = find_contours(img_lab, rRed,   ROI3)
            contours_green = find_contours(img_lab, rGreen, ROI3)
            best_red,   _ = find_best_pillar(contours_red,   redTarget,   "red",   img_lab)
            best_green, _ = find_best_pillar(contours_green, greenTarget, "green", img_lab)
            candidates = [p for p in (best_red, best_green) if p is not None]
            cPillar = min(candidates, key=lambda P: P.dist) if candidates else Pillar(0, 1000000, 0, 0, 0)
            seen_green_wait = (cPillar.target == greenTarget and cPillar.area > 0)
            seen_red_wait   = (cPillar.target == redTarget   and cPillar.area > 0)

            # === RGB：看到綠亮綠；看到紅亮紅；其他關燈（等待階段）===
            if seen_green_wait:
                rgb.show("green")
            elif seen_red_wait:
                rgb.show("red")
            else:
                rgb.off()

            if start_turn == 2:
                if seen_green_wait: color = 1; print("green"); a = 2
                elif seen_red_wait: color = 2; print("red"); a = 2
                elif time.time() - detect_start > TIMEOUT: color = 3; a = 2
            else:
                if seen_green_wait: color = 4; print("green"); a = 2
                elif seen_red_wait: color = 5; print("red"); a = 2
                elif time.time() - detect_start > TIMEOUT: color = 6; a = 2

        print(color)
        write(color)
        time2 = time.time()
    ```
    

    <div align=center>
        <table>
          <tr>
            <th>Counterclockwise_green</th>
            <th>Counterclockwise_red</th>
            <th>Counterclockwise_NO</th>
          </tr>
          <tr>
            <td align=center><img src="./img/Counterclockwise_green.png" width=400 /></td>
            <td align=center><img src="./img/Counterclockwise_red.png" width=400 /></td>
            <td align=center><img src="./img/Counterclockwise_NO.png" width=400 /></td>
          </tr>
        </table>
      </div>
    <div align=center>
    <div align=center>
        <table>
          <tr>
            <th>Counterclockwise_green</th>
            <th>Counterclockwise_red</th>
            <th>Counterclockwise_NO</th>
          </tr>
          <tr>
            <td align=center><img src="./img/Clockwise_green.png" width=400 /></td>
            <td align=center><img src="./img/Clockwise_red.png" width=400 /></td>
            <td align=center><img src="./img/Clockwise_NO.png" width=400 /></td>
          </tr>
        </table>
      </div>
    <div align=center>


 

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  


