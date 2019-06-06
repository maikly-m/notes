# JsBridge基本原理
实现原理：通过loadUrl()来加载本地js方法，改变iframe.src的url来触发webViewClient的shouldOverrideUrlLoading()，实现两端的交互；
## 交互流程
在webView中初始化Android端与js交互的参数，包括处理消息的handler集合，处理回调的集合，消息分发的队列等；
同样，在webViewClient的onPageFinished()中加载本地js，初始化本地js，创建发送消息、接收消息、处理消息、接口回调的容器；
webView加载url完毕之后，远端的js和本地的js将合并在一起，远端js将调用本地js注册handler；
- Android调用js       
  通过loadUrl()触发js，在js方法中查找对应的handler，处理完之后改变iframe.src的url，
  触发shouldOverrideUrlLoading()来刷新消息，再次改变iframe.src的url，触发shouldOverrideUrlLoading()来获取data，
  同时获取responseId调用Android端的回调；
- js调用Android       
  通过点击UI元素,触发js方法，调用对应的handler，处理完之后改变iframe.src的url，
  触发shouldOverrideUrlLoading()，然后刷新消息，
  再次改变iframe.src的url，触发shouldOverrideUrlLoading()来获取data，同时获取callbackId来loadUrl(),调用js方法；
  
  
