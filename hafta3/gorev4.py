# Görev 4 - Tuzaklar ve kapsam
# Halil İbrahim Arslan 20253004034


def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Yakıt deposuna miktar ekler ve güncel listeyi döndürür."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle():
    birinci = yakit_ekle(10)
    ikinci = yakit_ekle(20)
    assert birinci == [10]
    assert ikinci == [20]


print(yakit_ekle(10))
print(yakit_ekle(20))
