`目录：`
  - [面试题](#md_面试题)
      - [java中==和equals和hashCode的区别 ](#md_java中==和equals和hashCode的区别 )
      - [int与integer的区别](#md_int与integer的区别)
      - [String、StringBuffer、StringBuilder区别](#md_String、StringBuffer、StringBuilder区别)
      - [什么是内部类？内部类的作用](#md_什么是内部类？内部类的作用)
      - [进程和线程的区别](#md_进程和线程的区别)
      - [final，finally，finalize的区别](#md_final，finally，finalize的区别)
      - [Serializable 和Parcelable 的区别](#md_Serializable 和Parcelable 的区别)
      - [静态属性和静态方法是否可以被继承？ 是否可以被重写？以及原因？](#md_静态属性和静态方法是否可以被继承？ 是否可以被重写？以及原因？)
      - [成员内部类、静态内部类、局部内部类和匿名内部类的理解，以及项目中的应用](#md_成员内部类、静态内部类、局部内部类和匿名内部类的理解，以及项目中的应用)
      - [string 转换成 integer的方式及原理](#md_string 转换成 integer的方式及原理)
      - [哪些情况下的对象会被垃圾回收机制处理掉？](#md_哪些情况下的对象会被垃圾回收机制处理掉？)
        - [ `这里有2种方法：` ](#md_ `这里有2种方法：` )
      - [静态代理和动态代理的区别，什么场景使用？ ](#md_静态代理和动态代理的区别，什么场景使用？ )
      - [Java中实现多态的机制是什么？](#md_Java中实现多态的机制是什么？)
      - [说说你对Java反射的理解 ](#md_说说你对Java反射的理解 )
      - [说说你对Java注解的理解](#md_说说你对Java注解的理解)
      - [Java中String的了解 在源码中string是用final](#md_Java中String的了解 在源码中string是用final)
      - [String为什么要设计成不可变的？ ](#md_String为什么要设计成不可变的？ )
      - [Object类的equal和hashCode方法重写，为什么？](#md_Object类的equal和hashCode方法重写，为什么？)
---
## <span id="md_面试题"/>面试题
#### <span id="md_java中==和equals和hashCode的区别 "/>java中==和equals和hashCode的区别 

基本数据类型的==比较的值相等.

类的==比较的内存的地址，即是否是同一个对象，在不覆盖equals的情况下，同比较内存地址，原实现也为 == ，如String等重写了equals方法.

hashCode也是Object类的一个方法。返回一个离散的int型整数。在集合类操作中使用，为了提高查询速度。（HashMap，HashSet等比较是否为同一个）

如果两个对象equals，Java运行时环境会认为他们的hashcode一定相等。

如果两个对象不equals，他们的hashcode有可能相等。

如果两个对象hashcode相等，他们不一定equals。

如果两个对象hashcode不相等，他们一定不equals。

#### <span id="md_int与integer的区别"/>int与integer的区别

int 基本类型

integer 对象 int的封装类
#### <span id="md_String、StringBuffer、StringBuilder区别"/>String、StringBuffer、StringBuilder区别

String:字符串常量
不适用于经常要改变值得情况，每次改变相当于生成一个新的对象

StringBuffer:字符串变量 （线程安全）

StringBuilder:字符串变量（线程不安全） 确保单线程下可用，效率略高于StringBuffer
#### <span id="md_什么是内部类？内部类的作用"/>什么是内部类？内部类的作用

内部类可直接访问外部类的属性

Java中内部类主要分为成员内部类、局部内部类(嵌套在方法和作用域内)、匿名内部类（没构造方法）、静态内部类（static修饰的类，不能使用任何外围类的非static成员变量和方法， 不依赖外围类）
#### <span id="md_进程和线程的区别"/>进程和线程的区别

进程是cpu资源分配的最小单位，线程是cpu调度的最小单位。

进程之间不能共享资源，而线程共享所在进程的地址空间和其它资源。

一个进程内可拥有多个线程，进程可开启进程，也可开启线程。

一个线程只能属于一个进程，线程可直接使用同进程的资源,线程依赖于进程而存在。 

#### <span id="md_final，finally，finalize的区别"/>final，finally，finalize的区别

final:修饰类、成员变量和成员方法，类不可被继承，成员变量不可变，成员方法不可重写

finally:与try...catch...共同使用，确保无论是否出现异常都能被调用到

finalize:类的方法,垃圾回收之前会调用此方法,子类可以重写finalize()方法实现对资源的回收
#### <span id="md_Serializable 和Parcelable 的区别"/>Serializable 和Parcelable 的区别

Serializable Java 序列化接口 在硬盘上读写
读写过程中有大量临时变量的生成，内部执行大量的i/o操作，效率很低。

Parcelable Android 序列化接口 效率高 使用麻烦 在内存中读写（AS有相关插件 一键生成所需方法） ，对象不能保存到磁盘中
#### <span id="md_静态属性和静态方法是否可以被继承？ 是否可以被重写？以及原因？"/>静态属性和静态方法是否可以被继承？ 是否可以被重写？以及原因？

可继承 不可重写 而是被隐藏

如果子类里面定义了静态方法和属性，那么这时候父类的静态方法或属性称之为"隐藏"。
如果你想要调用父类的静态方法和属性，直接通过父类名.方法或变量名完成。
#### <span id="md_成员内部类、静态内部类、局部内部类和匿名内部类的理解，以及项目中的应用"/>成员内部类、静态内部类、局部内部类和匿名内部类的理解，以及项目中的应用

Java中内部类主要分为成员内部类、局部内部类(嵌套在方法和作用域内)、匿名内部类（没构造方法）、
静态内部类（static修饰的类，不能使用任何外围类的非static成员变量和方法，不依赖外围类）

使用内部类最吸引人的原因是：每个内部类都能独立地继承一个（接口的）实现，
所以无论外围类是否已经继承了某个（接口的）实现，对于内部类都没有影响。

因为Java不支持多继承，支持实现多个接口。但有时候会存在一些使用接口很难解决的问题，
这个时候我们可以利用内部类提供的、可以继承多个具体的或者抽象的类的能力来解决这些程序设计问题。
可以这样说，接口只是解决了部分问题，而内部类使得多重继承的解决方案变得更加完整。
#### <span id="md_string 转换成 integer的方式及原理"/>string 转换成 integer的方式及原理

String integer Integer.parseInt(string);

Integerstring Integer.toString();

#### <span id="md_哪些情况下的对象会被垃圾回收机制处理掉？"/>哪些情况下的对象会被垃圾回收机制处理掉？
  1.所有实例都没有活动线程访问。
  
  2.没有被其他任何实例访问的循环引用实例。 
  
  3.Java 中有不同的引用类型。
  判断实例是否符合垃圾收集的条件都依赖于它的引用类型。
  要判断怎样的对象是没用的对象。
  
##### <span id="md_ `这里有2种方法：` "/> `这里有2种方法：` 
  
  1.采用标记计数的方法：
  
  给内存中的对象给打上标记，对象被引用一次，计数就加1，引用被释放了，计数就减一，
  当这个计数为0的时候，这个对象就可以被回收了。当然，这也就引发了一个问题：
  循环引用的对象是无法被识别出来并且被回收的。所以就有了第二种方法：
  
  2.采用根搜索算法：
  从一个根出发，搜索所有的可达对象，这样剩下的那些对象就是需要被回收的
  
#### <span id="md_静态代理和动态代理的区别，什么场景使用？ "/>静态代理和动态代理的区别，什么场景使用？ 
静态代理类：

由程序员创建或由特定工具自动生成源代码，再对其编译。在程序运行前，代理类的.class文件就已经存在了。

动态代理类：

在程序运行时，运用反射机制动态创建而成。 

#### <span id="md_Java中实现多态的机制是什么？"/>Java中实现多态的机制是什么？
答：方法的重写Overriding和重载Overloading是Java多态性的不同表现
重写Overriding是父类与子类之间多态性的一种表现
重载Overloading是一个类中多态性的一种表现.
 
#### <span id="md_说说你对Java反射的理解 "/>说说你对Java反射的理解 
JAVA反射机制是在运行状态中, 对于任意一个类,
都能够知道这个类的所有属性和方法; 对于任意一个对象,
都能够调用它的任意一个方法和属性。

从对象出发，通过反射（Class类）可以取得取得类的完整信息（类名
Class类型，所在包、具有的所有方法
Method[]类型、某个方法的完整信息（包括修饰符、返回值类型、异常、参数类型）、所有属性
Field[]、某个属性的完整信息、构造器
Constructors），调用类的属性或方法自己的总结：
在运行过程中获得类、对象、方法的所有信息
 
#### <span id="md_说说你对Java注解的理解"/>说说你对Java注解的理解
元注解

元注解的作用就是负责注解其他注解。java5.0的时候，定义了4个标准的meta-annotation类型，它们用来提供对其他注解的类型作说明。

1.@Target 2.@Retention 3.@Documented 4.@Inherited 

#### <span id="md_Java中String的了解 在源码中string是用final"/>Java中String的了解 在源码中string是用final
进行修饰，它是不可更改，不可继承的常量。

#### <span id="md_String为什么要设计成不可变的？ "/>String为什么要设计成不可变的？ 
1、字符串池的需求

字符串池是方法区（Method
Area）中的一块特殊的存储区域。当一个字符串已经被创建并且该字符串在 池
中，该字符串的引用会立即返回给变量，而不是重新创建一个字符串再将引用返回给变量。如果字符串不是不可变的，那么改变一个引用（如:
string2）的字符串将会导致另一个引用（如: string1）出现脏数据。

2、允许字符串缓存哈希码 

在java中常常会用到字符串的哈希码，例如： HashMap
。String的不变性保证哈希码始终一，因此，他可以不用担心变化的出现。
这种方法意味着不必每次使用时都重新计算一次哈希码——这样，效率会高很多。

3、安全 

String广泛的用于java 类中的参数，如：网络连接（Network
connetion），打开文件（opening files
）等等。如果String不是不可变的，网络连接、文件将会被改变——这将会导致一系列的安全威胁。
操作的方法本以为连接上了一台机器，但实际上却不是。由于反射中的参数都是字符串，同样，也会引起一系列的安全问题。
#### <span id="md_Object类的equal和hashCode方法重写，为什么？"/>Object类的equal和hashCode方法重写，为什么？
首先equals与hashcode间的关系是这样的：

1、如果两个对象相同（即用equals比较返回true），那么它们的hashCode值一定要相同；

2、如果两个对象的hashCode相同，它们并不一定相同(即用equals比较返回false)

由于为了提高程序的效率才实现了hashcode方法，先进行hashcode的比较，如果不同，
那没就不必在进行equals的比较了，这样就大大减少了equals比较的次数，
这对比需要比较的数量很大的效率提高是很明显的
