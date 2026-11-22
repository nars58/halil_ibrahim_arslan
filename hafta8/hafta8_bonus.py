# Bonus - Roma rakamı dönüştürücü
# Halil İbrahim Arslan 20253004034


def romaya(sayi):
    sonuc = ""
    while sayi >= 1000:
        sonuc += "M"
        sayi -= 1000
    if sayi >= 900:
        sonuc += "CM"
        sayi -= 900
    if sayi >= 500:
        sonuc += "D"
        sayi -= 500
    if sayi >= 400:
        sonuc += "CD"
        sayi -= 400
    while sayi >= 100:
        sonuc += "C"
        sayi -= 100
    if sayi >= 90:
        sonuc += "XC"
        sayi -= 90
    if sayi >= 50:
        sonuc += "L"
        sayi -= 50
    if sayi >= 40:
        sonuc += "XL"
        sayi -= 40
    while sayi >= 10:
        sonuc += "X"
        sayi -= 10
    if sayi >= 9:
        sonuc += "IX"
        sayi -= 9
    if sayi >= 5:
        sonuc += "V"
        sayi -= 5
    if sayi >= 4:
        sonuc += "IV"
        sayi -= 4
    while sayi >= 1:
        sonuc += "I"
        sayi -= 1
    return sonuc


def romadan(metin):
    metin = metin.upper()
    toplam = 0
    onceki = 0
    for i in range(len(metin) - 1, -1, -1):
        harf = metin[i]
        if harf == "I":
            deger = 1
        elif harf == "V":
            deger = 5
        elif harf == "X":
            deger = 10
        elif harf == "L":
            deger = 50
        elif harf == "C":
            deger = 100
        elif harf == "D":
            deger = 500
        else:
            deger = 1000

        if deger < onceki:
            toplam -= deger
        else:
            toplam += deger
        onceki = deger
    return toplam


print("2026 ->", romaya(2026))
print("1994 ->", romaya(1994))
print("XLII ->", romadan("XLII"))
