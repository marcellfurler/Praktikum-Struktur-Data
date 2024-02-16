# class Stack:
#     def __init__(self):
#         self._container=[]

#     def pop(self, data):
#         if len(self._container)==0:
#             return None
#         self._container.pop(data)

#     def top(self, data):
#         if len(self._container) ==0:
#             return None

#     def push(self,data):
#         self._container.append(data)

#     def printAll(self):
#         for i in self._container:
#             print(i)
#         self._container.reverse


# if __name__ =="__main__":
#     stack=Stack()
#     stack.push(10)
#     stack.push(30)
#     stack.push(50)
#     stack.pop(2)
#     # stack.pop()

#     print(stack._container)
#     # stack.printAll()




# Stack dengan linked list

class Node:
    def __init__(self,elemen,n):
        self._element = elemen
        self._next = n

class Stack :
    def __init__(self):
        self._head=None
        self._seize=0
    
    def __len__(self):
        return self.__size
    def isEmpty(self):
        return self._size==0
    def push(self, e):
        baru=Node(e, None)
        if self.isEmpty==baru:
            self._head=baru
            self._tail=baru
            self._tail._next=None
        else:
            baru._next = self._head
            self._head = baru
        self._size +=1
        print('data masuk ke stack')

    def top(self):
        if self.isEmpty==True:
            return 'stack kosong'
        else:
            return self._head._elemen
        
    def pop(self):
        if self.isEmpty()==False:
            d=""
            if self._head._next==None:
                d=self._head._elemen
                self._head=None
            else:
                hapus=self._head
                d=hapus._elemen
                self._head=self._head._next
                hapus._next=None
            del hapus
            self._size -=1
            print(d, "dihapus")
        else:
            print("stack kosong")
        return d
    
    def prinAll(self):
        if self.isEmpty()==False:
            bantu=self._head
            while(bantu !=None):
                print(bantu._elemen, " ",end=" ")
                bantu=bantu._next
                print()
        else:
            print("kosong")


mystack = Stack()
mystack.push("3")
mystack.push("2")
mystack.push("1")
mystack.printAll()
mystack.pop()
mystack.printAll()
mystack.pop()
mystack.printAll()

