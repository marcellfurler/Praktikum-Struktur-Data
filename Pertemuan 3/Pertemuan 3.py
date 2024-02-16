# # list=[1,2,3,4,5]
# # nama="Marcell"

# tanggal=[
#     [10, "desember"],
#     [15, "juni"],
#     [13, 8]
# ]

# print(tanggal[2][1])


# angka1={1,2,3,4,5}
# angka2={2,4,7,9}

# lurus=angka1|angka2
# print(lurus)
# dan=angka1&angka2
# print(dan)


data_mahasiswa={
    "Marcell":{
        "Nama" : "Marcell",
        "NIM" : 71220855,
        "Kuliah" : "Universitas Kristen Duta Wacana"

    },
    "Asep" :{
        "Nama" : "Yosepus Ahmad Christian",
        "NIM": 71221856,
        "Kuliah" : "Universitas Kristen Islam Internasional"
    }
}

print(data_mahasiswa["Asep"]["Nama"])