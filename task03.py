def tekshir(kod):
    kod = kod.strip()

    qismlar = kod.split("-")

    if len(qismlar) != 3:
        return "yaroqsiz"

    davlat = qismlar[0]
    yil = qismlar[1]
    seriya = qismlar[2]

    if davlat != "UZ":
        return "yaroqsiz"

    if len(yil) != 4 or not yil.isdigit():
        return "yaroqsiz"

    if len(seriya) != 6:
        return "yaroqsiz"

    if not seriya[:2].isalpha():
        return "yaroqsiz"

    if not seriya[:2].isupper():
        return "yaroqsiz"

    if not seriya[2:].isdigit():
        return "yaroqsiz"

    return f"yaroqli | yil: {yil} | seriya: {seriya}"


kodlar = [
    " UZ-2026-AB1234 ",
    "UZ-26-AB1234",
    "UZ-2026-aB1234"
]

for kod in kodlar:
    toza_kod = kod.strip()
    print(f"{toza_kod}: {tekshir(kod)}")