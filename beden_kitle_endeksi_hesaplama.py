print("""
*********************
Beden Kitle Endeksi Hesaplama Programi
*********************
""")
boy= float(input("Boyunuzu giriniz:"))
kilo= int(input("Kilonuzu giriniz:"))
bki= kilo / (boy ** 2)
if bki < 18.5:
    print("Zayif")
elif bki >= 18.5 and bki < 25:
    print("Normal")
elif bki >= 25 and bki < 30:
    print("Fazla Kilolu")
else:
    print("Obez")
