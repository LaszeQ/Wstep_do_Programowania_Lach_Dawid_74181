#ZAD2
#A
n = int(input("Podaj liczbę wierszy: "))
for i in range(n):
    print("* " * n)

#B
n = int(input("Podaj liczbę wierszy: "))
for i in range(1, n + 1):
    print("* " * i)

#C
n = int(input("Podaj liczbę wierszy: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)