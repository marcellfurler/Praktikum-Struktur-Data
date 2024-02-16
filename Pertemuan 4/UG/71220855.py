import json

jumlah_mahasiswa=int(input("Masukan jumlah mahasiswa : "))
with open("biodata.json") as datafile:
    lama=json.load(datafile)

for x in range(jumlah_mahasiswa):
    nim=int(input("Masukan NIM Mahasiswa : "))
    nama=input("Masukan nama Mahasiswa : ")
    jurusan=input("Masukan jurusan mahasiswa : ")
    jumlah_matkul=int(input("Masukan jumlah mata kuliah : "))
    matkul1=[]
    for y in range(jumlah_matkul):
        matkul=input("Masukan mata kuliah : ")
        matkul1.append(matkul)
    print("Data Berhasil Ditambahkan")
    data=dict()
    data['nim']=nim
    data['nama']=nama
    data['jurusan']=jurusan
    data['matkul']=matkul
    lama[nim]=data
    

    
with open("biodata.json", "w") as datafile:
    json.dump(lama, datafile)
