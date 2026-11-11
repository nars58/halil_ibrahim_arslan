# Görev 5 - Closure ve lambda
# Halil İbrahim Arslan 20253004034


def hamle_sayaci():
    """Her çağrıldığında bir artan sayaç fonksiyonu döndürür."""
    sayi = 0

    def sayac() -> int:
        nonlocal sayi
        sayi += 1
        return sayi

    return sayac


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür."""
    return sorted(
        galaksi["gezegenler"],
        key=lambda g: (-len(galaksi["baglantilar"][g]), g)
    )


def travel(galaksi: dict) -> None:
    """Her yolculukta hamle sayacını çağırır ve toplam hamleyi yazdırır."""
    sayac = hamle_sayaci()
    toplam = 0
    for _ in range(13):
        toplam = sayac()
    print(f"Oyunu {toplam} hamlede bitirdin!")


g = {
    "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
    "baglantilar": {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "sirius"],
        "sirius": ["centauri", "dünya", "orion"],
        "orion": ["sirius", "kara_delik"],
        "kara_delik": ["orion"]
    }
}

travel(g)
print(en_bagli_gezegenler(g))


def test_hamle_sayaci():
    s = hamle_sayaci()
    assert s() == 1
    assert s() == 2


def test_en_bagli_gezegenler():
    assert en_bagli_gezegenler(g) == ["sirius", "centauri", "dünya", "orion", "kara_delik"]
