# View
- 自定义view属性：
  - xml方式：
    1. 通过在res/values目录下attrs.xml属性文件设置
    2. 在使用自定义view的布局文件中引用自定义view的命名空间，添加自定义view的属性
    3. 在自定义view的构造函数中，获取属性
  - 代码动态设置： 
    1. 添加方法来设置属性值
- 自定义view主要重写的方法：
  - onMeasure()     
    通过测量view的宽高，计算合适的数值并设置view的宽高；      
    一般是获取MeasureSpec类的三个模式属性--UNSPECIFIED, EXACTLY,
    AT_MOST其中一个数值，判断模式类型，然后在获取具体value；
    - view：         
      单个的view一般处理好自己的宽高即可，结合获取的padding和margin来计算
    - viewGroup：
      需要先测量子view的宽高大小，计算出具体的数值，然后再返回来计算自己到底需要多大；       
      需要把子view的宽度加起来，和原先viewGroup设定的宽度作比较，最后来确定该设置多大，同理，高度也一样；
  - onLayout()     
    view一般不用处理，主要是给viewGroup来放置子view的位置；
  - onDraw() 
    - view调用canvas来绘制界面：        
      用于绘制一些背景，前景，线条，文字，图形，还有自定义的一些图案等；
    - viewGroup会调用dispatchView()来调用子view的onDraw()来绘制；
- 自定义view动画实现：
  - 借助ViewDragHelper和surfaceView实现；可以实现较为炫酷的动画；     
    ViewDragHelper主要提供4个接口方法:       
    - onViewCaptured() 捕获哪些view；
    - clampViewPositionHorizontal() 
      view发生水平移动的时候回调位置等参数的处理；
    - clampViewPositionVertical() 
      view发生垂直移动的时候回调位置等参数的处理；
    - onViewReleased()view释放的时候回调；
  - 借助属性动画实现；
- 自定义view事件处理：      
  事件传递顺序：   
  用户点击屏幕产生MotionEvent（点击事件）
  Activity接收MotionEvent（点击事件）—>传递给Window—>传递给DecorView（ViewGroup）—>执行ViewGroup的dispatchTouchEvent()
  ViewGroup接收到MotionEvent（点击事件）之后，按照事件分发机制去分发事件。        
  若当子View不消耗事件，onTouchEvent()返回false，那么这个事件会传递回其父View的onTouchEvent()，如若父View也不消耗，最后会传递回给Activity进行处理。       
  伪代码如下：
  ```
  public boolean dispatchTouchEvent(MotionEvent ev) {
        boolean consume = false;
        if(onInterceptTouchEvent(ev)){
            consume = onTouchEvent(ev);
        }else {
            consume = child.dispatchTouchEvent(ev);
        }
        return consume;
    }
  ```
  - dispatchTouchEvent()        
    用来进行事件的分发，如果MotionEvent（点击事件）能够传递给该View，那么该方法一定会被调用。返回值由
    本身的onTouchEvent() 和 子View的dispatchTouchEvent()的返回值 共同决定。         
    返回值为true，则表示该点击事件被本身或者子View消耗。
    返回值为false，则表示该ViewGroup没有子元素，或者子元素没有消耗该事件。      
    
  - onInterceptTouchEvent()     
  用来判断是否拦截某个事件，如果当前View拦截了某个事件，那么在同一个事件序列中不会再访问该方法。
  - onTouchEvent()      
    返回结果表示是否消耗当前事件，如果不消耗（返回false），则在同一个事件序列中View不会再次接收到事件。   
  1. 事件分发机制就是点击事件的分发，在手指接触屏幕后产生的同一个事件序列都是点击事件。
  2. 点击事件的传递顺序是由父到子，再由子到父的。
  3. 正常情况下事件只能被一个View拦截。
  4. 如果View决定拦截事件，那么这一个事件序列都会由这个View来处理。
  5. 当子View不消耗点击事件，那点击事件将交由给他的父View去处理，如果所有的View都没有消耗掉点击事件，则Activity调用自己的onTouchEvent。
  6. onInterceptTouchEvent()方法不一定会每次都执行，如果想对每个事件都进行处理，那还是在dispatchTouchEvent()里面处理吧。
  7. OnTouchListener的优先级高于onTouchEvent()。这样做的好处是方便在外部处理事件。
  8. 当我们把View设置为不可用状态，View依然会消耗点击事件，只是看起来不可用。