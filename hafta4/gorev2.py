# Görev 2 - Yakıt göstergesi
# Halil İbrahim Arslan 20253004034

import pytest


def yakit_gostergesi(yakit: int, tuketim: int):
    """Her adımda yakıtı tüketim kadar azaltıp kalan yakıtı üretir."""
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit


def travel(galaksi: dict, adimlar: list[str], tuketim: int = 5) -> str:
    """Gösterge ile yakıtı takip ederek yolculuk yapar."""
    gosterge = yakit_gostergesi(galaksi["yakit"], tuketim)
    for hedef in adimlar:
        try:
            kalan = next(gosterge)
            galaksi["konum"] = hedef
            galaksi["yakit"] = kalan
        except StopIteration:
            return "Yakıtın bitti, uzayda sürükleniyorsun..."
    return galaksi["konum"]


print(list(yakit_gostergesi(100, 30)))


def test_yakit_gostergesi():
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_stop_iteration_ve_travel():
    g = yakit_gostergesi(10, 10)
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)

    galaksi = {"konum": "dünya", "yakit": 10}
    sonuc = travel(galaksi, ["sirius", "orion", "centauri"], tuketim=5)
    assert sonuc == "Yakıtın bitti, uzayda sürükleniyorsun..."
