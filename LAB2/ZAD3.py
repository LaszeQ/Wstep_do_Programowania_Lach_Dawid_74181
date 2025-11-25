#ZAD3

n = int(input("Podaj dowolną liczbę naturalną (n): "))
a = float(input("Podaj dowolną liczbę rzeczywistą (a): "))
r = float(input("Podaj dowolną liczbę rzeczywistą (r): "))

#wzor na n-ty element ciagu arytmetycznego  an = a1 + (n-1)r

print("Elementy ciągu arytmetycznego: ")
for i in range(n):
    wartosc = a + (i * r)
    print(f"Wyraz {i + 1}: {wartosc}")
