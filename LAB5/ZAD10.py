import random
import math


def zadanie_10():
    try:
        start = int(input("Podaj początek zakresu: "))
        koniec = int(input("Podaj koniec zakresu: "))

        # Generowanie listy, potem zamiana na krotkę (tuple)
        lista_liczb = [random.randint(start, koniec) for _ in range(10)]
        krotka = tuple(lista_liczb)
        print(f"Wylosowana krotka: {krotka}")

        # Średnia geometryczna: pierwiastek n-tego stopnia z iloczynu liczb
        iloczyn = 1
        for liczba in krotka:
            iloczyn *= liczba

        # Obliczenie pierwiastka 10-tego stopnia (bo 10 elementów)
        srednia_geom = iloczyn ** (1 / 10)
        print(f"Średnia geometryczna: {srednia_geom}")

    except ValueError:
        print("Błąd: Podaj poprawne liczby całkowite.")

zadanie_10()