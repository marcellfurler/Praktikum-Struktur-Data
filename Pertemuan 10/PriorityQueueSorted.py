class Node:
    def __init__(self, data, priority):
        self._data=data
        self._priority=priority
        self._next=None
        self._prev=None

class PriorityQueueSorted:
    def __init__(self) :
        self._head=None
        self._tail=None
        self._size=0

    def is_empty(self):
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
                

    def remove(self):
        if self.is_empty()==False:
            hapus=self._head
            if self._size==1:
                self._head=None
            else:
                self._head=self._head._next
                self._head._prev=None
            del hapus
            self._size=self._size-1

    def peek(self):
        if self.is_empty()==True:
            return None
        else:
            return tuple([self._head._data, self._head._priority])
        
    def add(self, data, priority):
        new=Node(data, priority)
        if self.is_empty():
            self._head = new
            self._tail = new
        elif self._size==1:
            if self._head._priority>priority:
                new._next=self._head
                self._head._prev=new
                self._head=new
            else:
                self._head._next=new
                new._prev=self._head
                self._tail=new
        else:
            if self._head._priority>priority:
                new._next=self._head
                self._head._prev=new
                self._head=new
            elif self._tail._priority<=priority:
                self._tail._next=new
                new._prev=self._tail
                self._tail=new
                self._tail._next=None
            else:
                helpen=self._head
                while helpen._priority<priority:
                    helpen=helpen._next
                helpenen=helpen._prev
                new._next=helpen
                helpen._prev=new
                helpenen._next=new
                new._prev=helpenen
        self._size=self._size+1


queueTestSoreted=PriorityQueueSorted()
queueTestSoreted.add("Amber", 5)
queueTestSoreted.add("Diluc", 1)
queueTestSoreted.print_all()
queueTestSoreted.add("Beidou", 3)
queueTestSoreted.add("Kaeya", 4)
queueTestSoreted.print_all()
data, priority=queueTestSoreted.peek()
print(data)
print(priority)
queueTestSoreted.remove()
queueTestSoreted.print_all()
queueTestSoreted.remove()
queueTestSoreted.print_all()
queueTestSoreted.remove()
queueTestSoreted.print_all()
queueTestSoreted.remove()
queueTestSoreted.add("Venti", 1)
queueTestSoreted.remove()
queueTestSoreted.print_all()


            