log = " hall-a, HALL-B, hall-a, , hall-c, HALL-B, hall-a "

qismlar = log.split(",")

tozalangan = []

for qism in qismlar:
    qism = qism.strip()

    if qism:
        tozalangan.append(qism.upper())

noyob = set(tozalangan)

print(f"Tozalangan: {', '.join(tozalangan)}")
print(f"Noyob bo‘limlar: {len(noyob)}")