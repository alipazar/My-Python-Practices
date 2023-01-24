total= 0
while True:
    sayi = input("Sayi:")
    if sayi == "q":
        break
    sayi= int(sayi)
    total += sayi
print("Girdiginiz sayilarin toplami:",total)