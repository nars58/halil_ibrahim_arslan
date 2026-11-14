# Görev 3 - Seyir defteri boru hattı
# Halil İbrahim Arslan 20253004034


def satirlari_oku(yol: str):
    """Dosyadaki boş ve # ile başlayan satırları atlayarak satırları üretir."""
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz = satir.strip()
            if temiz == "" or temiz.startswith("#"):
                continue
            yield temiz


def ayristir(satirlar):
    """Her satırdan (kaynak, hedef, yakit) demeti üretir."""
    for satir in satirlar:
        parcalar = satir.split()
        yield (parcalar[0], parcalar[2], int(parcalar[3]))


def uzun_yolculuklar(kayitlar, esik: int):
    """Yakıtı verilen eşikten büyük olan kayıtları üretir."""
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield (kaynak, hedef, yakit)


dosya_yolu = "hafta4/veri/seyir.txt"
toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(dosya_yolu)))
print(toplam_yakit)

kayitlar = ayristir(satirlari_oku(dosya_yolu))
hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
print(hedefler)


def test_seyir_boru_hatti():
    assert sum(y for _, _, y in ayristir(satirlari_oku(dosya_yolu))) == 88
    k = ayristir(satirlari_oku(dosya_yolu))
    assert [h for _, h, _ in uzun_yolculuklar(k, 10)] == ["sirius", "centauri", "orion", "kara_delik"]
