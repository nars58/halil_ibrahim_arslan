#HALİL İBRAHİM ARSLAN - 20253004034
# 02/10/2026
#  kullanıcının girdiği saniyeyi gün ,saat,dakika,saniyeye çevirme programı

saniye=int(input("saniye giriniz:"))
#1dk=60sn 1saat=3600sn 1gün=86400sn

gun=saniye//86400
kalan=saniye%86400

saat=kalan//3600
kalan=kalan%3600

dakika=kalan//60
kalan=kalan%60

saniye=kalan

print(f"{gun} Gün ,{saat} Saat,{dakika} Dakika,{saniye} Saniye")