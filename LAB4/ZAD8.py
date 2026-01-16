#ZAD8

def potega(a, n):
    if n == 0:
        return 1
    return a * potega(a, n - 1)

print(f"2^5 = {potega(2, 5)}")