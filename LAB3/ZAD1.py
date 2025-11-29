#ZAD1
Lista_imiona = ["Basia","Asia","Marek","Ola"]
print(Lista_imiona)
for imie in Lista_imiona:
    print(imie)

#A
posortowane = sorted(Lista_imiona)
print(posortowane)

#B
Lista_imiona.append("Krzysiek")
Lista_imiona.append("Wojtek")
print(Lista_imiona)

ostatni = Lista_imiona.pop()
print(ostatni)
print(posortowane)

#C
posortowane.insert(0,"Krzysiek")

