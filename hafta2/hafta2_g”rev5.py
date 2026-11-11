#HALİL İBRAHİM ARSLAN - 20253004034
# 02/10/2026
# bileşik faiz yatırımının gelecekteki değerini hesaplama ve round kullanarak yuvarlama programı.

a=float(input("Anaparanızı giriniz:"))
r=float(input("yıllık %faiz giriniz:"))
y=float(input("yıl cinsinden süre giriniz "))

g=a*(1+(r/(12*100)))**(12*y)

deger=round(g,2)
print(deger)