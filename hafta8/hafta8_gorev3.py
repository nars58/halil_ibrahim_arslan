# Görev 3 - Vigenere şifresi
# Halil İbrahim Arslan 20253004034

BUYUK = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KUCUK = "abcdefghijklmnopqrstuvwxyz"


def vigenere(metin, anahtar, yon=1):
    anahtar = anahtar.upper()
    sonuc = ""
    j = 0
    for karakter in metin:
        kayma = BUYUK.find(anahtar[j % len(anahtar)])
        if karakter in BUYUK:
            sira = BUYUK.find(karakter)
            sonuc += BUYUK[(sira + yon * kayma) % 26]
            j += 1
        elif karakter in KUCUK:
            sira = KUCUK.find(karakter)
            sonuc += KUCUK[(sira + yon * kayma) % 26]
            j += 1
        else:
            sonuc += karakter
    return sonuc


sifreli = vigenere("Attack at dawn", "LEMON")
cozulmus = vigenere(sifreli, "LEMON", -1)

print('vigenere("Attack at dawn", "LEMON")    ->', sifreli)
print('vigenere("Lxfopv ef rnhr", "LEMON", -1) ->', cozulmus)
