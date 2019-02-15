def bubble_sort(alist):
    #冒泡排序
    n = len(alist)
    for j in range(n-1,0,-1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

ls = [32,54,22,33,8,66,11]
bubble_sort(ls)
print(ls)
