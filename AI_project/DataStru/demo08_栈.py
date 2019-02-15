class Stack(object):
    #栈的实现
    def __init__(self):
        self.items = []

    def is_empty(self):
        #判断栈是否为空
        return self.items == []

    def push(self,item):
        #压栈：在栈中加入数据元素
        self.items.append(item)

    def pop(self):
        #弹栈操作：从栈中弹出元素,若栈为空，返回None
        if self.is_empty():
            pass
        else:
            return self.items.pop()

    def peek(self):
        #返回栈顶的数据元素，防止空栈报错
        if self.is_empty():
            pass
        else:
            return self.items[len(self.items)-1]

    def size(self):
        #返回栈的尺寸
        return len(self.items)

if __name__ == '__main__':
    stack = Stack()
    print(stack.peek())
    print(stack.is_empty())
    stack.push('hello')
    stack.push('python')
    stack.push('qiku')
    stack.push('zhengzhou')
    print(stack.is_empty())
    print(stack.items)
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.items)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

