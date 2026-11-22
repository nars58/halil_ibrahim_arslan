# Görev 2 - Taban dönüştürücü
# Halil İbrahim Arslan 20253004034

RAKAM = "0123456789ABCDEF"


def onluktan(n, taban):
    if n == 0:
        return "0"
    sonuc = ""
    while n > 0:
        sonuc = RAKAM[n % taban] + sonuc
        n = n // taban
    return sonuc


def onluga(metin, taban):
    metin = metin.upper()
    sonuc = 0
    for ch in metin:
        sonuc = sonuc * taban + RAKAM.find(ch)
    return sonuc


ikilik = onluktan(2026, 2)
sekizlik = onluktan(2026, 8)
onaltilik = onluktan(2026, 16)

print(f"2026 -> ikilik {ikilik} · sekizlik {sekizlik} · onaltılık {onaltilik}")
print(f'onluga("7ea", 16) = onluga("11111101010", 2) = onluga("3752", 8) = {onluga("7ea", 16)}')
