#ZAD10

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

start = min(a, b)
koniec = max(a, b)

for i in range(start, koniec + 1):
    print(i)