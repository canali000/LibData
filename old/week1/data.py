# kitaplar.txt bu dosyanın çıktısı


# Kitap
    # Adı
    # ISBN numarası
    # Yazarı
    # Yayınevi
    # Yayın yılı 
    # Kitapların stok miktarı
    # Konum bilgileri 

lib_data ={
    "kitaplar":{
        "kitap1": {
            "ISBN": 0,
            "yazar": 0,
            "yayın evi": 0,
            "yayın yılı": 0,
            "stok miktarı": 0,
            "konum bilgisi": 0
        },
        "kitap2": {
            "ISBN": 0,
            "yazar": 0,
            "yayın evi": 0,
            "yayın yılı": 0,
            "stok miktarı": 0,
            "konum bilgisi": 0
        }
    },
    "kullanıcılar": ["user1", "user2", "user3"],
    "ödünç alma": {
        "kitap1" : ["user1"],
        "kitap2" : ["user2"],
        "kitap3" : ["user3"]
    }
}

with open(file= "kitaplar.txt", mode= "w", encoding= "utf-8") as createData:
    pass

kitaplar = lib_data["kitaplar"]
kullanicilar = lib_data["kullanıcılar"]
odunc = lib_data["ödünç alma"]

for kitap in kitaplar:
    with open(file= "kitaplar.txt", mode= "a", encoding= "utf-8") as bookData:
        bookData.write(kitap)
        bookData.write("\n")
        bookData.write("\n")
        ozellik = kitaplar[kitap]
        for data in ozellik:
            bookData.write(f"\t{data}: {ozellik[data]}")
            bookData.write("\n")
        bookData.write("\n")


