# Görev 1 - Süre ölçen dekoratör
# Halil İbrahim Arslan 20253004034

import time
from functools import wraps


def sure_olc(fonksiyon):
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{fonksiyon.__name__}: {sure:.4f} sn")
        return sonuc
    return sarmalayici


def rota(adim):
    if adim <= 1:
        return 1
    return rota(adim - 1) + rota(adim - 2)


@sure_olc
def rota_sayaci(adim=20):
    """Rota sayısını hesaplar."""
    return rota(adim)


@sure_olc
def topla(a, b=0):
    """İki sayıyı toplar."""
    return a + b


def test_sonuc_degismeden_donuyor():
    assert topla(3, 5) == 8


def test_adli_argumanlarla_cagri():
    assert topla(a=10, b=20) == 30


def test_isim_ve_doc_korunuyor():
    assert topla.__name__ == "topla"
    assert topla.__doc__ == "İki sayıyı toplar."


rota_sayaci(adim=20)
