def binary_search(alist,item):
    #递归方式实现二分法的查找
    #设置递归退出的条件
    if len(alist) == 0:
        return False
    else:
        #确定中间值
        midpoint = len(alist) // 2
        # 拿指定的元素和中间元素进行比较
        if item == alist[midpoint]:
            # 找到要查找的元素
            return True
        elif item < alist[midpoint]:
            # 如果要查找的内容下于中间值，到前面的子序列中查找
            return binary_search(alist[:midpoint],item)

        else:
            # 如果要查找的内容大于中间值，到后面的子序列中查找
            return binary_search(alist[midpoint+1:],item)




alist = [3,12,22,33,44,45,88]
print(binary_search(alist,22))
print(binary_search(alist,1))
