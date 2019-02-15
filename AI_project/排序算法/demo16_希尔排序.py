def shell_sort(alist):
    n = len(alist)
    gap = n //2
    while gap>0:
        #改变步长的
        for i in range(gap,n):
            #对不同步长的分组做插入排序
            j = i
            #把下标为j的元素插入到前面的有序序列
            while j>0:
                #下标为j的元素和下标为j-gap的元素在分组中是相邻的
                if alist[j] < alist[j-gap]:
                    alist[j],alist[j-gap] = alist[j - gap],alist[j]
                j -= gap
        #缩小步长
        gap = gap // 2


alist= [34,55,21,66,21,45,78]
shell_sort(alist)
print(alist)






