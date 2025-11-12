
x = float(input("Podaj wartość x: "))

# a) Funkcja a(x)
if x > 0:
    a = 2 * x
elif x == 0:
    a = 0
else:
    a = -3 * x

# b) Funkcja b(x)
if x >= 1:
    b = x ** 2
else:
    b = x

# c) Funkcja c(x)
if x > 2:
    c = 2 + x
elif x == 2:
    c = 8
else:
    c = x - 4

print("\nWyniki funkcji dla x =", x)
print(f"a(x) = {a}")
print(f"b(x) = {b}")
print(f"c(x) = {c}")