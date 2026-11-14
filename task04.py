xizmatlar = {
    "diagnostika": 50000,
    "tozalash": 80000,
    "sozlash": 40000,
    "almashtirish": 120000
}


def hisobla(*args, **kwargs):
    jami = 0

    for xizmat in args:
        if xizmat in xizmatlar:
            jami += xizmatlar[xizmat]
        else:
            print(f"Ogohlantirish: {xizmat} xizmati topilmadi")

    mijoz = kwargs.get("mijoz", "Noma'lum")
    chegirma = kwargs.get("chegirma", 0)

    chegirma_summa = jami * chegirma / 100
    tolov = jami - chegirma_summa

    print(f"Mijoz: {mijoz}")
    print(f"Xizmatlar jami: {jami:.0f} so'm")
    print(f"Chegirma: {chegirma_summa:.0f} so'm")
    print(f"To'lov: {tolov:.0f} so'm")


hisobla(
    "diagnostika",
    "tozalash",
    "sozlash",
    mijoz="Nodira",
    chegirma=10
)