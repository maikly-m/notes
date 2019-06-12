## UI渲染

Android系统每隔16ms就会重新绘制一次Activity，因此，我们的应用必须在16ms内完成屏幕刷新的全部逻辑操作，
每一帧只能停留16ms，否则就会出现掉帧现象(也就是用户看到的卡顿现象)。

### UI渲染卡顿

我们知道，对于APP的每一个View，Android系统都会通过三个步骤来渲染：Measure（测量）、Layout（布局）和Draw（绘制）。
measure从最顶部的节点开始，顺着layout树形结构依次往下测量每个view需要在屏幕中展示的尺寸大小。
每个子节点都需要向父节点提供自己的尺寸来决定展示的位置，遇到冲突时，父节点可以强制子节点重新measure（可能导致时间消耗为原来的2-3倍）。
因此扁平化的view结构会性能更好。

RelativeLayouts经常需要measure所有子节点两次才能把子节点合理的布局。如果子节点设置了weights属性，
LinearLayouts也需要measure这些节点两次，才能获得精确的展示尺寸。如果LinearLayouts或者RelativeLayouts被套嵌使用，
measure所费时间可能会呈指数级增长。

一旦view开始被measure，该view所有的子view都会被重新layout，
再把该view传递给它的父view，如此重复一直到最顶部的根view。layout完成之后，所有的view都被渲染到屏幕上。
需要特别注意到是，并不是只有用户看得见的view才会被渲染，所有的view都会。APP拥有的views越多，measure，layout，draw所花费的时间就越久。
要缩短这个时间，关键是保持view的树形结构尽量扁平，而且要移除所有不需要渲染的view。
移除这些view会对加速屏幕渲染产生明显的效果。理想情况下，总共的measure，layout，draw时间应该被很好的控制在16ms以内，以保证滑动屏幕时UI的流畅。

### UI渲染优化

- 过度绘制(overdraw)    
  屏幕上的某个项目在同一帧内被绘制了多次。在多层次的UI结构里面，如果不可见的UI也在做绘制的操作，
  这就会导致某些像素区域内绘制了多次，这就浪费了大量的CPU以及GPU资源。     
  优化：   
  1.去掉window的默认背景     
  2.去掉其他不必要的背景     
  3.画布的clipRect使用     
  4.ViewStub和Merge标签的使用
  
- view的层级和结构需要调整，减少view重绘的时间