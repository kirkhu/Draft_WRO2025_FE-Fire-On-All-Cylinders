<div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

 ## <div align="center"> Circuit Design -電路設計</div>
- 在我們的**自駕車**電路板設計過程中，我們選用了 **EasyEDA** 這款擁有**直覺式圖形介面**的專業電路設計軟體。藉由這項工具，我們**顯著提升**了焊接工作的**準確性**與接線的**精確度**，從而**有效地降低**了製造過程中的錯誤率，並將元件**燒毀的風險**控制在最低。

- 我們採取了**專業的印刷電路板 (PCB) 製作方式**（即「洗電路板」）。此舉不僅**大幅減少**了焊接錯誤和短路的**潛在風險**，更**優化了成品的外觀品質**。同時，這種製造方法提供了**更高的製程靈活性**與**操作上的便利性**。

- 該電路板的**核心功能**在於為**整合**的各類**感測器**、**馬達**以及**上下層控制器**提供穩定可靠的**電力供應**與**訊號傳輸介面**。這確保了所有關鍵電子元件之間能夠實現**順暢的通訊**與**高效的協同運作**，為**車輛控制程式**的運行奠定堅實基礎。

- In the design process of our **Self-Driving Car** circuit board, we utilized **EasyEDA**, a professional circuit design software featuring an **intuitive graphical interface**. Through this tool, we have **significantly enhanced** the **accuracy** of soldering and the **precision** of wiring, thereby **effectively reducing** the error rate during the manufacturing process, and minimizing the **risk of component burnout**.

- We adopted a **professional Printed Circuit Board (PCB) manufacturing method** (i.e., "PCB etching/fabrication"). This approach has not only **substantially mitigated** the **potential risks** of soldering errors and short circuits but has also **improved the aesthetic quality of the finished product**. Concurrently, this manufacturing technique offers **greater process flexibility** and **operational convenience**.

- The **core function** of this circuit board is to provide a stable and reliable **power supply** and **signal transmission interface** for the **integrated** various **sensors**, **motors**, and the **upper and lower layer controllers**. This ensures that all critical electronic components can achieve **smooth communication** and **efficient collaborative operation**, laying a solid foundation for the execution of the **Vehicle's control program**.


 - ### The Process of Identifying and Correcting Physical Circuit Board Design Issues - 實體電路板設計問題之發現與修正歷程
   - ### Circuit Design Optimization and Iteration - 電路設計最佳化與迭代
   本專案的電路設計歷經了數個版本的迭代，以追求最高的效能與可靠性：
   The circuit design for this project underwent several versions to achieve maximum performance and reliability:
