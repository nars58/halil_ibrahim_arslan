# Görev 1 - E-posta doğrulayıcı
# Halil İbrahim Arslan 20253004034


def eposta_denetle(adres):
    adres = adres.strip()

    if adres.count("@") != 1:
        return "Tam olarak bir @ olmalı"

    konum = adres.find("@")
    kullanici = adres[:konum]
    alan = adres[konum + 1:]

    if kullanici == "":
        return "Kullanıcı adı boş olamaz"

    for karakter in kullanici:
        if not (karakter.isalnum() or karakter == "." or karakter == "_" or karakter == "-"):
            return f"Geçersiz karakter: '{karakter}'"

    if kullanici.startswith(".") or kullanici.endswith("."):
        return "Nokta ile başlayamaz/bitemez"

    if alan.find(".") == -1 or alan.startswith(".") or alan.endswith("."):
        return "Alan adı hatalı"

    if adres.find("..") != -1:
        return "İki nokta yan yana olamaz"

    return "Geçerli"


print("ece.yilmaz@nisantasi.edu.tr", eposta_denetle("ece.yilmaz@nisantasi.edu.tr"))
print("ece@@mail.com              ", eposta_denetle("ece@@mail.com"))
print("ece yilmaz@mail.com        ", eposta_denetle("ece yilmaz@mail.com"))
print(".ece@mail.com              ", eposta_denetle(".ece@mail.com"))
print("ece@mail                   ", eposta_denetle("ece@mail"))
