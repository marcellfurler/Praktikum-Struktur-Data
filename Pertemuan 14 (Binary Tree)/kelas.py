# class Node:
#     def __init__(self, data, parent):
#         self._data=data
#         self._parent = parent
#         self._left=None
#         self._right=None

#     def insert(self, data):
#         if self._data>data:
#             if self._left is None:
#                 self.left=Node(data, self)
#             else:
#                 self.left.insert(data)
#         elif self._data < data:
#             pass

#     def left(self):
#         return self._left

#     def right (self):
#         return self._right

#     def parent(self):
#         return self._parent

#     def isRoot(self):
#         return self._parent is None

#     def isExternal(self):
#         return self._left is None and self._right is None

# class BST:
#     def __init__(self):
#         self.root=None

#     def add(self, data):
#         if self.root==None:
#             self.root=Node(data, None)
#             self.size+=1
#         else:
#             pass

#     def inOrder(self, data):
#         pass

#     def bfs():
#         pass

#     def binarySearch(self, node, value):
#         if node is None or node.operatir()== value:
#             return node
#         elif value<node.operator():
#             return self.binarySearch(node.left(), value)
#         else:
#             return self.binarySearch(node.right(), value)
        
#     def search(self, value):
#         return self.binarySearch(self._root, value) is not None




