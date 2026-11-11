# Görev 3 - Galaksiyi veri dosyasından kur
# Halil İbrahim Arslan 20253004034

import json
import pytest


def galaksi_kur(gezegenler: list[str], baglantilar: dict[str, list[str]], baslangic: str, **kwargs) -> dict:
    """Galaksi verisini doğrular ve oyun başlangıç sözlüğünü döndürür."""
    if baslangic not in gezegenler:
        raise ValueError("Başlangıç gezegeni listede yok.")
    yakit = kwargs.get("yakit", 50)
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }


def travel(galaksi: dict) -> str:
    """Hedefleri galaksi bağlantılarından alarak yolculuk yapar."""
    planet = galaksi["konum"]
    destinations = galaksi["baglantilar"][planet]
    for i in range(len(destinations)):
        print(f"[{i + 1}] {destinations[i]}")
    secim = int(input("Seçim: ")) - 1
    galaksi["konum"] = destinations[secim]
    return galaksi["konum"]


with open("hafta3/galaksi.json", "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)

g = galaksi_kur(**veri)
print((g["konum"], g["yakit"]))
print(galaksi_kur(["mars"], {"mars": []}, "mars")["yakit"])


def test_galaksi_kur():
    assert (g["konum"], g["yakit"]) == ("dünya", 100)
    assert galaksi_kur(["mars"], {"mars": []}, "mars")["yakit"] == 50


def test_hatali_baslangic():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "venüs")
