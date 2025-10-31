<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">Distinctive Pseudo Code-獨特的偽代碼獨特的偽代碼</div>
### 邊緣偵測在車輛轉向控制的應用
我們使用邊緣檢測技術引導車輛駛向交通號誌路口，並沿著檢測出的邊緣線進行精確定位。透過對影像進行邊緣偵測，可以明確辨識出道路邊界與行駛區域，進而生成車輛行進的導引路徑。此方法能即時反映環境變化，確保車輛平穩且準確地駛向路口，同時也能輔助進行路口定位與避障操作。


```
 def draw_roi_boxes(img, rois, color=(255, 204, 0), thickness=2):
    for i, R in enumerate(rois, 1):
        if R is None or len(R) != 4:
            continue
        x1, y1, x2, y2 = R
        if x1 == x2 == y1 == y2 == 0:
            continue
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
        cv2.putText(img, f"ROI{i}", (int(x1) + 4, int(y1) + 18),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

def draw_contours_list(img, contours, roi, color, label=None, thickness=2, show_bbox=True):
    if contours is None or len(contours) == 0 or roi is None or len(roi) != 4:
        return
    ox, oy = int(roi[0]), int(roi[1])
    for c in contours:
        c2 = c + np.array([[[ox, oy]]])
        cv2.drawContours(img, [c2], -1, color, thickness)
        if show_bbox:
            x, y, w, h = cv2.boundingRect(c2)
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
    if label:
        cv2.putText(img, label, (ox + 4, oy + 16), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

```
<div align="center" ><img src="../../src/Steering_Control/img/Detecting_nearby_obstacles.png" width="400" alt="Recognize the color of traffic signal blocks"></div>


# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
