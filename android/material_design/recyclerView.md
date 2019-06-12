## RecyclerView

简单用法：

```
class CoordinatorLayoutActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_coordinatorlayout)
        init()
    }

    private fun init() {
        //替换为toolbar
        toolbar.title = "title"
        setSupportActionBar(toolbar)

        val list = mutableListOf<String>()
        for (i in 1..30) {
            list.add("test_$i")
        }

        recycle_view.layoutManager = LinearLayoutManager(this)
        TestAdapter(list, this).let {
            recycle_view.adapter = it
        }

    }

}

class TestAdapter(val list: List<String>, val context: Context) : RecyclerView.Adapter<VH>() {
    override fun onCreateViewHolder(p0: ViewGroup, p1: Int): VH {
        View.inflate(context, R.layout.recyclerview_item, null).let {
            VH(it).let { vh ->
                return vh
            }
        }
    }

    override fun getItemCount(): Int {
        return list.size
    }

    override fun onBindViewHolder(p0: VH, p1: Int) {
        list[p1].let {
            p0.tv.text = it
        }
    }

    init {

    }

}

class VH(itemView: View) : RecyclerView.ViewHolder(itemView) {
    val tv: TextView = itemView.findViewById(R.id.tv)
}
```

`additional：`

- 实现多类型的列表：

在RecyclerView中，我们可以重写方法getItemViewType()，这个方法会传进一个参数position表示当前是第几个Item，
然后我们可以通过position拿到当前的Item对象，然后判断这个item对象需要那种视图，返回一个int类型的视图标志，
然后在onCreateViewHolder方法中给引入布局；

- 可以实现局部刷新数据，列表操作的动画，嵌套滚动效果