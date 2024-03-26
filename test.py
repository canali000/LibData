# eğer data.py'ı anlamakta zorlanırsanız
# bu dosyayı çalıştırıp çıktısını inceleyebilirsiniz

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
    }
}

kitaplar = lib_data["kitaplar"]

for kitap in kitaplar:
    print(kitap)
    print("------")
    ozellik = kitaplar[kitap]
    for deger in ozellik:
        print(deger)
    print()

print(ozellik[deger])