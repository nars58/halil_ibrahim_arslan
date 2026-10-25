# Görev 5 - Argüman alan dekoratör
# Halil İbrahim Arslan 20253004034

from functools import wraps
import pytest


def sinirla(alt, ust):
    def dekorator(fonksiyon):
        @wraps(fonksiyon)
        def sarmalayici(*args, **kwargs):
            deger = args[0]
            if deger < alt or deger > ust:
                raise ValueError(f"{fonksiyon.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
            return fonksiyon(*args, **kwargs)
        return sarmalayici
    return dekorator


@sinirla(0, 100)
def yakit_harca(miktar):
    return 100 - miktar


def test_normal_deger():
    assert yakit_harca(30) == 70


def test_sinir_alt():
    assert yakit_harca(0) == 100


def test_sinir_ust():
    assert yakit_harca(100) == 0


def test_aralik_disi_alt():
    with pytest.raises(ValueError):
        yakit_harca(-10)


def test_aralik_disi_ust():
    with pytest.raises(ValueError):
        yakit_harca(150)


print(yakit_harca(30))
