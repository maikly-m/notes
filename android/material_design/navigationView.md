## NavigationView

导航栏

用法：配合DrawerLayout创建导航栏

```
<android.support.v4.widget.DrawerLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">
 
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="#4d7aed">
 
        <TextView
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:gravity="center"
            android:text="这里是一个主页面"
            android:textSize="18sp" />
    </LinearLayout>
 
    <android.support.design.widget.NavigationView
        app:headerLayout="@layout/layout"
        android:layout_width="450dp"
        android:layout_height="match_parent"
        android:layout_gravity="start"
        android:background="#ffffff">
    </android.support.design.widget.NavigationView>
 
</android.support.v4.widget.DrawerLayout>
```