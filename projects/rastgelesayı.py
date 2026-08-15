def main():
 import random

 rastgele_sayi = random.randint(1, 100)

 hak_sayisi = 5
 print("Sayı tahmin oyununa hoş geldiniz!")
 print(f"1 ile 100 arasında bir sayı tuttum.Bakalim {hak_sayisi} denemede bu sayıyı bulunuz.")

 while hak_sayisi > 0:
    tahmin = int(input("Tahmininizi girin: "))
    print("dalgamı geçiosun")
    if  tahmin < rastgele_sayi:
        print("Girdiğiniz sayı, tahmin edilen sayıdan küçük!")
    elif tahmin > rastgele_sayi:
        print("Girdiğiniz sayı, tahmin edilen sayıdan büyük!")    
    else:
        print(f"Tebrikler, doğru tahmin ettiniz! Sayınız: {rastgele_sayi}")


    hak_sayisi -= 1
    print(f"{hak_sayisi} hakkınız kaldı.")
    if hak_sayisi == 0:
        print(f"Kaybettiniz! Doğru sayı: {rastgele_sayi}")   

while True:
    main()              