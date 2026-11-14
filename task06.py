import csv

natija = {}

with open("qatnov.csv", "r") as fayl:
    reader = csv.DictReader(fayl)

    for qator in reader:
        yonalish = qator["yonalish"]
        yolovchi = int(qator["yolovchi"])

        if yonalish not in natija:
            natija[yonalish] = 0

        natija[yonalish] += yolovchi


for yonalish, jami in natija.items():
    print(f"{yonalish}-yo'nalish: {jami} nafar")