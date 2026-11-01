# Görev 1 - Üçgen analizörü
# Halil İbrahim Arslan 20253004034

import math

k1 = float(input("a: "))
k2 = float(input("b: "))
k3 = float(input("c: "))

if k1 <= 0 or k2 <= 0 or k3 <= 0 or (k1 + k2 <= k3) or (k1 + k3 <= k2) or (k2 + k3 <= k1):
    print("Geçersiz üçgen: Kenarlar pozitif olmalı ve üçgen eşitsizliğini sağlamalıdır.")
else:
    if k1 >= k2 and k1 >= k3:
        a = k1
        b = k2
        c = k3
    elif k2 >= k1 and k2 >= k3:
        a = k2
        b = k1
        c = k3
    else:
        a = k3
        b = k1
        c = k2

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
