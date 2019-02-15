def select_sort(alist):
    #选择排序
    n = len(alist)
    for i in range(n):#i表示挑选最小值的次数
        min_index= i
        #从无序的序列中找出最小的元素
        for j in range(i,n):
            if (alist[j]<alist[min_index]):
                min_index = j
        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]

ls = [32,54,22,33,8,66,11]
select_sort(ls)
print(ls)
