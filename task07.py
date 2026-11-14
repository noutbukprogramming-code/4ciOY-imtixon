import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
sarf = [42, 38, 51, 47, 62, 70, 45]

ortacha = sum(sarf) / len(sarf)

print("O'rtacha sarf:", round(ortacha, 2), "kWh")

print("O'rtachadan yuqori kunlar:")

for i in range(len(sarf)):
    if sarf[i] > ortacha:
        print(kunlar[i], "-", sarf[i], "kWh")

plt.plot(kunlar, sarf, marker="o")

plt.title("Energiya sarfi")
plt.xlabel("Kunlar")
plt.ylabel("kWh")

plt.grid()
plt.show()
