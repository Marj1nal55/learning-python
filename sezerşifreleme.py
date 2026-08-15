def sezar_sifreleme(metin,kaydirma_miktarı):
    sifreli_metin = ""

    for karakter in metin:
        if karakter.isalpha():#Karakter bir harf ise
            ascii_offset = 65 if karakter.isupper() else 97
            sifreli_metin += chr((ord(karakter) - ascii_offset + kaydirma_miktarı) % 26 + ascii_offset)
        else:
           sifreli_metin += karakter#Karakter harf değilse, karakteri sifreli_metin'e ekle
    return sifreli_metin

def sezar_sifrecozme(sifreli_metin, kaydirma_miktarı):
    return sezar_sifreleme(sifreli_metin, -kaydirma_miktarı) 

metin = input("Lütfen şifrelenecek metin girin: ") 
kaydirma_miktarı = int(input("Lütfen kaydırma miktarı girin(1-25): "))    

#metni sifrele
sifreli_metin = sezar_sifreleme(metin, kaydirma_miktarı)
print(f"Şifrelenmiş Metin: {sifreli_metin}")
#sifreli metin sezar sifrecozme

cozulmus_metin = sezar_sifrecozme(sifreli_metin, kaydirma_miktarı)
print(f"Şifre çözülmüş Metin: {cozulmus_metin}")