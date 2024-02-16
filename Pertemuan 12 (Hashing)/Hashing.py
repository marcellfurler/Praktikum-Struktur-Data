class BukuTelepon():
    def __init__(self):
        self.size=6
        self.map=[None]*self.size

    def _getHash(self, key):
        hash=0
        for char in str(key):
            hash+=ord(char)
        return hash % self.size
    
    def _probing(self, key):
        for index in range(self.size):
            probeHash=self._linearProbing(key, index)
            if (self.map[probeHash] is None) or (self.map[probeHash]=="Deleted"):
                return probeHash
        return None
    
    def _linearProbing(self, key, index):
        return (self._getHash(key)+index)%self.size
    

    def add(self, key, value):
        key_hash=self._getHash(key)
        key_value=[key, value]

        if self.map[key_hash] is None:
            self.map[key_hash]= list([key_value])
            return True
        else:
            print(f"Key Hash {key_hash} sudah terisi")
            return False
        
    def getPhoneNumber(self, key):
        key_hash = self._getHash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0]==key:
                    return pair[1]
        print(f"Key {key} tidak ditemukan")
        return "None"
    
    def delete(self, key):
        key_hash=self._getHash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0]==key:
                self.map[key_hash]=None
                self.map[key_hash]="deleted"
                return True
        print(f"Key {key} tidak ditemukan")
        return False
    
    def print(self):
        print("_-_Buku Telepon_-_")
        for item in self.map:
            if item is not None:
                print(str(item))


coba=BukuTelepon()
coba.add("Acell", "081248891255")
coba.add("Sia", "085254680336")
coba.add("Billie", "082247791245")
coba.add("Acello", "08521456874")
coba.add("Ahmad", "082247896547")
coba.add("Aman", "085269874563")
coba.print()
# coba.delete("Sia")
# coba.print()
# print("Acell : " + coba.getPhoneNumber("Acell"))
# coba.add("Billie", "082247712568")
# coba.add("Robbie", "082247711111")
coba.print()