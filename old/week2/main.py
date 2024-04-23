def userMenu():
    print("-----------------")
    print("Kullanıcı Menüsü")
    print("-----------------")
    print("1- Kitap Ekleme")
    print("2- Kitap Silme")
    print("3- Kitap Güncelleme")
    secim = input("Seçim: ") 
    print()

    if secim == "1":
        kitapEkle(libData)
    elif secim == "2":
        print("Silme")
    elif secim == "3":
        print("Güncelleme")
    else:
        print("Loop")

def userCheck(user):
    with open("kullanıcılar.txt", "r", encoding="utf-8") as kullanici:
        pack = kullanici.readlines()
        pack = [element.rstrip() for element in pack]
        if user in pack:
            return True
        return False

def kitapEkle(libData):
    while True:
        ozellik = {}
        isim = input("Kitap ismi gir: ")
        isbn = input("ISBN no gir: ")
        yazar = input("Yazar ismi gir: ")
        yayinevi = input("Yayınevi ismi gir: ")
        yil = input("Yayın yılı gir: ")
        stok = input("Stok gir: ")

        kitaplar = libData["kitaplar"]
        kitaplar[isim] = ozellik
        ozellik["ISBN"] = isbn
        ozellik["yazar"] = yazar
        ozellik["yayinevi"] = yayinevi
        ozellik["yil"] = yil
        ozellik["stok"] = stok

        enter = input("Tekrar veri girmek için 'y' veya çıkmak için 'ENTER': ").lower()

        if enter == "":
            break

    with open(file= "kitaplar.txt", mode="a", encoding="utf-8") as bookData:
        for kitap in libData["kitaplar"]:
            pack = []
            pack.append(kitap)
            for data in libData["kitaplar"][kitap]:
                pack.append(libData["kitaplar"][kitap][data])
            pack = ",".join(pack)
            bookData.write(pack)
            bookData.write("\n")

with open(file="kitaplar.txt", mode="a", encoding="utf-8") as checkFile:
    checkFile.write("")

with open(file="kullanıcılar.txt", mode="a", encoding="utf-8") as checkFile:
    checkFile.write("")

libData = {
    "kitaplar": {}
}

user = input("Kullanıcı adı gir: ")
if userCheck(user) == True:
    userMenu()
else:
    print("Kullanıcı bulunamadı.")
