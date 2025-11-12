# Funkcja input() pobiera dane od użytkownika z klawiatury.
# Każdą wartość konwertujemy na float, by obsługiwać także liczby niecałkowite.

x = float(input("Podaj pierwszą liczbę (x): "))
y = float(input("Podaj drugą liczbę (y): "))
z = float(input("Podaj trzecią liczbę (z): "))

# Porządkowanie liczb od najmniejszej do największej
# — wykonamy proste porównania i zamiany miejsc (tzw. sortowanie przez zamianę).

if x > y:
    x, y = y, x  # zamiana wartości
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print("\nLiczby od najmniejszej do największej:")
print(x, y, z)