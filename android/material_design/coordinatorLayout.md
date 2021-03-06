## CoordinatorLayout

CoordinatorLayout是一个“加强版”的 FrameLayout,有两个作用

- （1）用作应用的顶层布局管理器 
- （2）CoordinatorLayout主要是通过设置子视图的Behavior来达到协调子视图之间的工作。

它的直接子布局有： AppBarLayout

### behavior自定义

- `behavior 事件传递过程：`

    CoordinatorLayout作为顶层的布局，点击或者触摸事件首先分发到CoordinatorLayout，然后走onInterceptTouchEvent(),
    -> 
    ```
    public boolean onInterceptTouchEvent(MotionEvent ev) {
            int action = ev.getActionMasked();
            if (action == 0) {
                this.resetTouchBehaviors(true);
            }
    
            boolean intercepted = this.performIntercept(ev, 0);
            if (action == 1 || action == 3) {
                this.resetTouchBehaviors(true);
            }
    
            return intercepted;
        }
    
    ```
    -> 然后走到resetTouchBehaviors(),
    ```
     private void resetTouchBehaviors(boolean notifyOnInterceptTouchEvent) {
            int childCount = this.getChildCount();
    
            int i;
            View child;
            CoordinatorLayout.LayoutParams lp;
            for(i = 0; i < childCount; ++i) {
                child = this.getChildAt(i);
                lp = (CoordinatorLayout.LayoutParams)child.getLayoutParams();
                CoordinatorLayout.Behavior b = lp.getBehavior();
                if (b != null) {
                    long now = SystemClock.uptimeMillis();
                    MotionEvent cancelEvent = MotionEvent.obtain(now, now, 3, 0.0F, 0.0F, 0);
                    if (notifyOnInterceptTouchEvent) {
                        b.onInterceptTouchEvent(this, child, cancelEvent);
                    } else {
                        b.onTouchEvent(this, child, cancelEvent);
                    }
    
                    cancelEvent.recycle();
                }
            }
    
            for(i = 0; i < childCount; ++i) {
                child = this.getChildAt(i);
                lp = (CoordinatorLayout.LayoutParams)child.getLayoutParams();
                lp.resetTouchBehaviorTracking();
            }
    
            this.mBehaviorTouchView = null;
            this.mDisallowInterceptReset = false;
        }
    
    ```
    ->
    所以可以看到，最初xml布局中直接子布局设置了behavior的布局会获得事件传递的机会，
    将触发behavior中处理事件的方法；        
    其中behavior的实现是有具体的子布局处理的，比如`<string
    name="appbar_scrolling_view_behavior"
    translatable="false">android.support.design.widget.AppBarLayout$ScrollingViewBehavior</string>`
    是属于AppBarLayout的behavior；所以具体的拦截处理将转移到AppBarLayout下；且AppBarLayout下的子布局设置了属性`app:layout_scrollFlags="scroll|snap|enterAlways"`后
    就可以对behavior做定制化的处理；

- `behavior自定义：`
    
    自定义Behavior可以选择重写以下的几个方法有：
    
    onInterceptTouchEvent()：是否拦截触摸事件
    
    onTouchEvent()：处理触摸事件
    
    layoutDependsOn()：确定使用Behavior的View要依赖的View的类型
    
    onDependentViewChanged()：当被依赖的View状态改变时回调
    
    onDependentViewRemoved()：当被依赖的View移除时回调
    
    onMeasureChild()：测量使用Behavior的View尺寸
    
    onLayoutChild()：确定使用Behavior的View位置
    
    onStartNestedScroll()：嵌套滑动开始（ACTION_DOWN），确定Behavior是否要监听此次事件
    
    onStopNestedScroll()：嵌套滑动结束（ACTION_UP或ACTION_CANCEL）
    
    onNestedScroll()：嵌套滑动进行中，要监听的子 View的滑动事件已经被消费
    
    onNestedPreScroll()：嵌套滑动进行中，要监听的子 View将要滑动，滑动事件即将被消费（但最终被谁消费，可以通过代码控制）
    
    onNestedFling()：要监听的子 View在快速滑动中
    
    onNestedPreFling()：要监听的子View即将快速滑动
    
    



