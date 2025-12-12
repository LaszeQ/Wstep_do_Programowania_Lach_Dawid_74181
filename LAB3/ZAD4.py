#ZAD4
import random


n = int(input("Jak długa ma być ta lista: "))
x = int(input("Jak długie mogą to być słowa: "))
lista=[]
d=0
z=0
slowo=''
alfabet = ["a","k","m","p","t"]

for i in range(n):
    d =random.randint(1,x)
    slowo=''
    for j in range(d):
        z=random.randint(0,len(alfabet)-1)
        slowo+=alfabet[z]
#        print(slowo)
#    lista.append(f"el. {i} o dlugosci {d}: {slowo}")
    lista.append(slowo)
print(lista)
krotka=tuple(lista)

#A
suma=0
# for slowo in krotka
for i in range(n):
    suma+=len(krotka[i])
print(suma)

#B
# ile razy występuje "k"?

suma_k=0
for i in krotka:
    for znak in slowo:
        if znak =="k":
            suma_k+=1
print(suma_k)

#C
licznik_kt = 0
for napis in krotka:
    licznik_kt += napis.count('kt')
print("c) Ilość ciągów 'kt':", licznik_kt)

#D
s = int(input("Podaj długość s do porównania: "))
dluzsze_niz_s = 0
for napis in krotka:
    if len(napis) > s:
        dluzsze_niz_s += 1
print(f"d) Ilość ciągów dłuższych niż {s}:", dluzsze_niz_s)
#s = input
# for
# if dlugosc_slowa > s