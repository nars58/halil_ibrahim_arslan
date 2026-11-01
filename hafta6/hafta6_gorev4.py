# Görev 4 - Collatz kaşifi
# Halil İbrahim Arslan 20253004034

n = int(input("n: "))

if n <= 0:
    print("Lütfen pozitif bir tam sayı girin.")
else:
    sayi = n
    adim = 0
    en_yuksek = n

    while sayi > 1:
        sayi = sayi // 2 if sayi % 2 == 0 else 3 * sayi + 1
        adim += 1
        if sayi > en_yuksek:
            en_yuksek = sayi

    print(f"{n} -> 1: {adim} adım, en yüksek değer {en_yuksek}")

    ust_sinir = int(input("Üst sınır: "))
    if ust_sinir < 1:
        print("Üst sınır en az 1 olmalıdır.")
    else:
        en_uzun_sayi = 1
        en_uzun_adim = 0

        for baslangic in range(1, ust_sinir + 1):
            gecici = baslangic
            sayac = 0
            while gecici > 1:
                gecici = gecici // 2 if gecici % 2 == 0 else 3 * gecici + 1
                sayac += 1
            if sayac > en_uzun_adim:
                en_uzun_adim = sayac
                en_uzun_sayi = baslangic

        print(f"1-{ust_sinir} arasında en uzun zincir: {en_uzun_sayi} ({en_uzun_adim} adım)")
