# Görev 5 - map, filter, reduce ve partial
# Halil İbrahim Arslan 20253004034

from functools import reduce, partial


def buyuk_harfli_map(galaksi: dict) -> list[str]:
    """Gezegen adlarını map kullanarak büyük harfe çevirir."""
    return list(map(lambda g: g.upper(), galaksi["gezegenler"]))


def buyuk_harfli_liste(galaksi: dict) -> list[str]:
    """Gezegen adlarını liste üreteci kullanarak büyük harfe çevirir."""
    return [g.upper() for g in galaksi["gezegenler"]]


def en_az_iki_baglanti_filter(galaksi: dict) -> list[str]:
    """En az iki bağlantısı olan gezegenleri filter ile döndürür."""
    return list(filter(lambda g: len(galaksi["baglantilar"][g]) >= 2, galaksi["gezegenler"]))


def en_az_iki_baglanti_liste(galaksi: dict) -> list[str]:
    """En az iki bağlantısı olan gezegenleri liste üreteci ile döndürür."""
    return [g for g in galaksi["gezegenler"] if len(galaksi["baglantilar"][g]) >= 2]


def toplam_baglanti_reduce(galaksi: dict) -> int:
    """Toplam bağlantı sayısını reduce ile hesaplar."""
    return reduce(lambda toplam, g: toplam + len(galaksi["baglantilar"][g]), galaksi["gezegenler"], 0)


def toplam_baglanti_sum(galaksi: dict) -> int:
    """Toplam bağlantı sayısını sum ile hesaplar."""
    return sum(len(galaksi["baglantilar"][g]) for g in galaksi["gezegenler"])


def yolculuk(hedef: str, hiz: int = 1) -> str:
    """Belirtilen hedefe verilen hızla yolculuk metni döndürür."""
    return f"{hedef} gezegenine hiz={hiz} ile gidiliyor"


hizli_yolculuk = partial(yolculuk, hiz=3)

# Liste üreteci ve sum yazımı, lambda gerektiren map/filter/reduce yazımına göre daha sade ve okunaklıdır.

galaksi = {
    "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
    "baglantilar": {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "kara_delik": ["sirius"]
    }
}

print(buyuk_harfli_map(galaksi))
print(en_az_iki_baglanti_filter(galaksi))
print(toplam_baglanti_reduce(galaksi))


def test_istatistik_ve_partial():
    assert buyuk_harfli_map(galaksi) == ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]
    assert buyuk_harfli_map(galaksi) == buyuk_harfli_liste(galaksi)
    assert en_az_iki_baglanti_filter(galaksi) == ["dünya", "centauri", "sirius", "orion"]
    assert en_az_iki_baglanti_filter(galaksi) == en_az_iki_baglanti_liste(galaksi)
    assert toplam_baglanti_reduce(galaksi) == 10
    assert toplam_baglanti_reduce(galaksi) == toplam_baglanti_sum(galaksi)
    assert hizli_yolculuk("orion") == "orion gezegenine hiz=3 ile gidiliyor"
