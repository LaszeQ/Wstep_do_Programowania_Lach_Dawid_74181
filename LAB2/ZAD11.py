#ZAD11

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą: "))

start = min(a, b)
koniec = max(a, b)

for i in range(start, koniec + 1):
    if i % 2 != 0:
        continue
    print(i)