#kullanıcı ve şifreli kayıtlı dosyal

notter = []

def secenekler():
      print("1.Ekle not")
      print("2.Not kaldır")
      print("3.Notları dosyaya kaydet")
      print("4.çıkış")
      print("5.Notları görüntüle")
      print("6.Notları şifrele")
      scnk  = input("İşlemin sayısını seçin: ")

def en():
      yeninot = input("Notunuzu yazın: ")   
      notter.append(yeninot)
      print("Notunuz eklendi.")

def ng():
      if not notter:
           print("Not defteri boş")

      else:
           print("\nNotlarınız\n")     
           for i, not_ in enumerate(notter, 1)
                  print(f"{i}. {not_}")

def nt():
     not_no  = int(input("Silmek istediğiniz notun numarasını girin: ")) -1
     if 0 <= not_no < len(notter):
          silinen_not = notter.pop(not_no)    
          print(f" '{silinen_not}' başarıyla silindi")      

     
def nt():
     notkaldır =       

print("Not defterinize hos geldiniz")
giris = input ("Devam etmek istiomusuz Y or N: ")

if giris.lower() == "y":
   secenekler()
   

else:
   print("Hoscakal")
   exit()
        

   