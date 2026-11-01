# Görev 3 - T.C. kimlik numarası doğrulama
# Halil İbrahim Arslan 20253004034

tc = input("T.C. kimlik no: ")

if len(tc) != 11 or not tc.isdigit() or tc[0] == "0":
    print("GEÇERSİZ")
else:
    tek_toplam = 0
    cift_toplam = 0

    for i in range(9):
        rakam = int(tc[i])
        if i % 2 == 0:
            tek_toplam += rakam
        else:
            cift_toplam += rakam

    h10 = (7 * tek_toplam - cift_toplam) % 10
    h11 = (tek_toplam + cift_toplam + h10) % 10

    if h10 == int(tc[9]) and h11 == int(tc[10]):
        print(f"Tek: {tek_toplam} Çift: {cift_toplam} 10. hane: {h10} 11. hane: {h11} -> GEÇERLİ")
    else:
        print("GEÇERSİZ")
