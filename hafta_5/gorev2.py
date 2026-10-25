# Görev 2 - Çağrı sayacı ve dekoratör sırası
# Halil İbrahim Arslan 20253004034

from functools import wraps, lru_cache


def say(fonksiyon):
    @wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1
        return fonksiyon(*args, **kwargs)
    sarmalayici.cagri = 0
    return sarmalayici


@say
def fib1(n):
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n - 2)


@say
@lru_cache
def fib2(n):
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


@lru_cache
@say
def fib3(n):
    if n < 2:
        return n
    return fib3(n - 1) + fib3(n - 2)


fib1(20)
fib2(20)
fib3(20)

print(f"Yalnızca @say                 : {fib1.cagri}")
print(f"@say üstte, @lru_cache altta: {fib2.cagri}")
print(f"@lru_cache üstte, @say altta: {fib3.__wrapped__.cagri}")
