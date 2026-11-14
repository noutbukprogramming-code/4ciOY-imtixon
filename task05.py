import json

with open("inventar.json", "r") as fayl:
    inventar = json.load(fayl)

    natija = []

    for kitob in inventar:
        mavjud = kitob["jami"] - kitob["band"]

        natija.append({
            "nom": kitob["nom"],
            "mavjud": mavjud
        })

        print(f"{kitob['nom']}: {mavjud} ta mavjud")

    with open("mavjud_kitoblar.json", "w") as fayl:
        json.dump(natija, fayl, indent=4)

    print(f"{len(natija)} ta yozuv saqlandi.")

