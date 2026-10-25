# Bonus - Sözlük tabanlı hafıza dekoratörü
# Halil İbrahim Arslan 20253004034

from functools import wraps, lru_cache


def hafiza(maxsize=None):
    def dekorator(fonksiyon):
        sozluk = {}

        @wraps(fonksiyon)
        def sarmalayici(*args):
            if args in sozluk:
                return sozluk[args]
            sonuc = fonksiyon(*args)
            if maxsize is not None and len(sozluk) >= maxsize:
                eski_anahtar = list(sozluk.keys())[0]
                del sozluk[eski_anahtar]
            sozluk[args] = sonuc
            return sonuc

        return sarmalayici
    return dekorator


@hafiza(maxsize=None)
def fib_hafiza(n):
    if n < 2:
        return n
    return fib_hafiza(n - 1) + fib_hafiza(n - 2)


@lru_cache(maxsize=None)
def fib_lru(n):
    if n < 2:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


def test_hafiza_ve_lru_karsilastir():
    for i in range(20):
        assert fib_hafiza(i) == fib_lru(i)
