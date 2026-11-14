# Görev 4 - Önbellekli rota sayacı
# Halil İbrahim Arslan 20253004034

import time
from functools import lru_cache


def onbelleksiz_rota_sayaci(baglantilar: dict[str, list[str]]):
    """Önbellek kullanmadan rota sayısını hesaplayan fonksiyonu döndürür."""
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        toplam = 0
        for komsu in baglantilar[gezegen]:
            toplam += rota_sayisi(komsu, adim - 1)
        return toplam
    return rota_sayisi


def rota_sayaci(baglantilar: dict[str, list[str]]):
    """@lru_cache ile önbellekli rota_sayisi fonksiyonunu tanımlayıp döndürür."""
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        toplam = 0
        for komsu in baglantilar[gezegen]:
            toplam += rota_sayisi(komsu, adim - 1)
        return toplam
    return rota_sayisi


galaksi = {
    "baglantilar": {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "kara_delik": ["sirius"]
    }
}

say_onbelleksiz = onbelleksiz_rota_sayaci(galaksi["baglantilar"])
bas1 = time.perf_counter()
say_onbelleksiz("dünya", 20)
sure_onbelleksiz = time.perf_counter() - bas1

say = rota_sayaci(galaksi["baglantilar"])
bas2 = time.perf_counter()
say("dünya", 20)
sure_onbellekli = time.perf_counter() - bas2

print(f"Önbelleksiz (adim=20): {sure_onbelleksiz:.6f} sn")
print(f"Önbellekli  (adim=20): {sure_onbellekli:.6f} sn")
print("cache_info:", say.cache_info())

say.cache_clear()
print((say("dünya", 3), say("dünya", 10), say("dünya", 40)))


def test_rota_sayaci():
    s = rota_sayaci(galaksi["baglantilar"])
    assert (s("dünya", 3), s("dünya", 10), s("dünya", 40)) == (9, 2185, 16832258606399)
