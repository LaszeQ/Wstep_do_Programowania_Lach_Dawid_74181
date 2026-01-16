def przedstaw_sie(imie, wiek=20):
    """Funkcja wypisuje imię oraz wiek użytkownika na ekranie."""
    print(f"Imię: {imie}, Wiek: {wiek}")

# a) Wyświetlenie opisu __doc__
print(przedstaw_sie.__doc__)

# b) Wywołanie bez podania wieku
przedstaw_sie("Jan")