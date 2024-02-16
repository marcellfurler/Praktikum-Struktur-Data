# class Node:
#     def __init__(self, data,parent):
#         self._data=data
#         self._parent=parent
#         self._children=[]

#     def addChildren(self, data):
#         self._children.append(data)

#     def operator(self):
#         return self._data

#     def parent(self):
#         return self._parent

#     def children(self):
#         return self._children

#     def isRoot(self):
#         return self._parent is None

#     def isExternal(self):
#         return len(self._children)==0
    
# # root untuk menambahkan cabang baru
    

# root=Node(10,None)
# a=Node(12, root)
# b=Node(20,root)
# c=Node(50, a)
# d=Node(3,b)
# e=Node(30, a)
# f=Node(8,b)

# a.addChildren(c)
# a.addChildren(d)
# a.addChildren(e)
# b.addChildren(f)
# root.addChildren(a)
# root.addChildren(b)

# print(d.operator())
# print(e.parent().operator())
# for i in a.children():
#     print(i.operator(), end = " ")


a=[1,2]
print(sum(a))
