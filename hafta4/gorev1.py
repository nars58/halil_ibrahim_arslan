# Görev 1 - Fibonacci üreteci
# Halil İbrahim Arslan 20253004034

from itertools import islice, takewhile


def fibonacci():
    """Sonsuz Fibonacci sayı dizisi üretir."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


g = fibonacci()
ilk_uc = (next(g), next(g), next(g))
ilk_oniki = list(islice(fibonacci(), 12))
yuzden_kucuk = list(takewhile(lambda x: x < 100, fibonacci()))

print(ilk_uc)
print(ilk_oniki)
print(yuzden_kucuk)


def test_fibonacci_degerleri():
    uretec = fibonacci()
    assert (next(uretec), next(uretec), next(uretec)) == (0, 1, 1)
    assert list(islice(fibonacci(), 12)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(takewhile(lambda x: x < 100, fibonacci())) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_tek_kullanimlik():
    uretec = fibonacci()
    birinci = list(islice(uretec, 5))
    ikinci = list(islice(uretec, 5))
    assert birinci != ikinci
