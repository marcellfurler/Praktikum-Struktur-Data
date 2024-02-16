# class Node:
#     def __init__(self, element, n):
#         self._element=element
#         self._next=n

# class SLINC:
#     def __init__(self):
#         self._head=None
#         self._tail=None
#         self._size=0

#     def __len__(self):
#         return self._size
    
#     def isEmpty(self):
#         return self._size==0
    
    

class NodeBasic:
    def __init__(self, element, next=None):
        self._element=element
        self._next=next
        