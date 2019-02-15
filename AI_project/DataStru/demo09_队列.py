class Queue(object):
    #队列的实现
    def __init__(self):
        self.items = []

    def is_empty(self):
        #判断队列是否为空
        return self.items == []

    def enqueue(self,item):
        #插入到队列的头部
        self.items.insert(0,item)

    def dequeue(self):
        #删除数据,若超出范围会报错
        return self.items.pop()

    def size(self):
        #返回队列的大小
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue("hello")
    q.enqueue("sssss")
    q.enqueue("aaaaa")
    print(q.size())
    print(q.is_empty())
    print(q.dequeue())
    print(q.size())
    print(q.dequeue())
    print(q.size())