<div>
<table>
   <tr>
      <th colspan=3 >Initial Phase and Fundamental Design Flaws V1.0 (Pegboard)</th>
   </tr>
   <tr>
      <td align=center  width="25%"><img src="../Circuit_Design/img/circuit_board_fount_1.png"  /></td>
      <td align=center  width="25%"><img src="../Circuit_Design/img/circuit_board_back_1.png"/></td>
   <td>

   __Description:__          

   - 本設計採用了 電木板（PCB 萬用板） 進行電路製作，然而，這種選擇使得電路設計與焊接過程變得極度耗時 。此外，線路佈局顯得雜亂，缺乏系統性的規劃與美觀性。這不僅嚴重影響了後續的除錯（Debugging） 與故障診斷（Fault Diagnosis） 效率，更存在虛焊（冷焊）、焊接不良及短路等重大的電路可靠性風險。
   - This design utilized a PCB pegboard (also known as a universal PCB) as the material for circuit construction. However, this choice resulted in an extremely time-consuming process for circuit design and soldering. Furthermore, the wiring layout appeared cluttered, lacking systematic planning and aesthetic quality. This not only severely hindered the efficiency of subsequent debugging and fault diagnosis, but also posed significant circuit reliability risks, including issues like cold solder joints, poor soldering, and short circuits.
               
   </td>
   </tr>
   <tr>
      <th colspan=3>Adopting Professional Fabrication and Discovering Parameter Errors V2.0 (PCB)</th>
   </tr>
   <tr>
      <td align=center width="25%" ><img src="../Circuit_Design/img/circuit_board_fount_2.png"  /></td>
       <td align=center  width="25%"><img src="../Circuit_Design/img/circuit_board_back_2.png"  /></td>
      <td>

   __Description:__
            
   - 為了解決舊版本電路板（V1.0）設計中存在的諸多問題，我們採用 EasyEDA 軟體 重新繪製電路，並生成了新的 印刷電路板（PCB）圖稿（V2.0）。隨後，我們將此設計送交工廠進行專業印刷製作。這次完整的流程讓我們成功掌握了業界標準的 PCB 設計與製造知識。

   - 當我們收到工廠製作完成的 V2.0 印刷電路板時，團隊感到非常興奮。然而，在著手安裝電子元件的過程中，我們發現元件無法順利組裝。經仔細檢查與確認，這是由於我們在 PCB 設計階段錯誤地設定了元件的針腳插座間距（Pin Header Pitch） 所造成的設計失誤。

   - In order to resolve the various issues present in the old circuit board design (V1.0), we utilized EasyEDA software to redraw the circuit and generate a new Printed Circuit Board (PCB) layout (V2.0). We then submitted this design for professional manufacturing at a factory. This comprehensive process allowed us to successfully acquire industry-standard knowledge of PCB design and fabrication.

   - The team was highly excited upon receiving the factory-produced V2.0 PCB. However, during the component installation phase, we discovered that the electronic components could not be properly assembled. After careful inspection and verification, we confirmed that this was a design error caused by incorrectly setting the component's pin header pitch during the PCB design stage.
            
   </td>
   </tr>
   <tr>
      <th colspan=3>Critical Polarity Error and Subsequent Rectification V3.0 (PCB)</th>
   </tr>
   <tr>
      <td align=center width="25%"><img src="../Circuit_Design/img/circuit_board_fount_3.png" /></td>
      <td align=center width="25%"><img src="../Circuit_Design/img/circuit_board_back_3.png"  /></td>
   <td>

   __Description:__
      
   - 鑑於上一版印刷電路板（V2.0）出現元件針腳間距錯誤的問題，我們立即利用 EasyEDA 軟體內建的標準範例圖作為參考，精確地重新校準了正確的針腳間距參數，並將修正後的設計（V3.0）送交工廠製作。

   - 然而，當我們收到製作完成的 V3.0 PCB 並進行功能測試時，卻發現整個電路的極性（Polarity）呈現反向。經過詳細的電路追溯與檢查，最終確認此問題是源於電路板設計階段的一次操作失誤：我們誤將原本應佈局於電路板背面的線路層（Bottom Layer）繪製到了正面（Top Layer）。

   - Given the incorrect component pin pitch issue found in the previous PCB version (V2.0), we immediately referenced the standard example diagrams built into the EasyEDA software to precisely recalibrate the correct pin pitch parameters. We then sent this revised design (V3.0) to the factory for production.

   - However, upon receiving the factory-produced V3.0 PCB and proceeding with the functional testing phase, we discovered that the polarity of the entire circuit was reversed. After detailed circuit tracing and inspection, we ultimately confirmed that this problem stemmed from an operational error during the circuit board design stage: we mistakenly drew the trace layer that should have been on the bottom layer of the PCB onto the top layer.

            
   </td>
   </tr>
   <tr>
       <th colspan=3>Critical Polarity Error and Subsequent Rectification V4.0 (PCB)</th>
   </tr>
    <tr>
      <td align=center  width="25%"><img src="../Circuit_Design/img/circuit_board_fount_4.png" width=400 /></td>
      <td align=center width="25%"><img src="../Circuit_Design/img/circuit_board_back_4.png" width=400 /></td>
   <td>

   __Description:__

   - 針對上一版印刷電路板（V3.0）電路極性顛倒的問題，我們對電路圖進行了徹底重新繪製，並經過多次嚴格確認設計無誤後，才將檔案送出製作，最終獲得了正確無誤的印刷電路板（V4.0）。

   - 隨後，由於我們將機器人主控制器升級為 Jetson Orin Nano，並決定改用紅外線感測器來偵測車輛是否靠近停車區牆面，因此需要在電路板上增設兩個 2-Pin 的母頭插座。同時，為了提供穩定且可插拔的電源連接點給 Jetson Orin Nano，我們也重新設計了接線端子。基於這些功能上的變動與升級，我們不得不重新設計電路，並送交工廠印刷製作新版電路板（V5.0）。

   - Addressing the issue of reversed circuit polarity in the previous PCB version (V3.0), we performed a complete redraw of the schematic. Only after multiple strict verifications to ensure the design was correct did we submit the file for production, resulting in the accurate Printed Circuit Board (V4.0).

   - Subsequently, due to upgrading the robot's main controller to a Jetson Orin Nano and deciding to switch to infrared sensors for detecting proximity to the parking area walls, it became necessary to add two 2-Pin female connectors to the circuit board. Simultaneously, we redesigned the terminal blocks to provide a stable, plug-and-play power connection point for the Jetson Orin Nano. Based on these functional changes and upgrades, we were compelled to redesign the circuit and submit the new board version (V5.0) to the factory for re-printing.

   </td>
   </tr>
   <tr>
      <th colspan=3>Functional Upgrades and Final Circuit Architecture V5.0 (PCB)</th>
   </tr>
   <tr>
      <td align=center width="25%" ><img src="../Circuit_Design/img/circuit_board_fount_5.png" /></td>
      <td align=center width="25%"><img src="../Circuit_Design/img/circuit_board_back_5.png"  /></td>
   <td>
      
   __Description:__

   - 在取得新版印刷電路板（V5.0）後，我們在測試過程中發現讀取 BNO055 陀螺儀感測器的角度時，偶爾會出現數值為 0 的異常情況。經排查確認，此問題是因 BNO055 感測器的電源正負極連接至 Raspberry Pi Pico W 提供的電源，而其訊號線卻接在 Jetson Orin Nano 主控制器上。這種電源與信號源不在同一迴路的配置導致了感測器誤動作。因此，我們修正設計，確保 BNO055 陀螺儀感測器的電源和訊號源皆由 Jetson Orin Nano 主控制器統一提供。

   - 此外，為符合競賽規則中必須由 Jetson Orin Nano 偵測啟動按鈕才能開始運行的規定，我們將啟動按鈕電路獨立連接至 Jetson Orin Nano 的通用輸入/輸出（GPIO）接口。同時，為了優化除錯流程，我們新增了 RGB 燈珠，用於即時顯示車輛偵測到的最近物件顏色。基於這些新增功能，我們設計並製作了第二塊電路板，專門用於自駕車的啟動按鈕控制與狀態顯示。

   - Upon receiving the new PCB (V5.0), functional testing revealed an intermittent issue where the BNO055 gyroscope sensor would return an angle reading of zero. Troubleshooting confirmed that this anomaly occurred because the BNO055 sensor was drawing power from the Raspberry Pi Pico W, while its signal lines were connected to the Jetson Orin Nano main controller. This configuration, where the power and signal sources were on different circuits, caused the sensor malfunction. Consequently, we modified the design to ensure that both the power and signal lines for the BNO055 gyroscope sensor are now supplied exclusively by the Jetson Orin Nano controller.

   - Separately, to comply with the rule requiring the Jetson Orin Nano to detect the start button press before operation, we dedicated a circuit to connect the start button directly to the Jetson Orin Nano's General-Purpose Input/Output (GPIO) interface. Furthermore, to enhance the debugging process, we added RGB LEDs to display the color of the nearest object detected by the vehicle in real-time. Based on these additions, we designed and manufactured a second circuit board dedicated to the self-driving car's start button control and status indication.

   </td>
   </tr>
     </table>  
  </div>
     <table>
   <tr>
       <th colspan=4>Final Version(PCB)</th>
   </tr>
   <tr>
      <td align=center width="25%"><img src="./img/Circuit_6_Top.png"  width="200"/></td>
      <td align=center width="25%"><img src="./img/Circuit_6_Bottom.png" width="200"/></td>   
      <td align=center width="25%"><img src="./img/Button_And_Led_Top.png"  width="200"/></td>
      <td align=center width="25%"><img src="./img/Button_And_Led_Bottom.png" width="200"/></td>
   </tr>
      </table>


 - ### Circuit Schematic Drawing 電路原理圖
 <div align=center>
   <table>
      <tr>
      <th colspan=3>主電路板（Main PCB）</th>
      </tr>
      <tr>
         <th>3D view</th>
         <th>circuit schematic</th>
         <th>PBC layout drawing</th>
      </tr>
      <tr>
         <td align=center ><img src="./img/New_3D_View.png" height=250 /></td>
         <td align=center ><img src="./img/New_Schematic.png" height=250 /></td>
         <td align=center ><img src="./img/New_PCB_Layouts.png" height=250 /></td>
      </tr>
      <tr>
      <th colspan=3>Switch Control Circuit Board (Secondary PCB) - 開關控制電路板</th>
      </tr>
      <tr>
         <th>3D view</th>
         <th>circuit schematic</th>
         <th>PBC layout drawing</th>
      </tr>
      <tr>
         <td align=center ><img src="./img/New_3D_View_Button_and_Led.png" height=250 /></td>
         <td align=center ><img src="./img/New_Schematic_LED_and_button.png" height=250 /></td>
         <td align=center ><img src="./img/New_PCB_Layouts_Button_and_Led.png" height=250 /></td>
      </tr>
   </table>
   <table>
   <th align=center>	Overall circuit schematic  </th>
   <tr>
   <td align=center ><img src="./img/Schematic&PCB/Schematic_Version_all.png" height=500  />
   </td>
   </tr>
   </table>
 
 </div>

 ***
 - ### Supplementary Information -補充資訊
 
 - #### 經驗分享-Adafruit BNO055 電路 

 #### 中文
   在自駕車電路設計的初始版本中，Adafruit BNO055 IMU感測器正極由Raspberry Pi Pico W提供，而資料傳輸是連接到Jetson Orin Nano。然而由於該設計未能形成完整電源迴路，導致系統缺乏統一電位基準，進而造成感測數據異常，尤其航向角輸出長時間固定於0°，無法反映實際姿態變化。
   
   為解決此問題，設計方案改以 Jetson Orin Nano 提供 BNO055 的正極電源，並將地線直接連接至 Orin 之 GND 腳位，以確保電源迴路閉合並建立穩定的電位基準。經過此調整後，感測器數據恢復正常，航向角能隨著車體旋轉而準確變化，滿足自駕車定位與導航控制之需求。

 - #### EasyEDA Introduction  -EasyEDA 簡介
 #### 中文:
   __EasyEDA__ 是一款免費的線上電子設計自動化（EDA）軟體，可用於設計與模擬電子電路，以及製作印刷電路板（PCB）。它提供簡單且使用者友善的圖形介面，具備多種功能，非常適合電子愛好者與專業工程師使用。
   - EasyEDA 可直接在網頁瀏覽器中使用，無需安裝軟體，因此具備跨平台的可用性。它支援電路設計、模擬、PCB 製作，並允許團隊共同協作進行電子專案。
   #### 英文:

   __EasyEDA__ is a free online Electronic Design Automation (EDA) software used for designing, simulating electronic circuits, and creating printed circuit boards (PCBs). It offers a simple and user-friendly graphical interface, with a variety of features that make it ideal for both hobbyists and professional engineers.
   - EasyEDA can be used directly in a web browser without the need for software installation, making it cross-platform accessible. It supports circuit design, simulation, PCB creation, and also allows teams to collaborate on electronic projects.


   - ### __EasyEDA的主要功能包括：__

   - ### The main features of EasyEDA include:

   
   #### 中文:
   
   - 電路圖設計： 使用其豐富的元件庫設計電路圖，該元件庫包含電阻器、电容器、電晶體、積體電路（IC）等多種元件。
   - PCB 設計： 支援多層 PCB 設計，並提供自動佈線功能，協助使用者高效率地完成電路板佈局。
   - 內建的 SPICE 模擬功能可讓使用者在製造前先行虛擬測試電路。
   - 元件庫： 提供大量的元件庫，並支援從其他 CAD 工具匯入元件，或自行建立自訂元件。
   - 協作工具： 使用者可以與團隊成員共享設計圖，以進行協同作業。
   - 雲端儲存： 設計檔案可儲存在雲端，方便隨時隨地存取與修改，也有助於與團隊成員之間的協作。
   - 製造整合： EasyEDA 與 JLCPCB 無縫整合，使用者可直接提交設計進行生產，輕鬆訂購客製化的 PCB。

   #### 英文:
   - Schematic Design: Design circuit diagrams using its extensive component library, which includes resistors, capacitors, transistors, integrated circuits (ICs), and more.Schematic Design: Design circuit diagrams using its extensive component library, which includes resistors, capacitors, transistors, integrated circuits (ICs), and more.
   - PCB Design: Supports multi-layer PCB design and provides an auto-routing feature to help users efficiently layout their boards.
   - Simulation: Built-in SPICE simulation allows users to virtually test circuits before manufacturing.
   - Component Library: Offers a vast component library and supports importing parts from other CAD tools or creating custom components.
   - Collaboration Tools: Allows users to share designs with teammates for collaborative work.
   - Cloud Storage: Design files can be saved in the cloud, making it easy to modify and access from anywhere, as well as facilitating collaboration with team members.
   - Manufacturing Integration: EasyEDA is seamlessly integrated with JLCPCB, allowing users to directly submit designs for production and easily order custom PCBs.
   ### Summarize -總結
   #### 中文:
   整體而言，EasyEDA 是一款功能強大且操作簡便的電子設計工具。無論是初學者還是專業工程師，它都能提供符合需求的各項功能。其雲端可存取性、簡單的操作介面，以及與製造商的整合，使其成為設計與製作電子電路的絕佳選擇。
#### 英文:
   __Overall, EasyEDA is a powerful and easy-to-use tool for electronic design. Whether you're a beginner or a professional engineer, it offers features to meet your needs. Its cloud-based accessibility, simple operation, and integration with manufacturers make it an excellent choice for designing and producing electronic circuits.__

   - Software link：[EasyEDA](https://easyeda.com/)
 <div align=center>
    <table>
    <tr>
    <th>EasyEDA of Official website.</th>
    <th>Schematic Design</th>
    </tr><tr>
    <td><img src="./img/EasyEDA.png" width="500"alt="EasyEDA of Official website. "></td>
    <td><img src="./img/EasyEDA1.png" width="500" alt="Schematic Design"></td>
    </tr>
    </table>
    </div>

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div>  
