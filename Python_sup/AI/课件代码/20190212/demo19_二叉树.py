class Node(object):
    #树的结点
    def __init__(self,elem=-1,lchild=None,rchild=None):
        #结点的数据部分
        self.elem = elem
        # 左子树
        self.lchild = lchild
        #右子树
        self.rchild = rchild


class Tree(object):
    #定义树类
    def __init__(self,root=None):
        self.root = root

    #给树添加结点的方法
    def add(self,elem):
        #生成一个结点的对象
        node = Node(elem)
        #把结点添加到树上
        #如果树为空，对根结点直接赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            #把需要判断的节点放入一个列表
            #把根结点放入列表中
            queue.append(self.root)
            while queue:
                #弹出列表的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preoader(self,root):
        #先序遍历
        if root == None:
            return
        #访问根结点
        print(root.elem)
        #通过递归，访问左子树
        self.preoader(root.lchild)
        #通过递归，访问右子树
        self.preoader(root.rchild)

    def inorder(self,root):
        #中序遍历
        if root == None:
            return
        # 通过递归，访问左子树
        self.inorder(root.lchild)
        # 访问根结点
        print(root.elem)
        # 通过递归，访问右子树
        self.preoader(root.rchild)

    def postorder(self,root):
        #后续遍历
        if root == None:
            return
        # 通过递归，访问左子树
        self.postorder(root.lchild)
        # 通过递归，访问右子树
        self.postorder(root.rchild)
        # 访问根结点
        print(root.elem)

if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        #给树添加结点
        t.add(i)
    #前序遍历
    #t.preoader(t.root)
    #中序遍历
    #t.inorder(t.root)
    #后续遍历
    t.postorder(t.root)
