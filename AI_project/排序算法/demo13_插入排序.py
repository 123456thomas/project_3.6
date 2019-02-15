def insert_sort(alist):
    #插入排序
    n = len(alist)
    for i in range(1,n):# i表示插入的次数
        for j in range(i,-1,-1):
            if alist[j] > alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]


ls = [32,54,22,33,8,66,11]
insert_sort(ls)
print(ls)