sayi = int(input("Sayi:"))

i = 1
toplam = 0
while i < sayi:
    if (sayi % i == 0):
        toplam += i
    i += 1

if toplam == sayi:
    print(sayi,"mukemmel bir sayidir.")
else:
    print(sayi,"mukemmel bir sayi degildir.")