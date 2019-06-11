## toolbar

Google于2015年引入Material Design风格的控件，Android SDK中的ActionBar每个版本都会做一些改变, 
所以在不同的系统上看起来可能会不一样，导致严重的碎片化问题，于是谷歌在更新android-support-v7兼容包时引入了ToolBar，
用来替代ActionBar，它推荐开发者使用兼容包中的ToolBar，而非SDK中的ActionBar，以期解决碎片化问题。

`toolbar使用：`

在代码中替换掉actionBar，添加toolBar后，可以自定义返回icon，title和子title，弹出的item；toolbar继承viewGroup，所有添加的子view都可以在
设置的回调方法中处理监听事件；

测试Activity
```
class ToolbarActivity: AppCompatActivity(){

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_toolbar)
        //替换为toolbar
        toolbar.title = "title"
        setSupportActionBar(toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        toolbar.setNavigationOnClickListener {
            finish()
        }
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_toolbar, menu)
        return super.onCreateOptionsMenu(menu)
    }

    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        when(item?.itemId){
            R.id.tv_test0 ->
                Toast.makeText(this,"tv_test0", Toast.LENGTH_SHORT).show()
            R.id.tv_test1 ->
                Toast.makeText(this,"tv_test1", Toast.LENGTH_SHORT).show()
            else -> {}
        }
        return super.onOptionsItemSelected(item)
    }

    override fun onMenuOpened(featureId: Int, menu: Menu?): Boolean {
        return super.onMenuOpened(featureId, menu)
    }

    override fun openOptionsMenu() {
        Toast.makeText(this,"openOptionsMenu", Toast.LENGTH_SHORT).show()
        super.openOptionsMenu()
    }

    override fun closeOptionsMenu() {
        Toast.makeText(this,"closeOptionsMenu", Toast.LENGTH_SHORT).show()
        super.closeOptionsMenu()
    }
}
```

布局文件 
```
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        tools:context=".ToolbarActivity">
    <android.support.v7.widget.Toolbar
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toTopOf="parent"
            android:id="@+id/toolbar"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:background="@color/colorAccent"
            android:theme="@style/ToolBarPopupThem"
            android:minHeight="?attr/actionBarSize" />

    <TextView
            android:id="@+id/tv"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Hello World!"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toTopOf="parent"/>

</android.support.constraint.ConstraintLayout>
```

主题文件 
```
 <style name="AppThemeToolbar" parent="AppTheme">
        <item name="windowActionBar">false</item>
        <item name="windowNoTitle">true</item>
    </style>

    <style name="ToolBarPopupThem" parent="Widget.AppCompat.Light.PopupMenu.Overflow">
        <!-- 设置popupMenu背景颜色-->
        <item name="android:colorBackground">@color/colorPrimary</item>
        <!--设置popupMenu弹出位置不覆盖toolbar -->
        <item name="overlapAnchor">false</item>
        <!-- 修改字体大小 -->
        <item name="android:textSize">15sp</item>
        <!-- 修改字体颜色 -->
        <item name="android:textColor">#fff</item>
    </style>
```

items文件 
```
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
            android:icon="@mipmap/ic_launcher"
            android:id="@+id/tv_test0"
            android:title="测试按钮0" />
    <item
            android:icon="@mipmap/ic_launcher"
            android:id="@+id/tv_test1"
            android:title="测试按钮1" />
</menu>
```