# Bonus - Luhn algoritması kontrol hanesi bulucu
# Halil İbrahim Arslan 20253004034

numara = "453914880343646"

for aday in range(10):
    tam_numara = numara + str(aday)
    toplam = 0

    for i in range(16):
        rakam = int(tam_numara[i])
        if i % 2 == 0:
            carpim = rakam * 2
            if carpim > 9:
                carpim -= 9
            toplam += carpim
        else:
            toplam += rakam

    if toplam % 10 == 0:
        print(f"Geçerli kontrol hanesi: {aday}")
        print(f"Tam numara: {tam_numara}")
        break
