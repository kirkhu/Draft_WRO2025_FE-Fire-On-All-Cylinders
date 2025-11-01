<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center"> Automatically record the LAB values of the field-自動保存記錄場地的 LAB 值</div>
為了記錄交通標誌積木、停車區邊牆及場地線的顏色，我們撰寫了一個程式，能自動將最終的 LAB 值保存在 Jetson Orin Nano 控制器中。此功能省去手動記錄的麻煩，不僅節省時間，也確保了數據的準確性。

- #### Image processing-影像處理
    ### 中文:
    - 在影像處理時，使用 Color_LAB.py 檔案將交通標誌方塊與場地底圖上的線條轉換到不同的色彩空間是必須的步驟，以有效處理特定任務。
    - 我們使用 cv2.cvtColor 函數將原始的 RGB 影像轉換成 LAB（明度、紅綠軸、黃藍軸）色彩空間。
    - 轉換完成後，透過 cv2.inRange 函數並設定六個 LAB 閾值：L_low、L_high、A_low、A_high、B_low、B_high 來定義顏色範圍。cv2.inRange 函數會將 LAB 影像中每個像素與設定的範圍做比較，若像素值落在範圍內則保留，否則過濾掉。此過程可得到濾波後的影像。
    - 取得濾波後影像後，我們將對應數值儲存進 masks.py 檔案中進行儲存。
    - 在主程式中我們透過下方代碼呼叫masks檔案中的各物件數值，輸入給相對應的函數進行 LAB 視覺辨識。
        ```python
        from masks import rMagenta, rRed, rGreen, rBlue, rOrange, rBlack
        ```

<div align="center">

**Red traffic sign block-紅色交通標誌方塊**

|Adjusting the LAB Range Values for Red Color(調整紅色的 LAB 範圍值)|Save the LAB range values for Red(儲存紅色的 LAB )|Live image of the Red traffic sign block(紅色交通標誌方塊的即時影像)|
|:----:|:----:|:----:|
|<img src="./img/Red/Adjusting_the_LAB_Range_Values_for_Red_Color.png" alt="Adjusting_the_LAB_Range_Values_for_Red_Color" align=center />|<img src="./img/Red/Save_the_LAB_range_values_for_red.png"  alt="Save_the_LAB_range_values_for_red" align=center />|<img src="./img/Red/Live_image_ of_the_red_traffic_sign_block.png" alt="Live_image_ of_the_red_traffic_sign_block" align=center />|



**Green traffic sign block-綠色交通標誌方塊**


|Adjusting the LAB Range Values for GreenColor(調整綠色的 LAB 範圍值)|Save the LAB range values for Green(儲存綠色的 LAB )|Live image of the Green traffic sign block(綠色交通標誌方塊的即時影像)|
|:----:|:----:|:----:|
|<img src="./img/Green/Adjusting_the_LAB_Range_Values_for_green_Color.png" alt="Adjusting_the_LAB_Range_Values_for_green_Color" align=center />|<img src="./img/Green/Save_the_LAB_range_values_for_green.png"  alt="Save_the_LAB_range_values_for_green" align=center />|<img src="./img/Green/Live_image_ of_the_green_traffic_sign_block.png" alt="Live_image_ of_the_green_traffic_sign_block" align=center />|



**Blue line-藍色線條**


|Adjusting the LAB Range Values for Blue Color(調整藍色的 LAB 範圍值)|Save the LAB range values for Blue(儲存藍色的 LAB )|Live image of the Blue line（藍色線條的即時影像）|
|:----:|:----:|:----:|
|<img src="./img/Blueline/Adjusting_the_LAB_Range_Values_for_blueline_Color.png" alt="Adjusting_the_LAB_Range_Values_for_blueline_Color" align=center />|<img src="./img/Blueline/Save_the_LAB_range_values_for_blueline.png"  alt="Save_the_LAB_range_values_for_blueline" align=center />|<img src="./img/Blueline/Live_image_ of_the_blueline.png" alt="Live_image_ of_the_blueline" align=center />|



**Orange line-橘色線條**


|Adjusting the LAB Range Values for Orange Color(調整橘色的 LAB 範圍值)|Save the LAB range values for Orange(儲存橘色的 LAB)|Live image of the Orange line(橘色線條的即時影像) |
|:----:|:----:|:----:|
|<img src="./img/Orangeline/Adjusting_the_LAB_Range_Values_for_Orangeline_Color.png" alt="Adjusting_the_LAB_Range_Values_for_Orange line_Color" align=center />|<img src="./img/Orangeline/Save_the_LAB_range_values_for_Orangeline.png"  alt="Save_the_LAB_range_values_for_Orange linee" align=center />|<img src="./img/Orangeline/Live_image_ of_the_Orangeline_block.png" alt="Live_image_ of_the_Orange_line" align=center />|



**magenta sidewall-洋紅色測牆**


|Adjusting the LAB Range Values for magenta Color(調整洋紅色的 LAB 範圍值)|Save the LAB range values for Pink(儲存洋紅色的 LAB )|Live image of the Pink sidewall(洋紅色邊牆的即時影像)|
|:----:|:----:|:----:|
|<img src="./img//magenta/Adjusting_the_LAB_Range_Values_for_magenta_Color.png" alt="Adjusting_the_LAB_Range_Values_for_magenta_Color" align=center />|<img src="./img/magenta/Save_the_LAB_range_values_for_magenta.png"  alt="Save_the_LAB_range_values_for_pink" align=center />|<img src="./img/magenta/Live_image_ of_the_magenta_traffic_sign_block.png" alt="Live_image_ of_the_magenta_traffic_sign_block" align=center />|

</div>


# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
