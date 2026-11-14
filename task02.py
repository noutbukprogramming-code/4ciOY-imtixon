haroratlar = [-20, -19, -17, -16, -18, -21, -15, -14, -20]

xavfli = 0

for harorat in haroratlar:
    if harorat > -18:
        xavfli += 1

ortacha = sum(haroratlar) / len(haroratlar)

print(f"Xavfli o'lchovlar: {xavfli} ta")
print(f"O'rtacha harorat: {ortacha:.2f}°C")