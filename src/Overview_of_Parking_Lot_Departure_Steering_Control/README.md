<div align=center> <img src="../../other/img/logo.png" width=300 alt=" logo"> </div>

## <div align="center">Overview of Parking Lot Departure Steering Control-停車場出發轉向控制概述</div> 

- ### 判斷行車方向
    ### 中文:
- 我們首先判斷車輛的行駛方向是順時針還是逆時針：若出發區右側牆壁距離大於左側，則判定為逆時針方向，反之則為順時針。接著，車輛會朝柱子進行顏色辨識。
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
  <div align="center"> <img src="./img/Counterclockwise_direction.png"  alt="Detecting_nearby_obstacles"></div>|<div align="center"> <img src="./img/clockwise_direction.png"  alt="Obstacle_XY_coordinates"></div>|
  </div> 
- 若為逆時針方向：偵測到綠色柱子則行駛於內側，偵測到紅色柱子則行駛於外側；若未偵測到柱子，則預設行駛外側。
- 相反地，若為順時針方向：偵測到綠色柱子則行駛於外側，偵測到紅色柱子則行駛於內側；若未偵測到顏色，則同樣行駛外側。
<div align=center>

 

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  


