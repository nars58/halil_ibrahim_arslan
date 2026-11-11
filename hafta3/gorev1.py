# Görev 1 - Saf fonksiyonlar çıkar
# Halil İbrahim Arslan 20253004034


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Oyuncunun sahip olduğu eşyaları metin olarak döndürür."""
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")
    if len(esyalar) == 0:
        return ""
    return "Sende: " + ", ".join(esyalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek gezegenlerin numaralı menüsünü döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for i in range(len(hedefler)):
        satirlar.append(f"[{i + 1}] {hedefler[i]}")
    return "\n".join(satirlar)


def travel(hedefler: list[str], credits: bool, engines: bool, copilot: bool) -> str:
    """Envanter metnini ve hedef menüsünü kullanarak yolculuk seçimini yapar."""
    metin = envanter_metni(credits, engines, copilot)
    if metin != "":
        print(metin)
    print(hedef_menusu(hedefler))
    secim = int(input("Seçim: ")) - 1
    return hedefler[secim]


def test_envanter_metni():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"
    assert envanter_metni(False, False, False) == ""


def test_hedef_menusu():
    assert hedef_menusu(["centauri", "sirius"]) == "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"


print(envanter_metni(True, False, True))
print(envanter_metni(False, False, False))
print(hedef_menusu(["centauri", "sirius"]))
