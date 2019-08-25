`目录：`
  - [使用XposedInstaller管理xposed模块
](#4f2da9472bb5f7c8e7ba6b3cee20e857)
    - [xposed模块开发
](#5e284b556a5594cd88802a3735924763)
      - [依赖
](#0284bd150ab81d3213b15c6958881a79)
      - [模块编写
](#067339a455b62cf2891178b94906b769)
      - [声明类的入口
](#4f2e2740523c74877e7b431f4d02e5ae)
---
## <span id="4f2da9472bb5f7c8e7ba6b3cee20e857"/>使用XposedInstaller管理xposed模块


### <span id="5e284b556a5594cd88802a3735924763"/>xposed模块开发


#### <span id="0284bd150ab81d3213b15c6958881a79"/>依赖


[api](https://jcenter.bintray.com/de/robv/android/xposed/api/) 下载

v88版本依赖的 [jar](./api-82.jar), [source](./api-82-sources.jar) 。

#### <span id="067339a455b62cf2891178b94906b769"/>模块编写


创建Xposed项目后，需要还在AndroidMenafest.xml文件里面声明Xposed模块，在application里面添加三个meta-data标签（xposedmodule，xposeddescription，xposedminversion）。

xposedmodule：表示作为Xposed的一个模块    
xposeddescription：表示对本模块的描述，该描述会显示在安装好后的程序名称下方  
xposedminversion：表示的jar包的最低版本号

```
<meta-data
    android:name="xposedmodule"
    android:value="true"/>
<meta-data
    android:name="xposeddescription"
    android:value="Xposed Demo"/>
<meta-data
    android:name="xposedminversion"
    android:value="80"/>
```

```
public class Test implements IXposedHookLoadPackage {
    @Override
    public void handleLoadPackage(XC_LoadPackage.LoadPackageParam lpparam) throws Throwable {
        //拦截方法
    }

```

#### <span id="4f2e2740523c74877e7b431f4d02e5ae"/>声明类的入口


创建完我们钩类之后，我们需要将该类加载到XposedInstaller中，也就是我们必须声明该类的位置，需要在xposed_init中声明。 

先创建assets文件

然后在assets文件里，新建一个文件名为“xposed_init”

然后在 xposed_init 内写入刚创建的入口类的完整类名，这里是 xxx.xxx.Test

