class Resto:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def add(self, item, priority):
        self.data.append((priority, item))
        self.data.sort()



    def change_priority(self, item, new_priority):
        for i in range(len(self.data)):
            if self.data[i][1] == item:
                self.data[i] = (new_priority, item)
                self.data.sort()
                return
        


    def remove_highest_priority(self):
        del antrian.data[-1]
        
        

    def remove_with_priority(self, priority):
        a = []
        for i in range (len(self.data)):
            if self.data[i][0] == priority:
                a.append(self.data[i])
        for i in a:
            self.data.remove(i)
                
                


    def display(self):
        for priority, item in self.data:
            print(f"Priority: {priority}, Item: {item}")

antrian = Resto()
antrian.add("Pesan Pizza", 2)
antrian.add("Pesan Ayam Goreng", 1)
antrian.add("Pesan Burger", 3)
print("Isi awal Pesanan:")
antrian.display()

print("\nPesanan Ayam Goreng diminta cepat!!!")
antrian.change_priority("Pesan Ayam Goreng", 4)
antrian.display()

print("\n##### PESANAN PERTAMA SELESAI #####\n")
antrian.remove_highest_priority()

print("Sisa pesanan: ")
antrian.display()

print("\nPesanan dengan prioritas ini telah selesai")
antrian.remove_with_priority(2)
antrian.display()