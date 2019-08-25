`目录：`
- [Android 源码下载和编译
](#a7f621d032c443ca7dc12d9fa05e1cca)
  - [安装ubuntu16.04和配置环境
](#5478a3bf91f19f340926449e6c2981ae)
      - [安装git
](#d56611e1926d0047627a057994bb2c8c)
      - [安装java
](#7e1959bddb269d27771cff01bd0b3bc1)
      - [安装依赖库
](#7c23c0eaf52a46e713786ac74adcb854)
      - [下载配置 repo
](#c3d98f95942e5d7c717421c834a8f37e)
      - [下载源码
](#ad93d4bfdedecfb2c0cb0aa2168a76d9)
      - [编译
](#fe11cbd7713c56f6b98172c0beaadb3c)
      - [运行
](#3c6d3883a5143fbbb4b3a365dafa12dc)
---
# <span id="a7f621d032c443ca7dc12d9fa05e1cca"/>Android 源码下载和编译


## <span id="5478a3bf91f19f340926449e6c2981ae"/>安装ubuntu16.04和配置环境


#### <span id="d56611e1926d0047627a057994bb2c8c"/>安装git


sudo apt-get install git
 
git config –global user.email"xxx@xxx.com" 
  
git config –global user.name "xxx"

#### <span id="7e1959bddb269d27771cff01bd0b3bc1"/>安装java


sudo add-apt-repository ppa:openjdk-r/ppa

sudo apt-get update

sudo apt-get install openjdk-8-jdk

添加~/bin 到环境变量PATH里面

#### <span id="7c23c0eaf52a46e713786ac74adcb854"/>安装依赖库


```
sudo apt-get install libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-dev g++-multilib
sudo apt-get install -y git flex bison gperf build-essential libncurses5-dev:i386
sudo apt-get install tofrodos python-markdown libxml2-utils xsltproc zlib1g-dev:i386
sudo apt-get install dpkg-dev libsdl1.2-dev libesd0-dev
sudo apt-get install git-core gnupg flex bison gperf build-essential
sudo apt-get install zip curl zlib1g-dev gcc-multilib g++-multilib
sudo apt-get install libc6-dev-i386
sudo apt-get install lib32ncurses5-dev x11proto-core-dev libx11-dev
sudo apt-get install libgl1-mesa-dev libxml2-utils xsltproc unzip m4
sudo apt-get install lib32z-dev ccache
sudo apt-get install libssl-dev
890702/article/details/86380477
```

#### <span id="c3d98f95942e5d7c717421c834a8f37e"/>下载配置 repo


可以将源码放在bin目录下，也可以选择自己的目录，最好挂载另一个大硬盘来编译，一般源码及编译需要最少一百G

curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo

chmod a+x ~/bin/repo

修改repo脚本的镜像地址为国内的镜像源 REPO_URL =
'https://gerrit-google.tuna.tsinghua.edu.cn/git-repo'

#### <span id="ad93d4bfdedecfb2c0cb0aa2168a76d9"/>下载源码


源码版本查看 [http://source.android.com/source/build-numbers.html]()

repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b android-9.0.0_r3

8线程并发下载

repo sync -j8

#### <span id="fe11cbd7713c56f6b98172c0beaadb3c"/>编译


```
//加入临时环境变量
source build/envsetup.sh
//选择 aosp_x86_64-eng debug版本
lunch 6 

make update-api -j8
//8线程编译，第一次编译比较慢，根据主机配置选择线程数
make -j8
```

#### <span id="3c6d3883a5143fbbb4b3a365dafa12dc"/>运行


emulator 

运行编译好的模拟器





    