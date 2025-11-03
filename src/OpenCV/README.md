 <div align="center"><img src="../../other/img/logo.png" width="300" alt=" logo"></div>

## <div align="center">OpenCV Introduction－OpenCV介紹</div> 

### 中文:
- OpenCV（開源電腦視覺庫）是一個用於電腦視覺和機器學習的開源軟體庫。它包含 2,500 多種最佳化演算法，涵蓋影像處理、物件偵測、影像辨識、人臉辨識、運動追蹤和 3D 重建等各種視覺任務。 OpenCV 由於其多功能性和高效性，被廣泛應用於自動駕駛、機器人、醫學影像處理和安全監控等不同領域。
- OpenCV 支援多種程式語言（例如 C++、Python 和 Java），並且可以在各種作業系統上運行，包括 Windows、Linux、macOS 和 Android。它不僅可以在 CPU 上運行，還支援 GPU 和嵌入式設備的硬體加速，使其適用於 Nvidia Jetson Orin Nano 和 Raspberry Pi 等資源有限的設備，並能有效運作。
- 因此，可以透過OpenCV辨識技術，辨識賽道上的紅色/綠色柱體、黑色邊界牆、洋紅色停車區，乃至於地面上的藍線與橙線，進而控制車輛行進方向。

### 英文:


- ### Steps to install the OpenCV application on the Nvidia Jetson Orin Nano:
   
   __1.Update and Upgrade Packages:__
   ```bash
      sudo apt-get update
      sudo apt-get upgrade
   ```
   __2.Installing OpenCV with CUDA support 安裝支援CUDA加速的opencv套件__
   ```bash
      sudo apt install -y cmake
   ```

   __3.Download the OpenCV Main Source Code - 取得 OpenCV 主程式碼 (Main Repository)__
      
   ```bash
      cd ~
      git clone https://github.com/opencv/opencv.git
      cd opencv
      git checkout 4.7.0  
   ``` 

   __4.Download the Opencv_contrib Module__
  ```bash
      cd ~
      git clone https://github.com/opencv/opencv_contrib.git
      cd opencv_contrib
      git checkout 4.7.0 
  ```
  __5.Installing Dependencies - 安裝所需依賴庫__
  
   ```bash
      sudo apt update
      sudo apt install -y libgtk-3-dev pkg-config build-essential cmake git \
         libatlas-base-dev libjpeg-dev libpng-dev libtiff-dev \
         libavcodec-dev libavformat-dev libswscale-dev \
         libv4l-dev v4l-utils libxvidcore-dev libx264-dev \
         libtbb2 libtbb-dev libdc1394-22-dev
  ```
  __6.Create and Clean the Build Folder - 建立並清理Build資料夾__
  ```bash
      mkdir -p ~/opencv/build
      cd ~/opencv/build
      rm -rf *
  ```
  __7.Configure the Python Path - 設定python路徑__
  ```bash
      PYTHON_EXEC=$(pyenv which python3)
      PYTHON_PREFIX=$(pyenv prefix)
      PYTHON_INCLUDE=$PYTHON_PREFIX/include/python3.11
      PYTHON_LIB=$PYTHON_PREFIX/lib/libpython3.11.so
      PYTHON_PACKAGES=$PYTHON_PREFIX/lib/python3.11/site-packages
  ```
  __8.Configure the CMake__
  ```bash
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
         ...
  ```
  __9.Build OpenCV - 編譯opencv__

  ``` bash 
            make -j$(nproc)
  ```
  __10.Installing Opencv__
  ```bash 
            sudo make install
  ```
  __11.Confirm successful installation 驗證是否安裝成功__
  ```bash
      python3 -c "import cv2; print('OpenCV version:', cv2.__version__)"
      python3 -c "import cv2; print(cv2.getBuildInformation())" | grep -E "GStreamer|GTK|CUDA"

  ```   


- __Reference links:__
- __參考連結：__
  <ol>
  <li><a href="https://qengineering.eu/install-opencv-on-jetson-nano.html" target="_blank">Q-engineering</a></li>
  <li><a href="https://docs.arducam.com/Nvidia-Jetson-Camera/Native-Camera/Quick-Start-Guide/?fbclid=IwZXh0bgNhZW0CMTEAAR3rpGy1GsiVuHBFvi6qkJIelI8P88syOjCk1rvKRaBONlKQOsQ7BPMmfVI_aem_jJuQ5IOzOy0no-wMudOhlQ" target="_blank">ArduCam</a></li>
  <li><a href="https://zh.wikipedia.org/wiki/OpenCV" target="_blank">Wikipedia</a></li>
  <li><a href="https://steam.oxxostudio.tw/category/python/ai/opencv.html#google_vignette" target="_blank">steam educational website</a></li>
  </ol>

# <div align="center">![HOME](../../other/img/home.png)[Return Home](../../)</div> 
