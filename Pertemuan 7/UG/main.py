class Stack:
    def __init__(self):
        self._size = 0
        self._data = []
    def getLen(self):
        return self._size
    def top(self):
        if self._size == 0 :
            return None
        return self._data[-1]
    def pop(self):
        if self._size == 0:
            return None
        self._size-=1
        return self._data.pop()
    def push(self, data):
        self._data.append(data)
        self._size+= 1
    def printData(self):
        for i in range(1, self._size+1):
            print(self._data[-i])

# Peringatan! Tidak boleh mengakses variabel stack secara langsung!
# Anda hanya boleh berinteraksi dengan stack dengan menggunakan method
# top, pop, push, printData dan getLen (tidak boleh mengakses langsung _size dan _data).
# Jika nekat akan dibagi 2 nilainya 
def printDataPertama(stack: Stack) :
        datalist=[]
        for i in range(s.getLen()):
            datalist.append(s.top())
            s.pop()
        print(datalist[-1])

        datalist.reverse()
        for i in datalist:
            s.push(i)

        
            
    

if __name__ == "__main__":
    # Test Case pada program
    # jangan diganti. jika mau diganti, harus dikembalikan
    # ke keadaan semula saat pengumpulan
    
    # mengisi stack
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(1.5)
    s.push(5)
    s.push(3)

    print("Data stack")
    s.printData()
    print()
    print("Menampilkan Data stack paling bawah")
    printDataPertama(s)
    print()
    print("Pembuktian bahwa isi stack tidak berubah")
    s.printData()