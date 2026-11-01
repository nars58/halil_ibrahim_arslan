# Görev 5 - Adam asmaca
# Halil İbrahim Arslan 20253004034

gizli_kelime = "KOŞUL"
tahminler = ""
hata = 0
maks_hata = 6

while hata < maks_hata:
    gorunum = ""
    tamamlandi = True

    for karakter in gizli_kelime:
        if karakter in tahminler:
            gorunum += karakter + " "
        else:
            gorunum += "_ "
            tamamlandi = False

    if tamamlandi:
        print(f"{gorunum}(hata: {hata}/{maks_hata}) Kazandınız!")
        break

    print(f"{gorunum}(hata: {hata}/{maks_hata})")
    giris = input("Harf: ")

    if giris == "i":
        harf = "İ"
    elif giris == "ı":
        harf = "I"
    else:
        harf = giris.upper()

    if len(harf) != 1 or not harf.isalpha():
        print("Lütfen tek bir harf girin.")
        continue

    if harf in tahminler:
        print("Bu harfi zaten denediniz.")
        continue

    tahminler += harf

    if harf not in gizli_kelime:
        hata += 1
else:
    print(f"Kaybettiniz! Doğru kelime: {gizli_kelime}")
