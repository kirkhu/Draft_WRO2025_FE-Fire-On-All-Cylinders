<div align=center> <img src="../../other/img/logo.png" width=300 alt=" logo"> </div>

## <div align="center">Software Platform Construction </div> 
- ### __Installing System Software Required for Self-Driving Cars__

   - ### System Platform Software Installation Process Diagram-系統安裝流程圖

   <div align=center>
   <img src="./img/Orin_System_Installation.jpg" width="100%" />
   </div>

   - ### Installing the Operating System on Nvidia Jetson Orin Nano

      - #### Preparation Before Installation - 操作前的準備
         - 請配置或備妥一台運行 Ubuntu 作業系統的實體主機。 嚴禁使用任何虛擬化環境 (如虛擬機) 來執行相關任務。
         - 務必確認您的 Jetson Orin Nano 已妥善安裝固態硬碟 (SSD)。
         - Please prepare or configure a physical host machine running the Ubuntu operating system. The use of any virtualization environment (such as a virtual machine) for executing the relevant tasks is strictly prohibited.
         - Please ensure that a Solid-State Drive (SSD) is properly installed on your Jetson Orin Nano.

      - #### NVIDIA SDK Manager Installation

         - Download [NVIDIA SDK Manager 2.3.0](https://developer.nvidia.com/sdk-manager)

          <div align=center><img src="./img/NVIDIA SDK Manager Download Page.png" width="80%"></div>

         - Double-click the installation package to install, and upon completion and successful login, launching the application will display the following screen雙擊安裝包開始安裝，安裝完成後，登入並開啟（應用程式），即可看到以下畫面 
          <div align=center><img src="./img/Start SDK Manager Page.png" width="80%"></div>

   
      - #### JetPack Software Version Installation, Upgrade, and Downgrade Guide

         - SDK Manager 是 NVIDIA 的官方工具，可為 Jetson 主機執行 JetPack 版本的安裝、升級與降級。操作前請先將 Nvidia Jetson Orin Nano 切換至 Recovery Mode 並依指示接通電源與連線。以下為 SDK Manager 的操作流程。
         - SDK Manager is an official tool from NVIDIA that allows you to install, upgrade, or downgrade JetPack versions on Jetson devices. Before proceeding, please switch the Nvidia Jetson Orin Nano to Recovery Mode and follow the instructions to connect the power and establish a connection. Below is the operation procedure for SDK Manager.
         
         <div align=center><img src="./img/20250930_212433.jpg" width="80%" /></div>

      <div align=center>
         <table>
         <tr>
         <th>Connect the Nvidia Jetson Orin Nano to the host computer.</th>
         <th>Verify whether the connection is successful.</th>
         <th>Select the developer kit.</th>
         </tr>
         <tr>
         <td><img src="./img/11.jpg" width=400 /></td>
         <td><img src="./img/12.png" width=400 /></td>
         <td><img src="./img/13.png" width=400 /></td>
         </tr>
         <tr>
         <th>Select the desired JetPack version from the menu.</th>
         <th>Check the option on the left side and click Next.</th>
         <th>Enter the administrator password.</th>
         </tr>
         <tr>
         <td><img src="./img/14.png" width=400 /></td>
         <td><img src="./img/15.png" width=400 /></td>
         <td><img src="./img/16.png" width=400></td>
         </tr>
         <tr>
         <th>Enter the relevant information of the motherboard.</th>
         <th>After the installation is complete, click "Finish" to exit.</th>
         <th>Successful login screen of Jetson Orin Nano</th>
         </tr>
         <tr>
         <td><img src="./img/17.png" width=400 /></td>
         <td><img src="./img/18.png" width=400 /></td>
         <td><img src="./img/19.png" width=400 /></td>
         </tr>
         </table>
      </div>

   - ### System environment initial setup Steps

 - Update the operating environment.
    ```bash
    sudo apt update
    sudo apt upgrade -y

    ```

 - **python**版本升級
    ```bash
    # 安裝所需的支援庫
    sudo apt install update
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
      libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
      libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev nano

    # 安装 pyenv
    curl https://pyenv.run | bash

    # 临时设置环境（仅当前会话有效）
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

    # 安装 Python
    pyenv install 3.11.7
    pyenv global 3.11.7

    # 永久设置环境
    echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

    # 重新加载配置
    source ~/.bashrc

    ```

 - 安裝**BNO055**所需的驅動程序
    ```bash
    sudo apt update
    sudo apt install i2c-tools -y
    sudo i2cdetect -y -r 7 # 這行指令應改會在輸出中看到28這個位址
    python -m pip install --upgrade --user \
      adafruit-circuitpython-bno055 \
      circuitpython-bno055 \
      Jetson.GPIO \
      smbus2

    ```

 - 安裝 **WebSockets** 12.x 的最新版本
    ```bash
    pip install "websockets>=12<13"
    ```

 - 安裝ASUS AC1200驅動程式 或 安裝TP Link AC1300驅動程式
    ```bash
    mkdir -p ~/src && cd ~/src/
    git clone https://github.com/morrownr/88x2bu-20210702.git
    cd ~/src/88x2bu-20210702/
    sudo ./install-driver.sh

    ```

    ```bash
    sudo apt install dkms git -y && \
    sudo git clone https://github.com/RinCat/RTL88x2BU-Linux-Driver.git /usr/src/rtl88x2bu-git && \
    sudo sed -i 's/PACKAGE_VERSION="@PKGVER@"/PACKAGE_VERSION="git"/' /usr/src/rtl88x2bu-git/dkms.conf && \
    sudo dkms add -m rtl88x2bu -v git && \
    sudo dkms install -m rtl88x2bu -v git

    ```

 - 安裝支援CUDA加速的opencv
    ```bash
    sudo apt install -y cmake
    # 下載 OpenCV 主程式碼
    cd ~
    git clone https://github.com/opencv/opencv.git
    cd opencv
    git checkout 4.7.0   # 可以選擇穩定版本

    # 下載 opencv_contrib 模組
    cd ~
    git clone https://github.com/opencv/opencv_contrib.git
    cd opencv_contrib
    git checkout 4.7.0   # 對應 OpenCV 版本

    # 安裝所需依賴庫
    sudo apt update
    sudo apt install -y libgtk-3-dev pkg-config build-essential cmake git \
        libatlas-base-dev libjpeg-dev libpng-dev libtiff-dev \
        libavcodec-dev libavformat-dev libswscale-dev \
        libv4l-dev v4l-utils libxvidcore-dev libx264-dev \
        libtbb2 libtbb-dev libdc1394-22-dev

    # 建立並清理Build資料夾
    mkdir -p ~/opencv/build
    cd ~/opencv/build
    rm -rf *

    # 設定python路徑
    PYTHON_EXEC=$(pyenv which python3)
    PYTHON_PREFIX=$(pyenv prefix)
    PYTHON_INCLUDE=$PYTHON_PREFIX/include/python3.11
    PYTHON_LIB=$PYTHON_PREFIX/lib/libpython3.11.so
    PYTHON_PACKAGES=$PYTHON_PREFIX/lib/python3.11/site-packages

    # 進行CMake設定
    cmake \
      -D CMAKE_BUILD_TYPE=Release \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
      -D WITH_GSTREAMER=ON \
      -D WITH_CUDA=ON \
      -D ENABLE_FAST_MATH=ON \
      -D CUDA_FAST_MATH=ON \
      -D WITH_CUBLAS=ON \
      -D WITH_GTK=ON \
      -D BUILD_opencv_python3=ON \
      -D PYTHON3_EXECUTABLE=$PYTHON_EXEC \
      -D PYTHON3_INCLUDE_DIR=$PYTHON_INCLUDE \
      -D PYTHON3_LIBRARY=$PYTHON_LIB \
      -D PYTHON3_PACKAGES_PATH=$PYTHON_PACKAGES \
      -D BUILD_opencv_world=OFF \
      -D BUILD_EXAMPLES=OFF \
      -D BUILD_TESTS=OFF \
      -D BUILD_DOCS=OFF \
      -D BUILD_PERF_TESTS=OFF \
      ..

    # 編譯opencv
    make -j$(nproc)

    # 安裝opencv
    sudo make install

    # 驗證是否安裝成功
    python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
    python3 -c "import cv2; print(cv2.getBuildInformation())" | grep -E "GStreamer|GTK|CUDA"

    ```

 - **AP**自啟動設定
    ```bash
    curl -fsSL -u "if0_39931049:microhack188" -o "Set_AP.sh" "ftp://ftpupload.net/htdocs/UserData/WRO2025-Orin/Set_Orin_AP_AutoStart.sh" # 獲取配置腳本

    sudo bash ./Set_AP.sh # 執行腳本進行配置及啟用動作
    ```

 - **程序自啟動**設置
    ```bash
    curl -fsSL -u "if0_39931049:microhack188" -o "Set_Auto_Run.sh" "ftp://ftpupload.net/htdocs/UserData/WRO2025-Orin/set_auto_start_code.sh"

    sudo bash ./Set_Auto_Run.sh
    ```

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div> 