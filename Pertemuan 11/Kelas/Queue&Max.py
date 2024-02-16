import math

class Queue :
    def __init__(self):
        self.data = []
    
    def enqueue(self, data) :
        self.data.append(data)

    def dequeue(self):
        if len(self.data) == 0:
            return
        else :
            return self.data.pop(0)

    def front(self):
        if len(self.data) == 0 :
            return 
        else :
            return self.data[0]
    
    def get_length(self) :
        return len(self.data)

    def write_all_data(self):
        print("DATA: ")
        for i, data in enumerate(self.data):
            print(f"{data}")



# Haram untuk menggunakan list
def get_min(queue):
    q=Queue()
    minus1=queue.front()
    for i in range(queue.get_length()):
        minus2=queue.dequeue()
        q.enqueue(minus2)
        if minus2<minus1:
            minus1=minus2
    for i in range(q.get_length()):
        queue.enqueue(q.dequeue())
    return minus1
        
    
        
def pop(queue):
    data=Queue()
    none=None
    while queue.get_length()>0:
        data2=queue.front()
        if queue.get_length()==1:
            none=data2
        else:
            data.enqueue(data2)
        queue.dequeue()
    while data.get_length()>0:
        queue.enqueue(data.front())
        data.dequeue()
    return none


# def max(data, start, end, max_value):
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

    

if __name__ == "__main__":
    q : Queue = Queue()
    for i in [10, 8, 5, 60,1,2,3,4,100]:
        q.enqueue(i)
    print("==========")
    print("Data Awal")
    q.write_all_data()
    print("==========")
    print(f"Data terkecil = {get_min(q)}")
    print("==========")
    print()
    print("Pembuktian isi queue tidak berubah")
    print("==========")
    print("Data Akhir")
    q.write_all_data()
    print("==========")
    print()
    print("============")
    print("Percobaan Pop")
    print(f"pop - 1 = {pop(q)}")
    print(f"pop - 2 = {pop(q)}")
    print(f"pop - 3 = {pop(q)}")
    print("=============")
    print("Hasil Akhir: ")
    q.write_all_data()
    print("=============")