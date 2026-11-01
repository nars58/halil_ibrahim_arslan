# Görev 2 - Metin analizörü
# Halil İbrahim Arslan 20253004034

cumle = input("Cümle: ")

if cumle == "":
    print("Cümle boş olamaz.")
else:
    harf_sayisi = 0
    sesli_sayisi = 0
    sessiz_sayisi = 0
    rakam_sayisi = 0
    kelime_sayisi = 0
    kelime_icinde = False

    ters_cumle = ""
    duz_harfler = ""
    ters_harfler = ""
    sesliler = "aeıioöuüAEIİOÖUÜ"

    for karakter in cumle:
        ters_cumle = karakter + ters_cumle

        if karakter.isalpha():
            harf_sayisi += 1
            if karakter in sesliler:
                sesli_sayisi += 1
            else:
                sessiz_sayisi += 1

            if karakter == "İ":
                kucuk = "i"
            elif karakter == "I":
                kucuk = "ı"
            else:
                kucuk = karakter.lower()

            duz_harfler = duz_harfler + kucuk
            ters_harfler = kucuk + ters_harfler
        elif karakter.isdigit():
            rakam_sayisi += 1

        if karakter != " ":
            if not kelime_icinde:
                kelime_sayisi += 1
                kelime_icinde = True
        else:
            kelime_icinde = False

    print(f"Harf: {harf_sayisi} Sesli: {sesli_sayisi} Sessiz: {sessiz_sayisi} Rakam: {rakam_sayisi} Kelime: {kelime_sayisi}")
    print(f"Ters: {ters_cumle}")

    if duz_harfler != "" and duz_harfler == ters_harfler:
        print("Palindrom")
    else:
        print("Palindrom değil")
