# Görev 4 - Kesir sınıfı v2
# Halil İbrahim Arslan 20253004034


class Kesir:
    def __init__(self, pay, payda=1):
        if payda == 0:
            raise ValueError("Payda 0 olamaz")
        if payda < 0:
            pay = -pay
            payda = -payda
        a = abs(pay)
        b = abs(payda)
        while b != 0:
            a, b = b, a % b
        self.pay = pay // a
        self.payda = payda // a

    def __str__(self):
        if self.payda == 1:
            return f"{self.pay}"
        return f"{self.pay}/{self.payda}"

    def __add__(self, diger):
        return Kesir(self.pay * diger.payda + diger.pay * self.payda, self.payda * diger.payda)

    def __sub__(self, diger):
        return Kesir(self.pay * diger.payda - diger.pay * self.payda, self.payda * diger.payda)

    def __mul__(self, diger):
        return Kesir(self.pay * diger.pay, self.payda * diger.payda)

    def __truediv__(self, diger):
        return Kesir(self.pay * diger.payda, self.payda * diger.pay)

    def __eq__(self, diger):
        return self.pay * diger.payda == diger.pay * self.payda

    def __lt__(self, diger):
        return self.pay * diger.payda < diger.pay * self.payda

    def __le__(self, diger):
        return self.pay * diger.payda <= diger.pay * self.payda

    def __float__(self):
        return self.pay / self.payda


carpim = Kesir(1, 1)
for n in range(2, 11):
    carpim = carpim * (Kesir(1, 1) - Kesir(1, n))

kesir1 = Kesir(3, 7)
kesir2 = Kesir(5, 12)
kesir3 = Kesir(2, 5)
kesir4 = Kesir(4, 9)
kesir5 = Kesir(3, 8)

en_buyuk = kesir1
if en_buyuk < kesir2:
    en_buyuk = kesir2
if en_buyuk < kesir3:
    en_buyuk = kesir3
if en_buyuk < kesir4:
    en_buyuk = kesir4
if en_buyuk < kesir5:
    en_buyuk = kesir5

print(f"Çarpım: {carpim}        En büyük: {en_buyuk}")
print(f"Kesir(6, 8) == Kesir(3, 4) -> {Kesir(6, 8) == Kesir(3, 4)}    Kesir(3, 4) / Kesir(3, 8) -> {Kesir(3, 4) / Kesir(3, 8)}")
