#  program list buku


list_buku = []
while True:
    print("\nMasukkan data buku")
    judul = input("Judul buku\t: ")
    penulis = input("Nama penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index} |{buku[0]}| {buku[1]}")

    print("\n\n","="*20)
    isLanjut = input("Apakah mau lanjut?(y/n) ")

    if isLanjut == "n":
        break

print("PROGRAM SELESAI")