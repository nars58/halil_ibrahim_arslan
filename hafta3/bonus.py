# Bonus - Süre ölçen sarmalayıcı fonksiyon
# Halil İbrahim Arslan 20253004034

import time


def sure_olc(fonksiyon):
    """Verilen fonksiyonu çağırıp çalışma süresini yazdıran sarmalayıcı döndürür."""
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        print(f"{fonksiyon.__name__}: {bitis - baslangic:.6f} sn")
        return sonuc
    return sarmalayici


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür."""
    return sorted(
        galaksi["gezegenler"],
        key=lambda g: (-len(galaksi["baglantilar"][g]), g)
    )


en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)

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

print(en_bagli_gezegenler(g))


def test_sure_olc():
    assert en_bagli_gezegenler(g) == ["sirius", "centauri", "dünya", "orion", "kara_delik"]
