class Node(object):
    #节点的类
    def __init__(self,item):
        self.item = item
        self.prev = None
        self.next = None

class DLinkList(object):
    #双向链表的类
    def __init__(self):
        #指向链表的头节点
        self._head = None

    def is_empty(self):
        #链表是否为空
        return self._head == None


    def length(self):
        # 链表长度
        cur = self._head
        # 计数器
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        #遍历链表
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        #链表头部添加
        node = Node(item)
        if self.is_empty():
            #如果是空链表，将_head指向node
            #给链表添加第一个元素
            self._head = node
        else:
            #如果链表不为空，在新的节点和原来的首节点之间建立双向链接
            node.next = self._head
            self._head.prev = node
            #让_head指向链表的新的首节点
            self._head = node


    def append(self,item):
        #链表尾部添加
        #创建新的节点
        node = Node(item)
        if self.is_empty():
            #空链表，
            self._head = node
        else:
            #链表不为空
            cur = self._head
            while cur.next != None:
                cur = cur.next
            #cur的下一个节点是node
            cur.next = node
            #node的上一个节点是
            node.prev = cur

    def insert(self,pos,item):
        #指定位置添加
        if pos <=0:
            self.add(item)
        elif pos > self.length()-1:
            self.append()
        else:
            node = Node(item)
            cur = self._head
            count = 0
            #把cur移动到指定位置的前一个位置
            while count < (pos - 1):
                count+=1
                cur = cur.next
            #node的prev指向cur
            node.prev = cur
            #node的next指向cur的next
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self,item):
        #删除节点
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                #首节点是要删除的节点
                if cur.next == None:
                    #说明链表中只有一个节点
                    self._head = None
                else:
                    #链表多于一个节点的情况
                    cur.next.prev = None
                    self._head = cur.next
            else:
                # 首节点不是要删除的节点
                while cur != None:
                    if cur.item == item:
                        cur.prev.next = cur.next
                        if  cur.next != None:
                            cur.next.prev = cur.prev
                        break
                    cur = cur.next

    def search(self,item):
        #查找节点是否存在
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    dls = DLinkList()
    dls.add(10)
    dls.add(12)
    dls.append(15)
    dls.append(16)
    dls.insert(2,32)
    dls.insert(3,36)
    print('dls lenght:',dls.length())
    dls.travel()
    print(dls.search(15))
    dls.remove(16)
    print('dls length:',dls.length())
    dls.travel()
