import math

class Node:
    def __init__(self, value):
        self.next = None
        self.data = value

class SLNC:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getLength(self):
        return self.size

    def writeAllData(self):
        if self.size == 0:
            result = 'Linked list kosong'
        else:
            result = 'Linked List: ' + str(self.size) + ' data: \n'
            helper = self.head
            while helper != None:
                result = result + str(helper.data) + ' '
                helper = helper.next
        print(result)

    # methods
    def insert_head(self, new_data):
        node_baru = Node(new_data)
        if self.size == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            node_baru.next = self.head
            self.head = node_baru
        self.size = self.size + 1
    
    def insert_tail(self, new_data):
        node_baru = Node(new_data)
        if self.size == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru

        self.size = self.size + 1
    
    def insert_mid(self, new_data, index):
        if self.size == 0 or index <= 0:
            self.insert_head(new_data)
        elif index >= self.size:
            self.insert_tail(new_data)
        else:
            node_baru = Node(new_data)
            helper = self.head
            for i in range(index-1):
                helper = helper.next
            node_baru.next = helper.next
            helper.next = node_baru
            self.size = self.size + 1
    def delete_head(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return deleted_node
        else:
            hapus = self.head
            deleted_node = self.head
            self.head = self.head.next
            del hapus
            self.size = self.size - 1
            return deleted_node
            
    def delete_tail(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return deleted_node
        else:
            helper = self.head
            while helper.next != self.tail:
                helper = helper.next
            hapus = self.tail
            deleted_node = self.tail
            self.tail = helper
            self.tail.next = None
            del hapus
            self.size = self.size - 1
            return deleted_node

    def delete_mid(self, index):
        if self.size == 0 or index <= 0:
            return self.delete_head()
        elif index >= self.size-1:
            return self.delete_tail()  
        else:
            helper = self.head
            for i in range(index-1):
                helper = helper.next
            hapus = helper.next
            helper.next = hapus.next
            deleted_node = hapus
            del hapus
            self.size = self.size - 1
            return deleted_node
        



    # def max(self, data, start, end, max_value):
    #     if start == end:
    #         max_value=data[start]
    #         return max_value
    #     elif start==end-1:
    #         if data[start]>data[end]:
    #             max_value = data[start]
    #             return max_value
    #         else:
    #             max_value=data[end]
    #             return max_value
    #     else:
    #         mid=(start+end)//2
    #         left_max = max(data, start, mid, max_value)
    #         right_max=max(data, mid+1, end, max_value)
    #         if left_max>right_max:
    #             return left_max
    #         else:
    #             return right_max
    def quicksort(data, start, end):
        if start<end:
            pivot_index=partition(data, start, end)
            quicksort(data, start, pivot_index-1)
            quicksort(data, pivot_index+1, end)

    def partition(data, start, end):
        pivot=data[end]
        left=start
        right=end-1
        while left<=right:
            while data[left]<pivot:
                left+=1
            while data[right]>pivot:
                right-=1
            if left<=right:
                data[left], data[right]=data[right], data[left]
                left+=1
                right-=1
        data[left], data[end]=data[end], data[left]
        return left

    """
    Method getData(self, index) akan mereturn data dari linked list berdasarkan
    parameter index. Cara kerjanya hampir sama seperti index pada
    list biasa.
    """
    def getData(self, index) :
        if index<0 or index >=self.getLength():
            return None
        indexx=self.head
        indexx = indexx.next
        return indexx.data


    def hapusDuplikasi(self):
        # if self.size <=1:
        #     return
        indexx=self.head
        while indexx:
            data=indexx.data
            codes=indexx
            while codes.next:
                if codes.next.data==data:
                    codes.next=codes.next.next
                    self.size=self.size-1
                else:
                    codes=codes.next
            indexx=indexx.next


if __name__ == "__main__":
    ll = SLNC()
    for i in [1, 1, 1, 1, 1, 2, 3, 4, 2, 2, 2, 5, 7,7,8,8,45,20, 20]:
        ll.insert_tail(i)
    ll.max(i, 0, len(i)-1, -math.inf)
    ll.writeAllData()
    ll.hapusDuplikasi()
    ll.writeAllData()
    print(ll.getData(1))
