def hesapmakinesi():
    birincisayı = int(input("Birinci sayıyı giriniz: "))
    ikincisayı = int(input("İkinci sayıyı giriniz: "))
    islem = input("İşlemi giriniz.(+ = 1, - = 2, * = 3, / = 4, Üs = 5, karakök = 6): ")
    if islem == "1":
        sonuc = birincisayı + ikincisayı
        print("SONUÇ:", sonuc)
    elif islem == "2":
        sonuc = birincisayı - ikincisayı
        print("SONUÇ:", sonuc)
    elif islem == "3":
        sonuc = birincisayı * ikincisayı
        print("SONUÇ:", sonuc)
    elif islem == "4":
        if ikincisayı == 0:
            print("Bölme 0'a eşit olamaz!")
        else:
            sonuc = birincisayı / ikincisayı
            print("SONUÇ:", sonuc)
    elif islem == "5":
        sonuc = birincisayı ** ikincisayı
        print("SONUÇ:", sonuc)  
    elif islem == "6":
            print("Bilgi:Sadece bir sayı üzerinde karekök alınabilir.")           
            sonu = birincisayı ** 0.5
            print("Karekök:", sonu) 
                       
while True:
    hesapmakinesi()