import math


def pole_trojkata(a, b, c):
    try:
        # Sprawdzenie warunku trójkąta
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Boki muszą być dodatnie.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Z podanych boków nie można zbudować trójkąta.")

        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return pole
    except Exception as e:
        return f"Błąd: {e}"


print(f"Pole trójkąta: {pole_trojkata(3, 4, 5)}")