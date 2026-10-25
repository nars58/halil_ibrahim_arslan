# Görev 3 - Loglayan dekoratör
# Halil İbrahim Arslan 20253004034

from functools import wraps


def log_cagri(fonksiyon):
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        arg_listesi = []
        for a in args:
            arg_listesi.append(repr(a))
        for k, v in kwargs.items():
            arg_listesi.append(f"{k}={repr(v)}")
        arg_yazisi = ", ".join(arg_listesi)
        print(f"-> {fonksiyon.__name__}({arg_yazisi})")
        sonuc = fonksiyon(*args, **kwargs)
        print(f"<- {fonksiyon.__name__} = {repr(sonuc)}")
        return sonuc
    return sarmalayici


@log_cagri
def yolculuk(hedef, hiz=1):
    return f"{hedef} hiz={hiz}"


@log_cagri
def galaksi_kur():
    return ["orion", "dünya", "kara_delik"]


@log_cagri
def hedef_menusu(gezegenler):
    satirlar = ["Nereye gitmek istersin?"]
    for i in range(len(gezegenler)):
        satirlar.append(f"[{i + 1}] {gezegenler[i]}")
    return "\n".join(satirlar)


def test_yolculuk():
    assert yolculuk("orion", hiz=3) == "orion hiz=3"


def test_galaksi_kur():
    assert galaksi_kur() == ["orion", "dünya", "kara_delik"]


def test_hedef_menusu():
    menu = hedef_menusu(["orion", "dünya", "kara_delik"])
    assert "[1] orion" in menu


yolculuk("orion", hiz=3)
gezegenler = galaksi_kur()
hedef_menusu(gezegenler)
