class Node:
    def __init__(self, data, priority):
        self._data=data
        self._priority=priority
        self._next=None

class PriorityQueueUnsorted:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def is_Empty(self):
        if self._size==0:
            return True
        else:
            return False
        
    def __len__(self):
        return self._size
    
    def print_all(self):
        if self.is_Empty()==True:
            print("Priority Queue is empty")
        else:
            helpen=self._head
            while helpen != None:
                print("(", helpen._data, ",", helpen._priority, ")", end=" ")
                helpen=helpen._next
        print()

    def add(self, data, priority):
        new=Node(data, priority)
        if self.is_Empty():
            self._head=new
            self._tail=new
        else:
            self._tail._next=new
            self._tail=new
        self._size=self._size+1

    def remove(self):
        if self.is_Empty()==False:
            if self._size==1:
                helpen=self._head
                self._head=None
                self._tail=None
                del helpen
            else:
                min_priority=self._head._priority
                hapus=self._head
                while hapus!=None:
                    if hapus._priority<min_priority:
                        min_priority=hapus._priority
                    hapus=hapus._next
                hapus=self._head
                while hapus._priority!=min_priority:
                    hapus=hapus._next
                if hapus==self._head:
                    self._head=self._head._next
                    del hapus
                else:
                    helpen=self._head
                    while helpen._next!=hapus:
                        helpen=helpen._next
                    helpen._next=hapus._next
                    del hapus
                    self._tail=self._head
                    while self._tail._next!=None:
                        self._tail=self._tail._next
                self._size=self._size-1

    def peek(self):
        if self.is_Empty()==True:
            return None
        else:
            if self._size==1:
                return tuple([self._head._data, self._head._priority])
            else:
                min_priority=self._head._priority
                helpen=self._head
                while helpen!=None:
                    if helpen._priority<min_priority:
                        min_priority=helpen._priority
                    helpen=helpen._next
                helpen=self._head
                while helpen._priority!=min_priority:
                    helpen=helpen._next
                return tuple([helpen._data, helpen._priority])
            
queueTest=PriorityQueueUnsorted()
queueTest.add("Amber", 5)
queueTest.add("Diluc", 1)
queueTest.add("Beidou", 3)
queueTest.add("Kaeya", 4)
queueTest.print_all()
data, priority=queueTest.peek()
print(data)
print(priority)
queueTest.remove()
queueTest.print_all()
queueTest.remove()
queueTest.print_all()
queueTest.remove()
queueTest.print_all()



