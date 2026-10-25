# Görev 4 - Komut sistemi: kayıt deseni
# Halil İbrahim Arslan 20253004034

import pytest

KOMUTLAR = {}


def komut(ad, aciklama=""):
    def dekorator(fonksiyon):
        if ad in KOMUTLAR:
            raise ValueError(f"{ad} komutu zaten var")
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon
    return dekorator


@komut("envanter", "eşyalarını gösterir")
def envanter(durum):
    return f"Kredi: {durum['credits']}, Motor: {durum['engines']}, Yardımcı Pilot: {durum['copilot']}"


@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum):
    return ", ".join(durum["baglantilar"])


@komut("yardim", "komutları listeler")
def yardim(durum):
    satirlar = []
    for ad in KOMUTLAR:
        fonk, aciklama = KOMUTLAR[ad]
        satirlar.append(f"{ad:<10}{aciklama}")
    return "\n".join(satirlar)


def travel(durum):
    gezegenler = durum["baglantilar"]
    while True:
        print("Nereye gitmek istersin?")
        for i in range(len(gezegenler)):
            print(f"[{i + 1}] {gezegenler[i]}")
        girdi = input("> ")
        if girdi in KOMUTLAR:
            fonk, aciklama = KOMUTLAR[girdi]
            print(fonk(durum))
        else:
            secim = int(girdi) - 1
            durum["konum"] = gezegenler[secim]
            return durum["konum"]


durum = {
    "konum": "dünya",
    "baglantilar": ["orion", "dünya", "kara_delik"],
    "credits": 100,
    "engines": "iyon",
    "copilot": "aktif"
}


def test_yardim():
    assert "yardim" in yardim(durum)


def test_envanter():
    assert "100" in envanter(durum)


def test_harita():
    assert harita(durum) == "orion, dünya, kara_delik"


def test_ayni_isim_hatasi():
    with pytest.raises(ValueError):
        @komut("yardim", "tekrar")
        def baska_yardim(d):
            return ""
