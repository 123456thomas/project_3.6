def merge_sort(alist):
    #归并排序
    #设置递归返回的条件
    if len(alist) <=1:
        return alist
    #二分分解
    num = len(alist) // 2
    #返回值left和right:有序序列
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    #合并[24] [5]
    return merge(left,right)

def merge(left,right):
    #对left和right子序列进行合并，得到一个更大的有序的序列
    #定义下标指针，对左右两个列表进行操作
    lp = 0
    rp = 0
    #保存合并的结果
    result = []
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    result += left[lp:]
    result += right[rp:]
    return result


alist = [45,55,32,12,6,7,4,66,16]
sortedlist = merge_sort(alist)
print(sortedlist)
