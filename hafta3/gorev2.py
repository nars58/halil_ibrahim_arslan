# Görev 2 - Esnek parametreler
# Halil İbrahim Arslan 20253004034


def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> str:
    """Görev başlığını, adımlarını ve ek bilgilerini biçimlendirip döndürür."""
    satirlar = [f"[{oncelik.upper()}] {baslik}"]
    for i in range(len(adimlar)):
        satirlar.append(f"  {i + 1}. {adimlar[i]}")
    for anahtar, deger in ekler.items():
        satirlar.append(f"  {anahtar}: {deger}")
    return "\n".join(satirlar)


def test_normal_cagri():
    sonuc = gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", oncelik="yüksek", sorumlu="Ayşe")
    assert "[YÜKSEK] Kara deliğe atla" in sonuc
    assert "1. Kredi kazan" in sonuc
    assert "sorumlu: Ayşe" in sonuc


def test_acarak_cagri():
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    sonuc = gorev_kaydi("Kara deliğe atla", *adim_listesi, oncelik="yüksek", **ek_bilgiler)
    assert "3. Hiperdrive al" in sonuc
    assert "sorumlu: Ayşe" in sonuc


if __name__ == "__main__":
    print(gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al", oncelik="yüksek", sorumlu="Ayşe"))
    print()
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_sozluk = {"sorumlu": "Ayşe"}
    print(gorev_kaydi("Kara deliğe atla", *adim_listesi, oncelik="yüksek", **ek_sozluk))
