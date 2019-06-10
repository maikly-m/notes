## 堆
- 大小顶堆：     
  堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。
  
  `构建大顶堆：`        
  [参考堆排序建立大顶堆 ](../堆排序.md) 
  
  `堆的插入：`      
  堆的插入用的方法我们称其为向上调整法，因为我们在往堆里插入元素时，我们把元素插入在堆尾，因此，调整就要从堆尾开始，
  自底向上的把堆尾这个元素提到其合适的位置，也是非常形象，其过程就是相当于把向下调整法反过来了，思想是一样的
  
  ```
   private static int[] insert (int a, int[] arr) {
        int[] ints = new int[arr.length + 1];
        System.arraycopy(arr, 0, ints, 0, arr.length);
        ints[arr.length] = a;
        arr = ints;

        int parent = arr.length / 2 - 1;
        //只需要调整最后一个，向上调整
        int left = parent * 2 + 1;
        while (left >= 0){
            //从最后一个非叶子结点从下至上，从右至左调整结构
            parent = (left - 1) / 2;
            //存在右节点
            if (left + 1 < arr.length && arr[left] < arr[left + 1]){
                //右节点比左节点大
                //指向右节点
                left++;
            }
            if (arr[left] > arr[parent]){
                //节点比父节点要大
                int temp = arr[parent];
                arr[parent] = arr[left];
                arr[left] = temp;
            } else{
                break;
            }
            //向上寻找
            left = parent;
        }

        return arr;
    }
  ```
  
  
- top k 问题：

    最直观：小顶堆（大顶堆 -> 最小100个数）；
    较高效：Quick Select算法。