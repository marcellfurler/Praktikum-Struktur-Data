# buah=open("fruit.txt", "w")
# buah.write("Apel\n")
# buah.write("Buah Naga\n")

# buah.close()

# buah=open("fruit.txt", "r")
# buah2=buah.readline()
# for i in buah2:
#     print(i)

data=None
with open("menu.csv", "r") as datafile:
    data=datafile.readlines()
for i in range(0, len(data)):
    data[i] = data[i].strip()

data.append("Makanan : Babi Tumis Mentega : 25.000")
data.append("Makanan : Babi Tumis Minyak : 34.000")
data.append("Makanan : Ayam panggang Torch : 51.000")
data.append("Makanan : Babi Guling api abadi gunung berapi : 250.000")
data.append("Makanan : Babi Tumis  : 25.000")


# with open("menu.csv", "w") as datafile:
#     for line in data:
#         datafile.write(line + "\n")


buka=open("menu.csv", "r")
baru=buka.readlines()
for x in range(1, len(baru)):
    datax=baru[x].strip()
    baru2=datax.split(":")
    nama_makanan=baru2[0]
    harga=baru2[1]
    print(f"Makanan : {nama_makanan}\nHarga : {harga} ")
buka.close()