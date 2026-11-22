# Görev 5 - Türkçe kelime sınıfı
# Halil İbrahim Arslan 20253004034

ALFABE = "abcçdefgğhıijklmnoöprsştuüvyz"


class TrKelime:
    def __init__(self, metin):
        self.metin = metin.replace("I", "ı").replace("İ", "i").lower()

    def __str__(self):
        return self.metin

    def __len__(self):
        return len(self.metin)

    def __getitem__(self, indeks):
        return self.metin[indeks]

    def __contains__(self, alt_metin):
        return str(alt_metin) in self.metin

    def __eq__(self, diger):
        return self.metin == diger.metin

    def __lt__(self, diger):
        if len(self.metin) < len(diger.metin):
            kisa_uzunluk = len(self.metin)
        else:
            kisa_uzunluk = len(diger.metin)

        for i in range(kisa_uzunluk):
            sira1 = ALFABE.find(self.metin[i])
            sira2 = ALFABE.find(diger.metin[i])
            if sira1 != sira2:
                return sira1 < sira2
        return len(self.metin) < len(diger.metin)

    def buyuk(self):
        return self.metin.replace("i", "İ").replace("ı", "I").upper()


print(f"çay   < dağ     Türkçe: {TrKelime('çay') < TrKelime('dağ')}   Python str: {'çay' < 'dağ'}")
print(f"ılık  < iğne    Türkçe: {TrKelime('ılık') < TrKelime('iğne')}   Python str: {'ılık' < 'iğne'}")
print(f"ördek < pasta   Türkçe: {TrKelime('ördek') < TrKelime('pasta')}   Python str: {'ördek' < 'pasta'}")
print(f'TrKelime("Işık") == TrKelime("ışık") -> {TrKelime("Işık") == TrKelime("ışık")}')
k = TrKelime("İSTANBUL")
print(f'k = TrKelime("İSTANBUL") -> {k}   len(k) -> {len(k)}')
print(f'"tan" in k -> {"tan" in k}                     k.buyuk() -> {k.buyuk()}')
