# Program do rozwiązywania równania kwadratowego: a*x^2 + b*x + c = 0

# Funkcja input() pobiera dane od użytkownika, a float() zamienia je na liczby rzeczywiste.
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

# Sprawdzamy, czy równanie jest kwadratowe (a ≠ 0)
if a == 0:
    print("\nTo nie jest równanie kwadratowe!")
    # w tym przypadku równanie jest liniowe: bx + c = 0
    if b != 0:
        x = -c / b
        print(f"Równanie liniowe ma jedno rozwiązanie: x = {x}")
    elif c == 0:
        print("Równanie tożsamościowe – nieskończenie wiele rozwiązań.")
    else:
        print("Równanie sprzeczne – brak rozwiązań.")
else:
    # Obliczamy deltę
    delta = b**2 - 4*a*c
    print(f"\nΔ (delta) = {delta}")

    if delta > 0:
        # Dwa rozwiązania rzeczywiste
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        print(f"Dwa rozwiązania rzeczywiste:")
        print(f"x₁ = {x1}")
        print(f"x₂ = {x2}")
    elif delta == 0:
        # Jedno rozwiązanie (podwójny pierwiastek)
        x = -b / (2*a)
        print(f"Jedno rozwiązanie podwójne: x = {x}")
    else:
        # Brak rozwiązań rzeczywistych
        print("Brak rozwiązań rzeczywistych (delta < 0).")