from Node import Node

class TreeAnother:
    def __init__(self)-> None:
        self._root =None

    def depth(self, node):
        if node.isRoot():
            return 0
        else:
            return 1 + self.depth(node.parent())
        
    def preOrder(self, node):
        print(node.operaor(), end = " ")
        for i in node.children():
            self.preOrder(i)

    def postOrder(self, node):
        for i in node.children():
            self.postOrder(i)
        print(node.operator(), end = " ")
        
mytree=TreeAnother()
root=Node(10, None)
a=Node(12, root)
a=Node(12, root)
b=Node(20,root)
c=Node(50, a)
d=Node(3,b)
e=Node(30, a)
f=Node(8,b)


root.addChildren(a)
root.addChildren(b)
b.addChildren(d)
a.addChildren(c)

print(mytree.depth(a))

mytree.preOrder(root)
mytree.postOrder(root)
