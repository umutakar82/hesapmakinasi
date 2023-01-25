import os

os.system("title Hesap Makinası")

print("""
Hesap Makinası

Çarpam İşlemi İçin / 1
Bölme İşlemi İçin / 2
Toplama İşlemi İçin / 3
Çıkartma İşlemi İçin / 4

""")

islemnum = int(input("İşlem Numaranız : "))

if islemnum == 9:
    print("Hatalı İşlem")
else:
    print("Hatalı İşlem")

sayi1 = int(input("Sayıyı Giriniz (1) : "))
sayi2 = int(input("Sayıyı Giriniz (2) : "))

if islemnum == 1:
    islemcarpma = sayi1 * sayi2
    print(f"Sonuç : {islemcarpma}")

if islemnum == 2:
    islembolme = sayi1 / sayi2
    print(f"Sonuç : {islembolme}")

if islemnum == 3:
    islemtoplama = sayi1 + sayi2
    print(f"Sonuç : {islemtoplama}")

if islemnum == 4:
    islemcikartma = sayi1 - sayi2
    print(f"Sonuç : {islemcikartma}")

os.system("pause")
