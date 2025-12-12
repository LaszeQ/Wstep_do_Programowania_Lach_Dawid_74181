#ZAD2
zdanie = input("Podaj zdanie: ")

#A
# Używam prostego alfabetu jako stringa
alfabet = "abcdefghijklmnopqrstuvwxyz"
znalezione = []

# Szukam liter w zdaniu
for znak in zdanie.lower():
    if znak in alfabet:
        # Dodaję tylko jeśli jeszcze nie ma na liście
        if znak not in znalezione:
            znalezione.append(znak)

znalezione.sort()
print("a) Znalezione litery:", found_str := "".join(znalezione)) # mały trick żeby ładnie wypisać

# Szukam brakujących
brakujace = []
for litera in alfabet:
    if litera not in znalezione:
        brakujace.append(litera)
print("   Brakujące litery:", "".join(brakujace))


# b) Usuwanie znaków o nieparzystych indeksach
# Najprościej użyć wycinania (slicing) co 2, zaczynając od 0 (parzyste zostają)
samo_parzyste = zdanie[::2]
print("b) Tylko znaki o parzystych indeksach:", samo_parzyste)


# c) Każdy wyraz z wielkiej litery na początku i końcu
wyrazy = zdanie.split() # dzieli zdanie na listę słów
nowe_zdanie = []

for slowo in wyrazy:
    if len(slowo) > 1:
        # Pierwsza litera duża + środek + ostatnia duża
        nowe_slowo = slowo[0].upper() + slowo[1:-1] + slowo[-1].upper()
        nowe_zdanie.append(nowe_slowo)
    else:
        # Jak słowo ma 1 literę (np. "i"), to tylko powiększamy
        nowe_zdanie.append(slowo.upper())

print("c) Zmienione wyrazy:", " ".join(nowe_zdanie))


# d) Najdłuższe słowo
najdluzsze = ""
for slowo in wyrazy:
    if len(slowo) > len(najdluzsze):
        najdluzsze = slowo

print("d) Najdłuższe słowo:", najdluzsze)
print("   Jego długość:", len(najdluzsze))


# e) Zamiana powtórek na @
# Robię pusty napis i dodaję znaki, sprawdzając czy już były
wynik_e = ""
juz_byly = [] # lista pomocnicza

for znak in zdanie:
    if znak in juz_byly:
        wynik_e = wynik_e + "@"
    else:
        wynik_e = wynik_e + znak
        juz_byly.append(znak) # zapamiętuję, że ten znak już wystąpił

print("e) Bez powtórzeń:", wynik_e)