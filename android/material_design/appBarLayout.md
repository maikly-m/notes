## AppBarLayout

需要依赖CoordinatorLayout，通过添加behavior来实现UI动作；

behavior依赖于`<string name="appbar_scrolling_view_behavior"
translatable="false">android.support.design.widget.AppBarLayout$ScrollingViewBehavior</string>`

layout_scrollFlags有5种动作，分别是scroll,enterAlways,enterAlwaysCollapsed,exitUntilCollapsed,snap

AppBarLayout可以添加多个view，添加了layout_scrollFlags的view才会有所动作；
比如ScrollView设置了behavior，那么->
- scroll    
随着ScrollView滑动而滑动；
- enterAlways   
随着ScrollView向下滑动时，子View 将直接向下滑动，而不管ScrollView 是否在滑动。注意：要与scroll 搭配使用，否者是不能滑动的。
- enterAlwaysCollapsed  
enterAlwaysCollapsed 是对enterAlways 的补充，当ScrollView 向下滑动的时候，滑动View（也就是设置了enterAlwaysCollapsed 的View）下滑至折叠的高度，
当ScrollView 到达滑动范围的结束值的时候，滑动View剩下的部分开始滑动。这个折叠的高度是通过View的minimum height （最小高度）指定的。
- exitUntilCollapsed    
exitUntilCollapsed, 当ScrollView 滑出屏幕时（也就时向上滑动时），滑动View先响应滑动事件，滑动至折叠高度，
也就是通过minimum height 设置的最小高度后，就固定不动了，再把滑动事件交给 scrollview 继续滑动。
- snap  
snap,意思是：在滚动结束后，如果view只是部分可见，它将滑动到最近的边界。比如，如果view的底部只有25%可见，它将滚动离开屏幕，而如果底部有75%可见，它将滚动到完全显示。

