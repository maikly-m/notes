# 动画
在Android中我们一般将动画分为两类，一类是View Animation(视图动画)，一类是Property Animation,当然也有说分为三种，Frame Animation，
Tween Animation，和Property Animation,由于前两种一般都是作用于整个View的，所以就统称为View Animation。
- view的动画，主要是自定义view自身通过onDraw()实现的一些动画效果；
- Frame Animation
  将一系列的图片一张一张的展示出来，通过布局文件或者代码都可以实现；--- 
  AnimationDrawable类
- Tween Animation 即补间动画，主要分为四种，分别是平移、缩放、旋转、透明度；
  通过布局文件或者代码都可以实现；可以添加插值器，监听回调（点击范围不随位置变化）--
  Animation 类
- Property Animation
  作用于View的属性，效果和补间动画一样（点击的范围和view的位置同步）--
  AnimatorSet类和ObjectAnimator类
  


