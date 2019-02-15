#双端列表的定义
class Deque(object):
    def __init__(self):
        self.items = []

    def add_front(self,item):
        #从队头加入一个item元素
        self.items.insert(0,item)

    def add_rear(self,item):
        #从队尾加入一个item元素
        self.items.append(item)

    def remove_front(self):
        #从队头删除一个item元素
        return self.items.pop(0)

    def remove_rear(self):
        #从队尾删除一个item元素
        return self.items.pop()

    def is_empty(self):
        #判断双端队列是否为空
        return self.items == []

    def size(self):
        # 返回队列的大小
        return len(self.items)


if __name__ == '__main__':
    deqeue = Deque()
    print(deqeue.is_empty())
    deqeue.add_front(22)
    deqeue.add_front(33)
    deqeue.add_rear(44)
    deqeue.add_rear(55)
    print(deqeue.is_empty())
    print(deqeue.size())
    print(deqeue.remove_front())
    print('size:',deqeue.size())
    print(deqeue.remove_rear())
    print('size:',deqeue.size())
