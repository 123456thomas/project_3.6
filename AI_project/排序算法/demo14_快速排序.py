def quick_sort(alist,start,end):
    #快速排序
    #返回条件
    if start>=end:
        return
    #设定基准值，取列表的起始元素
    mid = alist[start]
    low = start
    high = end
    #遍历序列中所有的元素和基准比较
    while low<high:
        #如果列表后面的元素(high)比基准值大或等，high减1
        #直到找到比基准值小的元素
        while low<high and alist[high] >= mid:
            high -=1
        #把比基准小的元素放到基准值的前面
        alist[low] = alist[high]
        #如果列表前面的元素(low)比基准值小，low加1
        #直到找到比基准值大的元素
        while low<high and alist[low]<mid:
            low +=1
        #把比基准大的元素放到基准值的前面
        alist[high] = alist[low]
    alist[low] = mid
    #对基准值前面的子序列通过递归进行分区操作
    quick_sort(alist,start,low-1)
    #对基准值后面的子序列通过递归进行分区操作
    quick_sort(alist,low+1,end)


ls = [54,33,12,87,34,99,16,88,55]
quick_sort(ls,0,len(ls)-1)
print(ls)