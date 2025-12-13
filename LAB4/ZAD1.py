#ZAD1
def poleK(r, pi=3.14):
    pole = pi * r ** 2
    # wyświetla pole koła
    print(f"Koło o promieniu {r} ma pole: {pole}.")
    # zwrócenie wartości w miejsce wywołania
    return pole

print(poleK(3))