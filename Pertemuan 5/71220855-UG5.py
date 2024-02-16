class Mahasiswa :
    nilaiAngka = {"A": 4, "A-": 3.7,"B+": 3.3, "B":3, "B-": 2.7, "C+": 2.3, "C": 2, "D": 1, "E": 0}
    _nama=""
    _nim=0
    _prodi=""
    _ipk=0.00

    def __init__(self, _nama, _nim, _prodi):
        self._nama=_nama
        self._nim=_nim
        self._prodi=_prodi

    def informasi(self):
        print("===INFORMASI MAHASISWA===")
        nama=print(f"Nama : {self._nama}")
        nim=print(f"NIM : {self._nim}")
        prodi=print(f"Prodi : {self._prodi}")

    

    def hitungIPS(nilai):
        masukan=int(input("Masukan jumlah matakuliah : "))
        nilainya=0
        sksnya=0
        for i in range(masukan):
            input("Masukan mata kuliah : ")
            nilai=input("Masukan Nilai : ")
            if nilai== "A":
                nilai=4
                # return nilai
            elif nilai=="A-":
                nilai= 3.7
                # return nilai
            elif nilai=="B+":
                nilai=3.3
                # return nilai
            elif nilai=="B":
                nilai=3
                # return nilai
            elif nilai=="B-":
                nilai=2.7
                # return nilai
            elif nilai=="C+":
                nilai=2.3
                # return nilai
            elif nilai=="C":
                nilai= 2
                # return nilai
            elif nilai=="D":
                nilai= 1
                # return nilai
            elif nilai=="E":
                nilai= 0
                # return nilai
            sks=int(input("Masukan SKS : "))
            nilainya=nilainya+(nilai*sks)
            sksnya=sksnya+sks
        totipk=nilainya/sksnya
        print(f"IPK nya adalah {round(totipk,2)}")

            # print(nilaiipk)
            


    # def informasi(self, nama, nim, prodi):
    #     print("===INFORMASI MAHASISWA===")
    #     nama=input("Nama : ")
    #     nim=input("NIM : ")
    #     prodi=input("Prodi : ")

budi=Mahasiswa("Budi", 71220854, "FTI")
budi.informasi()
budi=budi.hitungIPS()



