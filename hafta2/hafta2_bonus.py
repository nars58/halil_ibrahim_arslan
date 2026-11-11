#HALİL İBRAHİM ARSLAN - 20253004034
# 02/10/2026
# bileşik faiz yatırımının gelecekteki değerini hesaplama ve round kullanarak yuvarlama programı.
# 1 gün=86400sn 1 saat=3600sn 1 dakika=60sn

gun=int(input("Gün sayısını girin:"))
saat=int(input("Saat sayısını girin:"))
dakika=int(input("Dakika sayısını girin:"))
saniye=int(input("Saniye sayısını girin:"))

topsaniye=(gun*86400)+(saat*3600)+(dakika*60)+saniye
print(f"{topsaniye}saniye")