# Görev 1 - Üçgen analizörü
# Halil İbrahim Arslan 20253004034

import math

kenar1 = float(input("a: "))
kenar2 = float(input("b: "))
kenar3 = float(input("c: "))

if kenar1 <= 0 or kenar2 <= 0 or kenar3 <= 0 or (kenar1 + kenar2 <= kenar3) or (kenar1 + kenar3 <= kenar2) or (kenar2 + kenar3 <= kenar1):
    print("Geçersiz üçgen: Kenarlar pozitif olmalı ve üçgen eşitsizliğini sağlamalıdır.")
else:
    if kenar1 >= kenar2 and kenar1 >= kenar3:
        a = kenar1
        b = kenar2
        c = kenar3
    elif kenar2 >= kenar1 and kenar2 >= kenar3:
        a = kenar2
        b = kenar1
        c = kenar3
    else:
        a = kenar3
        b = kenar1
        c = kenar2

    if a == b and b == c:
        kenar_turu = "Eşkenar"
    elif a == b or b == c or a == c:
        kenar_turu = "İkizkenar"
    else:
        kenar_turu = "Çeşitkenar"

    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - a) * (u - b) * (u - c))
    cos_alfa = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    aci = math.degrees(math.acos(cos_alfa))

    if math.isclose(aci, 90):
        aci_turu = "Dik açılı"
    elif aci < 90:
        aci_turu = "Dar açılı"
    else:
        aci_turu = "Geniş açılı"

    print(f"Tür: {kenar_turu}, {aci_turu}")
    print(f"Çevre: {cevre:.2f} Alan: {alan:.2f} En büyük açı: {aci:.2f}°")
