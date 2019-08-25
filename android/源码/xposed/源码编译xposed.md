`目录：`
- [源码编译xposed](#b780d7853749cc4834e213997efde8f1)
  - [编译android源码](#50b51e10a59c1e52ced2f2717c473f0d)
  - [编译XposedBridge](#33acd2ce7824a83c6fe59a7e6002f326)
  - [使用xposed tools](#1d4be69ccc727d2a32730d5ed88c1473)
      - [下载XposedTools](#56d68943d22e86f57c0bf90f623cea11)
      - [配置build.conf文件](#2bad87b60d1edf183aea491b858e1813)
      - [替换xposed和art文件](#4da943807bd4f9777f5df23808e84760)
      - [编译](#38e956ced3d258de195759cc9f7bf527)
      - [将xposed框架集成到Android系统](#bca7bc9d14192ede7d83b70ff5ac4a1a)
        - [替换文件](#22e7f61591e1c09d90b2002daea6bd3f)
        - [移动文件 ](#a32c80003f81147090a7742a0959cde7)
        - [重新生成镜像文件](#d3660ac4a7388b1a3285401ae292974b)
---
# <span id="b780d7853749cc4834e213997efde8f1"/>源码编译xposed


## <span id="50b51e10a59c1e52ced2f2717c473f0d"/>编译android源码


编译android 7.1.1， sdk 25；XposedBridge下载版本是v89，其他的是v88

## <span id="33acd2ce7824a83c6fe59a7e6002f326"/>编译XposedBridge


下载XposedBridge的源代码
[XposedBridge](https://github.com/rovo89/XposedBridge)，选择tag v89的，编译

也可以下载编译好的 v89 [XposedBridge.jar](./XposedBridge.jar)
，jar不依赖平台

存放在/out/target/product/xxx/system/framework/下。

## <span id="1d4be69ccc727d2a32730d5ed88c1473"/>使用xposed tools


#### <span id="56d68943d22e86f57c0bf90f623cea11"/>下载XposedTools

[XposedTools](https://github.com/rovo89/XposedTools)

#### <span id="2bad87b60d1edf183aea491b858e1813"/>配置build.conf文件


build.conf文件是一个配置文件，会被build.pl读取使用。build文件中主要定义了编译xposed的结果的存放路径，android源码的路径，还有一些版本信息之类的值。
将下载的zip包解压，在文件夹下创建build.conf文件。然后编辑build.conf文件。

build.conf文件包含：
```
outdir指向的路径是xposed编译之后生成的文件的存放路径。
version的值和后边的参数是自己设置的。编译之后会写入到xposed.prop文件中。
makeflags是设置在后边编译过程中使用的线程数。
AospDir指向的路径是android源码存放的路径，前边的值是源码对应的SDK的版本号。这里我指向的是android5.1.1的源码，对应的android sdk的版本是22。
```

#### <span id="4da943807bd4f9777f5df23808e84760"/>替换xposed和art文件


从github上克隆xposed两个仓库到本地。分别是
[xposed](https://github.com/rovo89/Xposed/tree/v88) 和
[art](https://github.com/rovo89/android_art/tree/v88-sdk25)
。点击下载zip包，解压压缩包得到xposed文件夹和art文件夹。

xposed文件夹包括xposed修改之后的app_process等应用程序和libxposed_*.so等库文件的源码；
art文件夹主要包括xposed修改之后的art虚拟机的文件

android_art文件夹替换源码目录下的art文件夹

xposed文件夹移动到 源码目录/frameworks/base/cmds/中

如果虚拟机需要root，xposed中部分代码需要修改，参考
[模拟器root](../模拟器root.md)

#### <span id="38e956ced3d258de195759cc9f7bf527"/>编译


在build.conf文件中outdir目录下创建一个java文件夹，然后将XposedBridge.jar包放到java文件夹下

使用build.pl编译xposed源码

编译 arm表示平台，22位版本

./build.pl -t arm:22

在执行过程中，可能会提示缺少一些依赖包，例如可能会缺少Config::IniFiles，
使用apt-cache search Config::IniFiles搜索，安装缺少的包即可。

编译完成后，生成文件：
包括lib文件夹下的五个so库和bin文件加下的四个可执行程序以及一个配置文件。

#### <span id="bca7bc9d14192ede7d83b70ff5ac4a1a"/>将xposed框架集成到Android系统


##### <span id="22e7f61591e1c09d90b2002daea6bd3f"/>替换文件

用第四部分中生成的bin文件夹和lib文件夹下的文件替换xxx/out/target/product/hammerhead/system/文件夹下的bin文件和lib文件里的相同的文件。
需要注意的是用xposed编译生成的app_process32_xposed替换system/bin文件夹下的app_process32,
名字还是app_process32

##### <span id="a32c80003f81147090a7742a0959cde7"/>移动文件 

将xposed.prop文件移动到system文件夹下

##### <span id="d3660ac4a7388b1a3285401ae292974b"/>重新生成镜像文件


```
source ./build/envsetup.sh
lunch 版本
make snod
```







