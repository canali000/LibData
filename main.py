# menü işlemleri
def adminMenu():
    print("-----------------")
    print("Admin Menüsü")
    print("-----------------")
    print("1- Kitap Görüntüleme")
    print("2- Kitap Ödünç Alma")
    print("3- Kitap İade Etme")
    print("4- Kitap Ekleme")
    print("5- Kitap Silme")
    print("6- Kitap Güncelleme")
    print("7- Kullanıcı Ekle")
    print("8- Admin Ekle")
    print()
    secim = input("Seçim: ").lower().rstrip()
    print()

    if secim == "1":
        kitapGoruntule()
    elif secim == "2":
        oduncAl(secim)        
    elif secim == "3":
        oduncAl(secim)        
    elif secim == "4":
        kitapEkle()
    elif secim == "5":
        kitapSil()
    elif secim == "6":
        kitapGuncelle()
    elif secim == "7":
        kullaniciEkle()
    elif secim == "8":
        adminEkle()
    else:
        adminMenu()

def kullaniciMenu():
    print("-----------------")
    print("Kullanıcı Menüsü")
    print("-----------------")
    print("1- Kitap Görüntüleme")
    print("2- Kitap Ödünç Alma")
    print("3- Kitap İade Etme")
    print()
    secim = input("Seçim: ").lower().rstrip()
    print()

    if secim == "1":
        kitapGoruntule()
    elif secim == "2":
        oduncAl(secim)        
    elif secim == "3":
        oduncAl(secim)        
    else:
        adminMenu()

# yetkilendirme

def adminCheck(user, password):
    with open(file="adminler.txt", mode="r", encoding="utf-8") as kullanici:
        pack = kullanici.readlines()
        pack = [element.rstrip() for element in pack]
        check = user + keyGenerator(password)
        if check in pack:
            return True
        elif check not in pack:
            with open(file="kullanıcılar.txt", mode="r", encoding="utf-8") as kullanici:
                pack = kullanici.readlines()
                pack = [element.rstrip() for element in pack]
                check = user + keyGenerator(password)
                if check in pack:
                    return False
        return None

def kullaniciEkle():
    user = input("Kullanıcı adını oluştur: ").lower().rstrip()
    password = input("Şifreni oluştur: ").lower().rstrip()
    print()

    code = user + keyGenerator(password) + "\n"

    with open(file="kullanıcılar.txt", mode="a", encoding="utf-8") as writeFile:
        writeFile.write(code)

def adminEkle():
    admin = input("Kullanıcı adını oluştur: ").lower().rstrip()
    password = input("Şifreni oluştur: ").lower().rstrip()
    print() 

    code = admin + keyGenerator(password) + "\n"

    with open(file="adminler.txt", mode="a", encoding="utf-8") as writeFile:
        writeFile.write(code)

def keyGenerator(password):
    key = 0
    for passChar in password:
        unipoint = ord(passChar)
        key += unipoint
    return str(key)

# kullanıcı işlemleri
def kitapBul(search):
    with open(file="kitaplar.txt", mode="r", encoding="utf-8") as readFile:
        data = readFile.readlines()

    index = 0
    for element in data:
        pack = element.split(",")
        if pack[0].rstrip() == search:
            return index
        index += 1

def kitapEkle():
    kitaplar = {}
    while True:

        kitap = {}
        isim = input("Kitap ismi gir: ").lower().rstrip()
        if kitapBul(isim) != None:
            print(f"{isim.title()} isimli kitap listede zaten var.")
            print()
            continue
        isbn = input("ISBN no gir: ").lower().rstrip()
        yazar = input("Yazar ismi gir: ").lower().rstrip()
        yayinevi = input("Yayınevi ismi gir: ").lower().rstrip()
        yil = input("Yayın yılı gir: ").lower().rstrip()
        stok = input("Stok adedini gir: ").lower().rstrip()


        kitaplar[isim] = kitap
        kitap["ISBN"] = isbn
        kitap["yazar"] = yazar
        kitap["yayinevi"] = yayinevi
        kitap["yil"] = yil
        kitap["stok"] = stok

        enter = input("Tekrar kitap girmek için 'y' veya çıkmak için 'ENTER': ").lower().rstrip()
        print()
        if enter == "":
            break

    with open(file= "kitaplar.txt", mode="a", encoding="utf-8") as bookData:
        for kitap in kitaplar:
            pack = []
            pack.append(kitap)
            for data in kitaplar[kitap]:
                pack.append(kitaplar[kitap][data])
            pack = ",".join(pack)
            bookData.write(pack)
            bookData.write("\n")
            print(f"{kitap.title()} isimli kitap listeye eklendi.")
            print()
    return kitaplar

def kitapSil():
    toDelete = input("Silmek istediğin kitabın adını gir: ").lower().rstrip()

    if toDelete == "kitap ismi":
        print("Geçersiz işlem.")

    elif kitapBul(toDelete) == None:
        print(f"{toDelete.title()} isimli kitap listede bulunamadı.")

    else:
        with open(file="kitaplar.txt", mode="r", encoding="utf-8") as readFile:
            data = readFile.readlines()
            data.pop(kitapBul(toDelete))

        with open(file="kitaplar.txt", mode="w", encoding="utf-8") as writeFile:
            writeFile.writelines(data)
        print(f"{toDelete.title()} isimli kitap listeden silindi.")
        print()


