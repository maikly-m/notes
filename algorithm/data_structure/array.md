# 数组
数组

数组是最简单、也是使用最广泛的数据结构。栈、队列等其他数据结构均由数组演变而来。下图是一个包含元素（1，2，3和4）的简单数组，数组长度为4。

每个数据元素都关联一个正数值，我们称之为索引，它表明数组中每个元素所在的位置。大部分语言将初始索引定义为零。

类型：

一维数组（如上所示）
多维数组（数组的数组）

数组的基本操作

Insert——在指定索引位置插入一个元素       
Get——返回指定索引位置的元素        
Delete——删除指定索引位置的元素     
Size——得到数组所有元素的数量       

面试中关于数组的常见问题

- 寻找数组中第二小的元素 

    实现方式:
  -  使用排序算法，快排、堆排、归并等都可以实现，快排复杂度是O(nlogn)；
  -  扫描两次，第一次寻找最小值，第二次寻找第二小的值，复杂度为O(2n)；
  -  一次扫描两个，每次保留最小的两个值，遍历的时候都做比较，只要比这两个小就替换复杂度O(n)；
     ```
     public static void main (String[] args) {
        int[] array = {32, 1, 7, 4, -9, 23, 0, 34, 93, -1, 3, 2, 66, 34, -5, 10};
        //寻找最小的第二值
        int min_first = 0;
        int min_second = 0;
        if (array[0] > array[1]){
            min_second = array[0];
            min_first = array[1];
        } else{
            min_second = array[1];
            min_first = array[0];
        }
        for (int i = 2; i < array.length; i++){
            if (array[i] >= min_second){
                //比第二小的大，不用处理
            } else{
                if (array[i] < min_first){
                    //比最小的还小，更换
                    min_second = min_first;
                    min_first = array[i];
                } else{
                    //比第二小的小
                    min_second = array[i];
                }
            }
        }
        System.out.println("min_second -> "+min_second);
     }
     ```
- 找到数组中第一个不重复出现的整数
  -  hashMap过滤法：
     扫描一遍数组，将数值作为key，次数作为value存入map中；       
     ```
     public static void main (String[] args) {
        //找到数组中第一个不重复出现的整数
        //HashMap过滤, HashSet过滤会增加算法复杂度
        int[]  ints = {12, 56, 48, 2, 45, 56, 8, 55, 332, 44, 56, 12, 456, 75, 61, 48, 34, 26, 45};
        HashMap map = new HashMap<Integer, Integer>(ints.length);
        int flag = ((1 << 16) - 1) << 16;
        for (int i = 0; i < ints.length; i++){
            Object o = map.get(ints[i]);
            //高16位作为位置标记符，第一次出现的时候做好标记;低16位作为次数标记
            if (o == null){
                //添加
                int value = (i + 1) << 16 | 1;
                map.put(ints[i], value);
            }else {
                int temp = (Integer)o;
                //替换
                temp = (temp & flag) | ((temp >> 16) + 1);
                map.put(ints[i], temp);
            }
        }
        int position = Integer.MAX_VALUE;//出现的位置
        for (Object o: map.values()){
            Integer i = (Integer) o;
            int value = (i >> 16);//获取高位
            int count = i & ((1 << 16) - 1);//获取低位
            if (count == 1){
                //比较位置
                position = position > value ? value : position;
            }
        }
        System.out.println("position  -> "+ position);
     }
     
     ```
  - 数组方式： 
    ```
    public static void main (String[] args){
        //找到数组中第一个不重复出现的整数
        int[]  ints = {12, -1, 56, 48, 2, 45, 56, 8, 55, 332, 44, 56, 12, 456, 75, 61, 48, 34, 26, 45};
        int[]  array = new int[ints.length];
        int replace = -1;//去重flag,不能为0
        int count = 0;
        int index = 0;
        int value = 0;
        for (int i = 0; i < ints.length; i++){
            //赋值
            for (int j = 0; j < i+1; j++){
                if (array[j] == replace){
                    continue;
                }
                if (array[j] == ints[i]){
                    array[j] = replace;
                    array[i] = replace;
                    break;
                }
                if (j == i){
                    array[i] = ints[i];
                }
            }
            if (ints[i] == replace){
                count++;
                if (count == 1){
                    index = i;
                    value = ints[i];
                }
            }
        }
        for (int i = 0; i < array.length; i++){
            if (array[i] != replace){
                if (count == 1){
                    if (index > i){
                        index = i;
                        value = array[i];
                    }
                }else {
                    index = i;
                    value = array[i];
                }
                break;
            }
        }

        System.out.println("index -> "+index);
        System.out.println("value -> "+value);
    }
    ```
- 合并两个有序数组
  - 归并排序，需要额外的空间，通过空间换时间；
    ``` 
    public static void main (String[] args) {
        int[] a = {1, 5, 10, 11, 12, 18 , 21};
        int[] b = {2, 5, 6, 8, 13, 16, 19, 22, 45, 77};
        int[] c = new int[a.length+b.length];

        int m = 0, i = 0, j = 0;
        while (i < a.length && j < b.length) {
            c[m++] = a[i] < b[j] ? a[i++] : b[j++];
        }
        while (i < a.length)
            c[m++] = a[i++];
        while (j < b.length)
            c[m++] = b[j++];
        System.out.println("c ->");
        for (int k = 0; k < c.length; k++){
            System.out.print(" "+c[k]);
        }

    }
    ```
- 重新排列数组中的正值和负值