sekil= input("Hangi geometrik sekli ogrenmek istiyorsunuz?:")
if sekil == "Dortgen":
    print("Lutfen kenarlari giriniz:")
    a= int(input("Kenar1"))
    b= int(input("Kenar2"))
    c= int(input("Kenar3"))
    d= int(input("Kenar4"))
    if a == b and a==c and a==d:
        print("Kare")
    elif a == c and b == d:
        print("Dikdortgen")
    else:
        print("Dortgen")

elif sekil == "Ucgen":
    print("Lutfen kenarlari giriniz:")
    a= int(input("Kenar1"))
    b= int(input("Kenar2"))
    c= int(input("Kenar3"))
    if abs(a+b) > c and abs(a+c) > b and abs(b+c) > a:
        if a == b and a == c:
            print("Eskenar ucgen")
        elif a == b and a != c or a == c and a != b or b == c and b != a:
            print("Ikizkenar ucgen")
        else:
            print("Cesitkenar ucgen")
    else:
        print("Ucgen belirten islem girmediniz!")
else:
    print("Gecersiz islem girdiniz!")

