#wiek = input("Cześć, ile masz lat? ")
#if wiek <= 0 or wiek >= 4: print

# Funkcja input() pobiera dane od użytkownika z klawiatury
# i może też od razu wyświetlać pytanie, bez potrzeby użycia print().

while True:
    try:
        wiek = int(input("Podaj swój wiek (w pełnych latach): "))
        if wiek < 0:
            print("Wiek nie może być ujemny. Spróbuj ponownie.")
            continue
        break
    except ValueError:
        print("Podaj liczbę całkowitą!")

# Dla dorosłych sprawdzimy, czy są studentami
czy_student = "nie"
if wiek >= 18:
    czy_student = input("Czy jesteś studentem? (tak/nie): ").strip().lower()

# Logika ustalania ceny biletu
if wiek < 4:
    cena = 0
elif 4 <= wiek < 18:
    cena = 10
elif wiek >= 18 and czy_student == "tak":
    cena = 20 * 0.75  # 25% zniżki
else:
    cena = 20

print(f"\nCena biletu: {cena:.2f} zł")