def kitapGuncelle():
    toUpdate = input("Güncellemek istediğin kitabın ismini gir: ").lower().rstrip()

    if toUpdate == "kitap ismi":
        print("Geçersiz işlem.")

    elif kitapBul(toUpdate) == None:
        print(f"{toUpdate.title()} isimli kitap listede bulunamadı.")

    else:
        with open(file="kitaplar.txt", mode="r", encoding="utf-8") as readFile:
            data = readFile.readlines()

        kitap = {}
        isim = input("Kitap ismi gir: ").lower().rstrip()
        if kitapBul(isim) != None:
            print()
            print(f"{isim.title()} isimli kitap listede zaten var.")
            print()
            return None
        isbn = input("ISBN no gir: ").lower().rstrip()
        yazar = input("Yazar ismi gir: ").lower().rstrip()
        yayinevi = input("Yayınevi ismi gir: ").lower().rstrip()
        yil = input("Yayın yılı gir: ").lower().rstrip()
        stok = input("Stok adedini gir: ").lower().rstrip()

        kitap["isim"] = isim
        kitap["ISBN"] = isbn
        kitap["yazar"] = yazar
        kitap["yayinevi"] = yayinevi
        kitap["yil"] = yil
        kitap["stok"] = stok

        updated = [kitap[ozellik] for ozellik in kitap]
        updated = ",".join(updated)
        data[kitapBul(toUpdate)] = updated + "\n"

        with open(file="kitaplar.txt", mode="w", encoding="utf-8") as writeFile:
            writeFile.writelines(data)

        print()
        print(f"{isim.title()} isimli kitabın bilgileri güncellendi.")

def kitapGoruntule():
    toFind = input("Görüntülemek istediğin kitabın ismini gir: ").lower().rstrip()

    if toFind == "kitap ismi":
        print("Geçersiz işlem.")

    elif kitapBul(toFind) == None:
        print(f"{toFind.title()} isimli kitap listede bulunamadı.")

    else:
        with open(file="kitaplar.txt", mode="r", encoding="utf-8") as readFile:
            pack = readFile.readlines()
            pack = [element.rstrip() for element in pack]
            data = pack[kitapBul(toFind)]
            data = data.split(",")

            isim = data[0]
            isbn = data[1]
            yazar = data[2]
            yayinevi = data[3]
            yil = data[4]
            stok = data[5]

            print()
            print(f"Kitap ismi: {isim.title()}")
            print(f"ISBN numarası: {isbn}")
            print(f"Yazar adı: {yazar.title()}")
            print(f"Yayın evi: {yayinevi.title()}")
            print(f"Yayın yılı: {yil}")
            if stok != "0":
                print(f"Stokta {stok} adet mevcut.")
            else: 
                print("Stokta mevcut değil.")


def oduncAl(secim):
    if secim == "2":
        toBorrow = input("Ödünç almak istediğin kitabın adını gir: ").lower().rstrip()
        change = -1
    else:
        toBorrow = input("İade etmek istediğin kitabın adını gir: ").lower().rstrip()
        change = 1

    if toBorrow == "kitap ismi":
        print("Geçersiz işlem.")

    elif kitapBul(toBorrow) == None:
        print(f"{toBorrow.title()} isimli kitap listede bulunamadı.")

    else:
        with open(file="kitaplar.txt", mode="r", encoding="utf-8") as readFile:
            pack = readFile.readlines()
            data = pack[kitapBul(toBorrow)]
            data = data.rstrip()
            data = data.split(",")
            if data[-1] == "0" and secim == "2":
                print(f"{toBorrow.title()} isimli kitap stokta yok.")
                return None
            data[-1] = str(int(data[-1]) + change)
            data = ",".join(data)
            pack[kitapBul(toBorrow)] = data + "\n"

        with open(file="kitaplar.txt", mode="w", encoding="utf-8") as writeFile:
            writeFile.writelines(pack)

# Dosya Doğrulama
try:
    with open(file="adminler.txt", mode="r", encoding="utf-8") as checkFile:
        pass
except FileNotFoundError:
    print("Admin Dosyası Eksik")
    print("Yeni Dosya Oluşturuldu")
    print()
    with open(file="adminler.txt", mode="a", encoding="utf-8") as checkFile:
        admin = "can" + keyGenerator("can") + "\n"
        checkFile.write(admin)

try:
    with open(file="kitaplar.txt", mode="r", encoding="utf-8") as checkFile:
        pass
except FileNotFoundError:
    print("Kitaplar Dosyası Eksik")
    print("Yeni Dosya Oluşturuldu")
    print()
    with open(file="kitaplar.txt", mode="a", encoding="utf-8") as checkFile:
        checkFile.write("kitap ismi,ISBN,yazar,yayınevi,yil,stok\n")

try:
    with open(file="kullanıcılar.txt", mode="r", encoding="utf-8") as checkFile:
        pass
except FileNotFoundError:
    print("Kullanıcı Dosyası Eksik")
    print("Yeni Dosya Oluşturuldu")
    print()
    with open(file="kullanıcılar.txt", mode="a", encoding="utf-8") as checkFile:
        pass

# Program Başlangıcı
while True:
    user = input("Kullanıcı adı gir: ").lower().rstrip()
    password = input("Şifreni gir: ").lower().rstrip()

    if adminCheck(user, password) == True:
        adminMenu()
        break
    elif adminCheck(user, password) == False:
        kullaniciMenu()
        break
    else:
        print()
        print("Kullanıcı bulunamadı.")
        print("Kayıt oluşturmak için '1'")
        print("Tekrar şifre girmek için 'ENTER'")
        secim = input("Seçim: ").lower().rstrip()
        print()

        if secim == "1":
            kullaniciEkle()
            kullaniciMenu()
            break
