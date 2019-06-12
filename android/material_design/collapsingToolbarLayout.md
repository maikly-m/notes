##  CollapsingToolbarLayout 

用于实现可折叠式标题栏， CollapsingToolbarLayout是不能独立存在的，它必须只能作为AppBarLayout的子布局来使用；

用法：

```
<android.support.design.widget.CoordinatorLayout
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:id="@+id/coordinator_layout"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:fitsSystemWindows="true"
        android:orientation="vertical">


    <android.support.design.widget.AppBarLayout
            android:id="@+id/appBarLayout"
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

        <android.support.design.widget.CollapsingToolbarLayout
                android:id="@+id/collapsingToolbarLayout"
                android:layout_width="match_parent"
                android:layout_height="250dp"
                android:background="@color/colorPrimaryDark"
                app:layout_scrollFlags="scroll|exitUntilCollapsed">
            <ImageView
                    android:fitsSystemWindows="true"
                    android:scaleType="centerCrop"
                    app:layout_collapseMode="parallax"
                    android:src="@mipmap/ic_launcher"
                    android:id="@+id/iv_collapsed"
                    android:layout_width="match_parent"
                    android:layout_height="match_parent"/>

            <android.support.v7.widget.Toolbar
                    android:id="@+id/toolbar"
                    app:title="@string/app_name"
                    android:layout_width="match_parent"
                    android:layout_height="?attr/actionBarSize"
                    app:layout_collapseMode="pin"
                    android:background="@android:color/transparent">

            </android.support.v7.widget.Toolbar>



        </android.support.design.widget.CollapsingToolbarLayout>
    </android.support.design.widget.AppBarLayout>

    <android.support.v7.widget.RecyclerView
            android:id="@+id/recycle_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:layout_behavior="@string/appbar_scrolling_view_behavior"
            android:scrollbars="none"/>

</android.support.design.widget.CoordinatorLayout>
```