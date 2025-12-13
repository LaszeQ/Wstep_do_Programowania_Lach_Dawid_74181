def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Przykład użycia
n = int(input("Podaj liczbę elementów ciągu Fibonacciego: "))
print(fibonacci(n))