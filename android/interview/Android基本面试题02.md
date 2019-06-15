`目录：`
  - [面试题](#d11195cba9985a6572a41c4acf6edb33)
      - [Handler的原理](#73b6e7a611664773efc2cff20922ba56)
      - [Binder机制原理](#db559f8440a393fee53b6a0082a3bd14)
      - [热修复的原理 ](#7f65781ae13f5334571854ab2116c0ff)
      - [Android内存泄露及管理](#1e33e319686773adf5dca98d451aa0a5)
        - [内存泄露原因：](#15d8c4186cfecadd297f2ab5c5aae17b)
      - [Fragment与Fragment、Activity通信的方式](#cc117d22db29bd51815f3a0401c29baf)
      - [Android UI适配](#b1fa8e7b610f82bba2cd2a19872f8632)
      - [app优化 ](#c2dcd19aa7cae42ad9108feab8268b96)
        - [优化：](#5e0ada5fd61cc852bc17fa1c593670ed)
      - [图片优化](#1de33821a53101e8d846e85f3618bbba)
      - [HybridApp WebView和JS交互](#8af4b5f76bece869eb465977ff337426)
      - [JAVA GC原理](#4f8816565e8a4d8fff9eff5d0d939d3d)
      - [ ANR ](#b8319749b4c2c0221d0f117dbe06de6e)
      - [设计模式 ](#8f4832ec71ecc5b67c07889892f2a8e8)
      - [RxJava ](#b5035777bfa3df19db181b25289a3166)
      - [MVP，MVC，MVVM ](#73ee0ad6f84149f63602b6fdc704b573)
      - [手写算法（选择冒泡必须要会） ](#2f7b9656a68b01a5d2639f5d45c212d4)
      - [JNI ](#ddba29c1b4e2160f23b2dda35c5c987f)
      - [RecyclerView和ListView的区别](#b6b433b5cacc1e9fbfb14a3eddef1760)
      - [Universal-ImageLoader，Picasso，Fresco，Glide对比 ](#95ea4efe05cf8de8addaaed9b5269b98)
      - [Xutils, OKhttp, Volley, Retrofit对比](#ace088d91e5621d12cf218459ed4d309)
    - [Java](#bc6f0dc77f5a1471c9d7508e5c1ca9e5)
      - [线程中sleep和wait的区别](#221070ece5a64d8100c3c238649f7c49)
      - [Thread中的start()和run()方法有什么区别](#1cc6a5f640233112a5f01f455bc632b1)
      - [关键字final和static是怎么使用的](#bc82c923cd1029d90c2364db06a43f3f)
      - [String,StringBuffer,StringBuilder区别](#ceddc2912f790275e025482fc4e6ff32)
      - [Java中重载和重写的区别：](#7293b7faa85f1f247da5fca3efee8d29)
      - [Http https区别 此处延伸：https的实现原理](#60f1e602574046dd5f97e1af04abcb46)
      - [Http位于TCP/IP模型中的第几层？为什么说Http是可靠的数据传输协议？](#0b3ea2154a389671e6a63967792ef477)
      - [HTTP链接的特点](#039f64d7a66d0aa6daf84da4c1e0b5c5)
      - [TCP和UDP的区别](#a17f8cff1cfa25a584fc0737bfb27b6d)
      - [Socket建立网络连接的步骤](#9b19b47f3cc7824234e71a0ea19bde6b)
---
## <span id="d11195cba9985a6572a41c4acf6edb33"/>面试题


#### <span id="73b6e7a611664773efc2cff20922ba56"/>Handler的原理

Android中主线程是不能进行耗时操作的，子线程是不能进行更新UI的。所以就有了handler，它的作用就是实现线程之间的通信。

handler整个流程中，主要有四个对象，handler，Message,MessageQueue,Looper。当应用创建的时候，就会在主线程中创建handler对象，
我们通过要传送的消息保存到Message中，handler通过调用sendMessage方法将Message发送到MessageQueue中，Looper对象就会不断的调用loop()方法
不断的从MessageQueue中取出Message交给handler进行处理。从而实现线程之间的通信。

#### <span id="db559f8440a393fee53b6a0082a3bd14"/>Binder机制原理

在Android系统的Binder机制中，是有Client,Service,ServiceManager,Binder驱动程序组成的，其中Client，service，Service
Manager运行在用户空间，Binder驱动程序是运行在内核空间的。

而Binder就是把这4种组件粘合在一块的粘合剂，其中核心的组件就是Binder驱动程序，Service
Manager提供辅助管理的功能，而Client和Service正是在Binder驱动程序和Service
Manager提供的基础设施上实现C/S
之间的通信。其中Binder驱动程序提供设备文件/dev/binder与用户控件进行交互，Client、Service，Service
Manager通过open和ioctl文件操作相应的方法与Binder驱动程序进行通信。
而Client和Service之间的进程间通信是通过Binder驱动程序间接实现的。而Binder
Manager是一个守护进程，用来管理Service，并向Client提供查询Service接口的能力。

#### <span id="7f65781ae13f5334571854ab2116c0ff"/>热修复的原理 

我们知道Java虚拟机 —— JVM
是加载类的class文件的，而Android虚拟机——Dalvik/ART VM
是加载类的dex文件，
而他们加载类的时候都需要ClassLoader,ClassLoader有一个子类BaseDexClassLoader，而BaseDexClassLoader下有一个
数组——DexPathList，是用来存放dex文件，当BaseDexClassLoader通过调用findClass方法时，实际上就是遍历数组，
找到相应的dex文件，找到，则直接将它return。

而热修复的解决方法就是将新的dex添加到该集合中，并且是在旧的dex的前面，
所以就会优先被取出来并且return返回。 
#### <span id="1e33e319686773adf5dca98d451aa0a5"/>Android内存泄露及管理

（1）内存溢出（OOM）和内存泄露（对象无法被回收）的区别。

（2）引起内存泄露的原因 (3) 内存泄露检测工具 ------>LeakCanary 内存溢出
outofmemory：是指程序在申请内存时，没有足够的内存空间供其使用，出现outofmemory；

比如申请了一个integer,但给它存了long才能存下的数，那就是内存溢出。内存溢出通俗的讲就是内存不够用
内存泄露 memoryleak：

是指程序在申请内存后，无法释放已申请的内存空间，一次内存泄露危害可以忽略，但内存泄露堆积后果很严重，无论多少内存,迟早会被占光

##### <span id="15d8c4186cfecadd297f2ab5c5aae17b"/>内存泄露原因：


一、Handler 引起的内存泄漏。

解决：将Handler声明为静态内部类，就不会持有外部类SecondActivity的引用，其生命周期就和外部类无关，
如果Handler里面需要context的话，可以通过弱引用方式引用外部类

二、单例模式引起的内存泄漏。

解决：Context是ApplicationContext，由于ApplicationContext的生命周期是和app一致的，不会导致内存泄漏

三、非静态内部类创建静态实例引起的内存泄漏。

解决：把内部类修改为静态的就可以避免内存泄漏了

四、非静态匿名内部类引起的内存泄漏。 解决：将匿名内部类设置为静态的。

五、注册/反注册未成对使用引起的内存泄漏。

注册广播接受器、EventBus等，记得解绑。

六、资源对象没有关闭引起的内存泄漏。

在这些资源不使用的时候，记得调用相应的类似close（）、destroy（）、recycler（）、release（）等方法释放。

七、集合对象没有及时清理引起的内存泄漏。

通常会把一些对象装入到集合中，当不使用的时候一定要记得及时清理集合，让相关对象不再被引用。

#### <span id="cc117d22db29bd51815f3a0401c29baf"/>Fragment与Fragment、Activity通信的方式

1.直接在一个Fragment中调用另外一个Fragment中的方法 

2.使用接口回调

3.使用广播 

4.Fragment直接调用Activity中的public方法 

#### <span id="b1fa8e7b610f82bba2cd2a19872f8632"/>Android UI适配

字体使用sp,使用dp，多使用match_parent，wrap_content，weight
图片资源，不同图片的的分辨率，放在相应的文件夹下可使用百分比代替。 
#### <span id="c2dcd19aa7cae42ad9108feab8268b96"/>app优化 

app优化:
    (工具：Hierarchy Viewer 分析布局 工具：TraceView测试分析耗时的) 
    App启动优化 
    布局优化 
    响应优化 
    内存优化 
    电池使用优化
    网络优化 
App启动优化(针对冷启动) 

App启动的方式有三种：

冷启动：App没有启动过或App进程被killed, 系统中不存在该App进程,
此时启动App即为冷启动。
 
热启动：热启动意味着你的App进程只是处于后台,
系统只是将其从后台带到前台, 展示给用户。 介于冷启动和热启动之间,
一般来说在以下两种情况下发生: (1)用户back退出了App, 然后又启动.
App进程可能还在运行, 但是activity需要重建。 (2)用户退出App后,
系统可能由于内存原因将App杀死, 进程和activity都需要重启,
但是可以在onCreate中将被动杀死锁保存的状态(saved instance state)恢复。

##### <span id="5e0ada5fd61cc852bc17fa1c593670ed"/>优化：

Application的onCreate（特别是第三方SDK初始化），首屏Activity的渲染都不要进行耗时操作，如果有，就可以放到子线程或者IntentService中
布局优化 尽量不要过于复杂的嵌套。可以使用<include>，<merge>，<ViewStub>
响应优化 Android系统每隔16ms会发出VSYNC信号重绘我们的界面(Activity)。

`页面卡顿的原因：` 
    
    (1)过于复杂的布局. 
    (2)UI线程的复杂运算 
    (3)频繁的GC,
        导致频繁GC有两个原因:
        1、内存抖动, 即大量的对象被创建又在短时间内马上被释放.
        2、瞬间产生大量的对象会严重占用内存区域。

内存优化： 参考内存泄露和内存溢出部分

电池使用优化(使用工具：Batterystats& bugreport) 
    (1)优化网络请求
    (2)定位中使用GPS, 请记得及时关闭

网络优化:(网络连接对用户的影响:流量,电量,用户等待)可在Android
studio下方logcat旁边那个工具Network Monitor检测

API设计：App与Server之间的API设计要考虑网络请求的频次, 资源的状态等.
以便App可以以较少的请求来完成业务需求和界面的展示.

Gzip压缩：使用Gzip来压缩request和response, 减少传输数据量,
从而减少流量消耗.

图片的Size：可以在获取图片时告知服务器需要的图片的宽高,
以便服务器给出合适的图片, 避免浪费.

网络缓存：适当的缓存,
既可以让我们的应用看起来更快, 也能避免一些不必要的流量消耗.
#### <span id="1de33821a53101e8d846e85f3618bbba"/>图片优化

(1)对图片本身进行操作。尽量不要使用setImageBitmap、setImageResource、
BitmapFactory.decodeResource来设置一张大图，因为这些方法在完成decode后，
最终都是通过java层的createBitmap来完成的，需要消耗更多内存.

(2)图片进行缩放的比例，SDK中建议其值是2的指数值,值越大会导致图片不清晰。

(3)不用的图片记得调用图片的recycle()方法
#### <span id="8af4b5f76bece869eb465977ff337426"/>HybridApp WebView和JS交互

Android与JS通过WebView互相调用方法，实际上是： Android去调用JS的代码

1. 通过WebView的loadUrl(),使用该方法比较简洁，方便。但是效率比较低，获取返回值比较困难。
2. 通过WebView的evaluateJavascript(),该方法效率高，但是4.4以上的版本才支持，4.4以下版本不支持。所以建议两者混合使用。

JS去调用Android的代码

1. 通过WebView的addJavascriptInterface（）进行对象映射 ，该方法使用简单，仅将Android对象和JS对象映射即可，但是存在比较大的漏洞。
漏洞产生原因是：当JS拿到Android这个对象后，就可以调用这个Android对象中所有的方法，
包括系统类（java.lang.Runtime 类），从而进行任意代码执行。

解决方式：

    (1)Google 在Android 4.2 版本中规定对被调用的函数以 @JavascriptInterface进行注解从而避免漏洞攻击。
    (2)在Android 4.2版本之前采用拦截prompt（）进行漏洞修复。
    
2. 通过 WebViewClient 的shouldOverrideUrlLoading ()方法回调拦截 url 。

这种方式的优点：不存在方式1的漏洞；

缺点：JS获取Android方法的返回值复杂。(ios主要用的是这个方式)

    (1)Android通过 WebViewClient 的回调方法shouldOverrideUrlLoading ()拦截 url
    (2)解析该 url 的协议
    (3)如果检测到是预先约定好的协议，就调用相应方法
    
3. 通过 WebChromeClient 的onJsAlert()、onJsConfirm()、onJsPrompt（）方法回调拦截JS对话框alert()、confirm()、prompt（） 消息

这种方式的优点：不存在方式1的漏洞；

缺点：JS获取Android方法的返回值复杂。
#### <span id="4f8816565e8a4d8fff9eff5d0d939d3d"/>JAVA GC原理

垃圾收集算法的核心思想是：对虚拟机可用内存空间，即堆空间中的对象进行识别，如果对象正在被引用，那么称其为存活对象
，反之，如果对象不再被引用，则为垃圾对象，可以回收其占据的空间，用于再分配。

垃圾收集算法的选择和垃圾收集系统参数的合理调节直接影响着系统性能。
#### <span id="b8319749b4c2c0221d0f117dbe06de6e"/> ANR 

ANR全名Application Not Responding, 也就是"应用无响应".

当操作在一段时间内系统无法处理时, 系统层面会弹出上图那样的ANR对话框.

产生原因：

    (1)5s内无法响应用户输入事件(例如键盘输入, 触摸屏幕等).
    (2)BroadcastReceiver在10s内无法结束 
    (3)Service 20s内无法结束（低概率）

解决方式：

    (1)不要在主线程中做耗时的操作，而应放在子线程中来实现。如onCreate()和onResume()里尽可能少的去做创建操作。
    (2)应用程序应该避免在BroadcastReceiver里做耗时的操作或计算。
    (3)避免在IntentReceiver里启动一个Activity，因为它会创建一个新的画面，并从当前用户正在运行的程序上抢夺焦点。
    (4)service是运行在主线程的，所以在service中做耗时操作，必须要放在子线程中。

#### <span id="8f4832ec71ecc5b67c07889892f2a8e8"/>设计模式 

单例模式：分为恶汉式和懒汉式 

恶汉式： 

    public class Singleton { 
        private static Singleton instance =
        new Singleton(); public static Singleton getInstance()
    
        { 
            return instance ; 
        } 
    }

懒汉式：

    public class Singleton02{ 
        private static Singleton02 instance;
        public static Singleton02 getInstance(){ 
            if (instance == null) 
            { 
                synchronized (Singleton02.class) 
                { 
                    if (instance == null) 
                    { 
                        instance = new Singleton02(); 
                    } 
                } 
            } 
            return instance; 
        } 
    }

#### <span id="b5035777bfa3df19db181b25289a3166"/>RxJava 

#### <span id="73ee0ad6f84149f63602b6fdc704b573"/>MVP，MVC，MVVM 

此处延伸：手写mvp例子，与mvc之间的区别，mvp的优势

MVP模式，对应着Model--业务逻辑和实体模型,view--对应着activity，负责View的绘制以及与用户交互,
Presenter--负责View和Model之间的交互,MVP模式是在MVC模式的基础上，
将Model与View彻底分离使得项目的耦合性更低，在Mvc中项目中的activity对应着mvc中的C--Controllor,
而项目中的逻辑处理都是在这个C中处理，同时View与Model之间的交互，也是也就是说，
mvc中所有的逻辑交互和用户交互，都是放在Controllor中，也就是activity中。

View和model是可以直接通信的。而MVP模式则是分离的更加彻底，
分工更加明确Model--业务逻辑和实体模型，view--负责与用户交互，Presenter
负责完成View于Model间的交互，MVP和MVC最大的区别是MVC中是允许Model和View进行交互的，而MVP中很明显，
Model与View之间的交互由Presenter完成。还有一点就是Presenter与View之间的交互是通过接口的
#### <span id="2f7b9656a68b01a5d2639f5d45c212d4"/>手写算法（选择冒泡必须要会） 

#### <span id="ddba29c1b4e2160f23b2dda35c5c987f"/>JNI 


    (1)安装和下载Cygwin，下载 Android NDK
    (2)在ndk项目中JNI接口的设计 (3)使用C/C++实现本地方法
    (4)JNI生成动态链接库.so文件
    (5)将动态链接库复制到java工程，在java工程中调用，运行java工程即可

#### <span id="b6b433b5cacc1e9fbfb14a3eddef1760"/>RecyclerView和ListView的区别

RecyclerView可以完成ListView,GridView的效果，还可以完成瀑布流的效果。同时还可以设置列表的滚动方向（垂直或者水平）；

RecyclerView中view的复用不需要开发者自己写代码，系统已经帮封装完成了。

RecyclerView可以进行局部刷新。

RecyclerView提供了API来实现item的动画效果。 在性能上：

如果需要频繁的刷新数据，需要添加动画，则RecyclerView有较大的优势。
如果只是作为列表展示，则两者区别并不是很大。

#### <span id="95ea4efe05cf8de8addaaed9b5269b98"/>Universal-ImageLoader，Picasso，Fresco，Glide对比 

Fresco 是
Facebook 推出的开源图片缓存工具，主要特点包括：两个内存缓存加上 Native
缓存构成了三级缓存，
 
`优点：`
1. 图片存储在安卓系统的匿名共享内存, 而不是虚拟机的堆内存中, 图片的中间缓冲数据也存放在本地堆内存, 所以, 应用程序有更多的内存使用, 不会因为图片加载而导致oom, 同时也减少垃圾回收器频繁调用回收 Bitmap 导致的界面卡顿, 性能更高。
2. 渐进式加载 JPEG 图片, 支持图片从模糊到清晰加载。
3. 图片可以以任意的中心点显示在 ImageView, 而不仅仅是图片的中心。
4. JPEG 图片改变大小也是在 native 进行的, 不是在虚拟机的堆内存, 同样减少 OOM。
5. 很好的支持 GIF 图片的显示。

`缺点:`
1. 框架较大, 影响 Apk 体积
2. 使用较繁琐

Universal-ImageLoader：（估计由于HttpClient被Google放弃，作者就放弃维护这个框架）

`优点：`

1. 支持下载进度监听
2. 可以在 View 滚动中暂停图片加载，通过 PauseOnScrollListener 接口可以在 View 滚动中暂停图片加载。
3. 默认实现多种内存缓存算法 这几个图片缓存都可以配置缓存算法，不过 ImageLoader 默认实现了较多缓存算法，如 Size 最大先删除、使用最少先删除、最近最少使用、先进先删除、时间最长先删除等。
4. 支持本地缓存文件名规则定义

`Picasso 优点`

1. 自带统计监控功能。支持图片缓存使用的监控，包括缓存命中率、已使用内存大小、节省的流量等。
2. 支持优先级处理。每次任务调度前会选择优先级高的任务，比如 App 页面中 Banner 的优先级高于 Icon 时就很适用。
3. 支持延迟到图片尺寸计算完成加载
4. 支持飞行模式、并发线程数根据网络类型而变。 手机切换到飞行模式或网络类型变换时会自动调整线程池最大并发数，
比如 wifi 最大并发为 4，4g 为 3，3g 为 2。  这里 Picasso 根据网络类型来决定最大并发数，而不是 CPU 核数。
5. “无”本地缓存。无”本地缓存，不是说没有本地缓存，而是 Picasso 自己没有实现，
交给了 Square 的另外一个网络库 okhttp 去实现，这样的好处是可以通过请求 Response Header 
中的 Cache-Control 及 Expired 控制图片的过期时间。

`Glide 优点`

1. 不仅仅可以进行图片缓存还可以缓存媒体文件。Glide 不仅是一个图片缓存，它支持 Gif、WebP、缩略图。甚至是 Video，所以更该当做一个媒体缓存。
2. 支持优先级处理。
3. 与 Activity/Fragment 生命周期一致，支持 trimMemory。Glide 对每个 context 都保持一个 RequestManager，
通过 FragmentTransaction 保持与 Activity/Fragment 生命周期一致，并且有对应的 trimMemory 接口实现可供调用。
4. 支持 okhttp、Volley。Glide 默认通过 UrlConnection 获取数据，可以配合 okhttp 或是 Volley 使用。
实际 ImageLoader、Picasso 也都支持 okhttp、Volley。
5. 内存友好。Glide 的内存缓存有个 active 的设计，从内存缓存中取数据时，不像一般的实现用 get，
而是用 remove，再将这个缓存数据放到一个 value 为软引用的 activeResources map 中，并计数引用数，
在图片加载完成后进行判断，如果引用计数为空则回收掉。内存缓存更小图片，Glide 以 url、view_width、view_height、
屏幕的分辨率等做为联合 key，将处理后的图片缓存在内存缓存中，
而不是原始图片以节省大小与 Activity/Fragment 生命周期一致，支持 trimMemory。
图片默认使用默认 RGB_565 而不是 ARGB_888，虽然清晰度差些，但图片更小，也可配置到 ARGB_888。
6. Glide 可以通过 signature 或不使用本地缓存支持 url 过期

#### <span id="ace088d91e5621d12cf218459ed4d309"/>Xutils, OKhttp, Volley, Retrofit对比

`Xutils:`这个框架非常全面，可以进行网络请求，可以进行图片加载处理，可以数据储存，还可以对view进行注解，
使用这个框架非常方便，但是缺点也是非常明显的，使用这个项目，会导致项目对这个框架依赖非常的严重，
一旦这个框架出现问题，那么对项目来说影响非常大的。

`OKhttp：`Android开发中是可以直接使用现成的api进行网络请求的。
就是使用HttpClient,HttpUrlConnection进行操作。okhttp针对Java和Android程序，
封装的一个高性能的http请求库，支持同步，异步，而且okhttp又封装了线程池，
封装了数据转换，封装了参数的使用，错误处理等。API使用起来更加的方便。
但是我们在项目中使用的时候仍然需要自己在做一层封装，这样才能使用的更加的顺手。

`Volley：`Volley是Google官方出的一套小而巧的异步请求库，该框架封装的扩展性很强，支持HttpClient、HttpUrlConnection，
甚至支持OkHttp，而且Volley里面也封装了ImageLoader，所以如果你愿意你甚至不需要使用图片加载框架，
不过这块功能没有一些专门的图片加载框架强大，对于简单的需求可以使用，稍复杂点的需求还是需要用到专门的图片加载框架。
Volley也有缺陷，比如不支持post大数据，所以不适合上传文件。不过Volley设计的初衷本身也就是为频繁的、数据量小的网络请求而生。

`Retrofit：`Retrofit是Square公司出品的默认基于OkHttp封装的一套RESTful网络请求框架，RESTful是目前流行的一套api设计的风格，
并不是标准。Retrofit的封装可以说是很强大，里面涉及到一堆的设计模式,可以通过注解直接配置请求，
可以使用不同的http客户端，虽然默认是用http，可以使用不同Json Converter
来序列化数据，同时提供对RxJava的支持，使用Retrofit + OkHttp + RxJava +
Dagger2 可以说是目前比较潮的一套框架，但是需要有比较高的门槛。

Volley VS OkHttp

Volley的优势在于封装的更好，而使用OkHttp你需要有足够的能力再进行一次封装。而OkHttp的优势在于性能更高，因为
OkHttp基于NIO和Okio ，所以性能上要比 Volley更快。

IO和NIO这两个都是Java中的概念，如果我从硬盘读取数据，

第一种方式就是程序一直等，
数据读完后才能继续操作这种是最简单的也叫阻塞式IO,还有一种是你读你的,程序接着往下执行，
等数据处理完你再来通知我，然后再处理回调。

而第二种就是
NIO 的方式，非阻塞式， 所以NIO当然要比IO的性能要好了,而 Okio是 Square
公司基于IO和NIO基础上做的一个更简单、高效处理数据流的一个库。理论上如果Volley和OkHttp对比的话，更倾向于使用
Volley，因为Volley内部同样支持使用OkHttp,这点OkHttp的性能优势就没了，
而且 Volley 本身封装的也更易用，扩展性更好些。 

OkHttp VS Retrofit

毫无疑问，Retrofit 默认是基于 OkHttp
而做的封装，这点来说没有可比性，肯定首选 Retrofit。 Volley VS Retrofit
这两个库都做了不错的封装，但Retrofit解耦的更彻底,尤其Retrofit2.0出来，Jake对之前1.0设计不合理的地方做了大量重构，
职责更细分，而且Retrofit默认使用OkHttp,性能上也要比Volley占优势，再有如果你的项目如果采用了RxJava
，那更该使用
Retrofit。所以这两个库相比，Retrofit更有优势，在能掌握两个框架的前提下该优先使用
Retrofit。但是Retrofit门槛要比Volley稍高些，要理解他的原理，各种用法，
想彻底搞明白还是需要花些功夫的，如果你对它一知半解，那还是建议在商业项目使用Volley吧。

### <span id="bc6f0dc77f5a1471c9d7508e5c1ca9e5"/>Java

#### <span id="221070ece5a64d8100c3c238649f7c49"/>线程中sleep和wait的区别

(1)这两个方法来自不同的类，sleep是来自Thread，wait是来自Object；

(2)sleep方法没有释放锁，而wait方法释放了锁。

(3)wait,notify,notifyAll只能在同步控制方法或者同步控制块里面使用，而sleep可以在任何地方使用。
#### <span id="1cc6a5f640233112a5f01f455bc632b1"/>Thread中的start()和run()方法有什么区别

start()方法是用来启动新创建的线程，而start()内部调用了run()方法，这和直接调用run()方法是不一样的，如果直接调用run()方法，
则和普通的方法没有什么区别。 
#### <span id="bc82c923cd1029d90c2364db06a43f3f"/>关键字final和static是怎么使用的

final:
1. final变量即为常量，只能赋值一次。
2. final方法不能被子类重写。
3. final类不能被继承。 
static：
- static变量：对于静态变量在内存中只有一个拷贝（节省内存），JVM只为静态分配一次内存，
在加载类的过程中完成静态变量的内存分配，可用类名直接访问（方便），当然也可以通过对象来访问（但是这是不推荐的）。
- static代码块 static代码块是类加载时，初始化自动执行的。
- static方法:
   static方法可以直接通过类名调用，任何的实例也都可以调用，因此static方法中不能用this和super关键字，
   不能直接访问所属类的实例变量和实例方法(就是不带static的成员变量和成员成员方法)，只能访问所属类的静态成员变量和成员方法。
   
#### <span id="ceddc2912f790275e025482fc4e6ff32"/>String,StringBuffer,StringBuilder区别

1、三者在执行速度上：StringBuilder > StringBuffer > String
(由于String是常量，不可改变，拼接时会重新创建新的对象)。

2、StringBuffer是线程安全的，StringBuilder是线程不安全的。（由于StringBuffer有缓冲区）
#### <span id="7293b7faa85f1f247da5fca3efee8d29"/>Java中重载和重写的区别：

1、重载：一个类中可以有多个相同方法名的，但是参数类型和个数都不一样。这是重载。

2、重写：子类继承父类，则子类可以通过实现父类中的方法，从而新的方法把父类旧的方法覆盖。

#### <span id="60f1e602574046dd5f97e1af04abcb46"/>Http https区别 此处延伸：https的实现原理

1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用。

2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议。

3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

4、http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。

https实现原理：

    （1）客户使用https的URL访问Web服务器，要求与Web服务器建立SSL连接。
    （2）Web服务器收到客户端请求后，会将网站的证书信息（证书中包含公钥）传送一份给客户端。
    （3）客户端的浏览器与Web服务器开始协商SSL连接的安全等级，也就是信息加密的等级。
    （4）客户端的浏览器根据双方同意的安全等级，建立会话密钥，然后利用网站的公钥将会话密钥加密，并传送给网站。
    （5）Web服务器利用自己的私钥解密出会话密钥。
    （6）Web服务器利用会话密钥加密与客户端之间的通信。
#### <span id="0b3ea2154a389671e6a63967792ef477"/>Http位于TCP/IP模型中的第几层？为什么说Http是可靠的数据传输协议？

tcp/ip的五层模型： 

从下到上：物理层->数据链路层->网络层->传输层->应用层

其中tcp/ip位于模型中的网络层，处于同一层的还有ICMP（网络控制信息协议）。http位于模型中的应用层
由于tcp/ip是面向连接的可靠协议，而http是在传输层基于tcp/ip协议的，所以说http是可靠的数据传输协议。

#### <span id="039f64d7a66d0aa6daf84da4c1e0b5c5"/>HTTP链接的特点

HTTP连接最显著的特点是客户端发送的每次请求都需要服务器回送响应，在请求结束后，会主动释放连接。
从建立连接到关闭连接的过程称为“一次连接”。 
#### <span id="a17f8cff1cfa25a584fc0737bfb27b6d"/>TCP和UDP的区别

tcp是面向连接的，由于tcp连接需要三次握手，所以能够最低限度的降低风险，保证连接的可靠性。

udp
不是面向连接的，udp建立连接前不需要与对象建立连接，无论是发送还是接收，都没有发送确认信号。所以说udp是不可靠的。
由于udp不需要进行确认连接，使得UDP的开销更小，传输速率更高，所以实时行更好。

#### <span id="9b19b47f3cc7824234e71a0ea19bde6b"/>Socket建立网络连接的步骤

建立Socket连接至少需要一对套接字，其中一个运行与客户端--ClientSocket，一个运行于服务端--ServiceSocket

1、服务器监听：服务器端套接字并不定位具体的客户端套接字，而是处于等待连接的状态，实时监控网络状态，等待客户端的连接请求。

2、客户端请求：指客户端的套接字提出连接请求，要连接的目标是服务器端的套接字。注意：客户端的套接字必须描述他要连接的服务器的套接字，
指出服务器套接字的地址和端口号，然后就像服务器端套接字提出连接请求。

3、连接确认：当服务器端套接字监听到客户端套接字的连接请求时，就响应客户端套接字的请求，建立一个新的线程，把服务器端套接字的描述
发给客户端，一旦客户端确认了此描述，双方就正式建立连接。而服务端套接字则继续处于监听状态，继续接收其他客户端套接字的连接请求。
