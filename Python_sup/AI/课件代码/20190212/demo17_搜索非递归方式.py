def binary_search(alist,item):
    #非递归方式实现二分法的查找
    first = 0
    last = len(alist) - 1
    while first <= last:
        # 中间元素的下标
        midpoint = (first + last) // 2
        # 判断值的大小
        # 拿指定的元素和中间元素进行比较
        if item == alist[midpoint]:
            # 找到要查找的元素
            return True
        elif item < alist[midpoint]:
            # 如果要查找的内容下于中间值，到前面的子序列中查找
            last = midpoint - 1

        else:
            # 如果要查找的内容大于中间值，到后面的子序列中查找
            first = midpoint + 1

    return False


alist = [3,12,22,33,44,45,88]
print(binary_search(alist,22))
print(binary_search(alist,1))
