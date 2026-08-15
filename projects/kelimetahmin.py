import random

name=input("Adınız nedir? ")
print("Başarılar", name)

words=['pele','marodona','messi','ronaldo','icardi','kerem','güler','baris','kenan','hakan','muslera','neymar','mbappe']

word=random.choice(words)

print("Karakterleri Tahmin Et")

guesses= ''
turns= 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" " \
            "")

        else:
            print(":")
            failed += 1

    if failed == 0:
        print(name,"Kazandın")
        print("Kelime: ", word)
        break

    print()
    guess = input("Harfi Gir:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("YanlIŞ")
        print(name,turns,'hakka sahipsin ' 'Biraz daha tahmin yap')

        if  turns == 0:
          print(name, " Kaybettin")


            