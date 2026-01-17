import math
import cmath

# a) Pierwiastek z 81
print(f"a) sqrt(81) = {math.sqrt(81)}")

# b) 8 do potęgi 10
print(f"b) 8^10 = {math.pow(8, 10)}")

# c) Suma pierwiastków
wynik_c = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
print(f"c) sqrt(2)+sqrt(3)+sqrt(6) = {wynik_c}")

# d) Pierwiastek z -5
print(cmath.sqrt(-5))

# e) Pierwiastek trzeciego stopnia z 125
# Można użyć potęgowania odwrotnego: 125^(1/3)
wynik_e = math.pow(125, 1.0/3)
print(f"e) 125^(1/3) = {wynik_e}")