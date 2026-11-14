# Bonus - Zamanlayıcı üreteci (Tik-Tak)
# Halil İbrahim Arslan 20253004034

import time


def zamanlayici(aralik: float):
    """Belirtilen süre aralığı dolduğunda True, dolmadığında False üretir."""
    son_tetik = time.perf_counter()
    while True:
        simdi = time.perf_counter()
        if simdi - son_tetik >= aralik:
            son_tetik = simdi
            yield True
        else:
            yield False


def tik_tak_calistir(toplam_sure: float = 10.0) -> None:
    """Belirtilen süre boyunca her 2 saniyede tik, her 5 saniyede tak yazdırır."""
    tik = zamanlayici(2.0)
    tak = zamanlayici(5.0)
    baslangic = time.perf_counter()

    while time.perf_counter() - baslangic <= toplam_sure:
        if next(tik):
            print("tik")
        if next(tak):
            print("tak")


# Açıklama: Bu yöntem döngü içinde sürekli saati kontrol ettiği için işlemciyi boş yere çalıştırır (meşgul bekleme / busy waiting).
# time.sleep ise programı belirtilen süre boyunca uyutarak işlemciyi meşgul etmez.

if __name__ == "__main__":
    tik_tak_calistir(10.0)
