class Mahasiswa:
    # atribut/variable
    _nim=""
    _nama=""
    _ipk=0.0

    # Methods
    def data_mahasiswa(self):
        penge= "Informasi Mahasiswa : "+ "\nIPK : "+ str(self._ipk) + "\nNama : "+ self._nama + "\nNIM : " + str(self._nim)
        return penge
    
    # construktor
    def __init__(self, _ipk, _nama, _nim):
        print("constructor of Mahasiswa")
        self._ipk=_ipk
        self._nama=_nama
        self._nim=_nim
        


# contoh construktor
printout=Mahasiswa(3.8, "Marcell Furler", "71220855")
print(f"Nama\t: {printout._nama}")
print(f"NIM\t: {printout._nim}")
print(f"IPK\t: {printout._ipk}")

    

# contoh methods

mahas1=Mahasiswa()
mahas1._nama="Marcell"
mahas1._nim="71220855"
mahas1._ipk=3.5
print(mahas1.data_mahasiswa())