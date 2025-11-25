#ZAD7

#A Imię
imie = input("Podaj imię: ")
print("Witaj", imie)

#B Wiek
wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

#C Inicjały
im = input("Podaj imię: ")
naz = input("Podaj nazwisko: ")

print(im[0].upper(), naz[0].upper(), sep=".")

#D Wyświetl łańcuch 5 razy
tekst = input("Podaj tekst: ")

for _ in range(5):
    print(tekst)

#E Połączenie dwóch łańcuchów
a = input("Podaj pierwszy tekst: ")
b = input("Podaj drugi tekst: ")

c = a + b
print(c)

#F Połączenie połówek tekstów
a = input("Podaj pierwszy tekst: ")
b = input("Podaj drugi tekst: ")

pol1 = len(a) // 2
pol2 = len(b) // 2

c = a[:pol1] + b[pol2:]
print(c)