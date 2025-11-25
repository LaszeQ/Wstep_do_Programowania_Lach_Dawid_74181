#ZAD4
n = int(input("Podaj liczbę n: "))
silnia = 1
for i in range(1, n+1):
    silnia *= i
print(f"Silnia z {n} wynosi: {silnia}")