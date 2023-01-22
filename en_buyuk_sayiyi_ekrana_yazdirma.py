print("""
**********************************************
En Buyuk Sayiyi Ekrana Yazdirma Programi
**********************************************
""")
print("Sayilari sirayla giriniz.")


a= int(input("1:"))
b= int(input("2:"))
c= int(input("3:"))

if a>=b and a>=c:
    print("En buyuk sayi:",a)
elif b>=a and b>=c:
    print("En buyuk sayi:",b)
else:
    print("En buyuk sayi:",c)