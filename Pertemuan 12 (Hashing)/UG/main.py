class HashTable:
    def __init__(self):
        self.size = 10
        self.map = [None]*self.size
    
    def _get_hash(self, key):
        hash = key
        return hash % self.size
    
    def _linear_probing(self, key, index):
        return (self._get_hash(key)+index)%self.size

    def _probing(self, key):
        for index in range(self.size):
            probeHash=self._linear_probing(key, index)
            if (self.map[probeHash] is None) or (self.map[probeHash]=="Deleted"):
                return probeHash
        return None

    def add(self, key, value):
        key_hash=self._get_hash(key)
        key_value=[key, value]
        if self.map[key_hash] is None:
            self.map[key_hash]= list([key_value])
            return True
        else:
            key_hash = self._probing(key)
            if key_hash is None:
                print("Sudah ada")
                return False
            
        self.map[key_hash]= list([key_value])
        return False
        

    def print_all(self):
        for item in self.map:
            if item is not None:
                print(f"NIM : {item[0][0]} Nama : {item[0][1]}")
    
    def get_data(self, key):
        key_hash = self._get_hash(key=key)
        if self.map[key_hash] is not None:
            if self.map[key_hash][0][0] == key:
                return self.map[key_hash][0][-1]
            
    
    def resize(self, size):
        map_lama=self.map
        self.size=size
        self.map=[None]*size

        for i in map_lama:
            if i is not None:
                key,value=tuple(i[0])
                self.add(key, value)

        # for i in map_lama:
        #     if i is not None:
        #         for key in i :
        #             self.add(key)
        
        
            


def main():
    ht : HashTable = HashTable()
    # isi hash table
    
    ht.add(71210689, "Gian")
    ht.add(71210683, "Yandi")
    ht.add(71210699, "Andreas")

    print("==== HASH TABLE SEBELUM DIRESIZE ====")
    print()
    # print(ht.map)
    ht.print_all()
    print(f"mahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")
    print()
    # resize hash table
    ht.resize(3)

    print("==== HASH TABLE SETELAH DIRESIZE ====")
    print()
    ht.print_all()
    print(f"mahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")
    

if __name__ == "__main__":
    main()