# Prosty kalkulator w Pythonie

# Funkcja input() pobiera dane od użytkownika (jako tekst), więc konwertujemy je na float.
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("\nWybierz działanie:")
print("1. Dodawanie (+)")
print("2. Odejmowanie (-)")
print("3. Mnożenie (*)")
print("4. Dzielenie (/)")

dzialanie = input("Wpisz symbol działania (+, -, *, /): ")

# W Pythonie nie ma instrukcji switch/case (jak w C, C++, Java czy JavaScript).
# Zamiast tego stosuje się serię instrukcji warunkowych if / elif / else.
# Każdy blok elif działa podobnie do "case" w innych językach programowania.

if dzialanie == "+":
    wynik = a + b
    print(f"Wynik: {a} + {b} = {wynik}")

elif dzialanie == "-":
    wynik = a - b
    print(f"Wynik: {a} - {b} = {wynik}")

elif dzialanie == "*":
    wynik = a * b
    print(f"Wynik: {a} * {b} = {wynik}")

elif dzialanie == "/":
    if b == 0:
        print("Błąd: nie można dzielić przez zero!")
    else:
        wynik = a / b
        print(f"Wynik: {a} / {b} = {wynik}")

else:
    print("Nieprawidłowy symbol działania!")