class PriorityQueueSorted:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0
    
    
    def len(self):
        return len(self)

    def remove(self):
        if len(self.data)==0:
            return
        else:
            return self.data.pop(0)
        

    

    def peek(self):
        if not self.is_empty():
            print(self.data[0][0])
            return self.data[0][0]
        else:
            return None
        
    
        
        
    def add(self, data, priority):
        item=(data, priority)

        self.data.append(item)
        self.merge_sort(self.data)

    def merge_sort(self,data):
        if len(data)>1:
            mid=len(data)//2
            left=data[:mid]
            right=data[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            
            i=0
            j=0
            k=0

            while i<len(left) and j<len(right):
                if left[i][1]>=right[j][1]:
                    data[k]=left[i]
                    i+=1
                else:
                    data[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                data[k]=left[i]
                i+=1
                k+=1

            while j<len(right):
                data[k]=right[j]
                j+=1
                k+=1

    def print_all(self):
        for i in (self.data):
            print(i)


myQueue = PriorityQueueSorted()
myQueue.add('Gian', 2)
myQueue.add('Kezia', 8)
print()
myQueue.print_all()
myQueue.peek()
myQueue.add('Glen', 5)
myQueue.add('Christo', 9)
print()
myQueue.print_all()
myQueue.peek()
print("========REMOVE========")
myQueue.remove()
print()
myQueue.print_all()
myQueue.remove()
print()
myQueue.print_all()
myQueue.remove()
print()
myQueue.print_all()
print()
myQueue.add('Saya', 7)
myQueue.print_all()
