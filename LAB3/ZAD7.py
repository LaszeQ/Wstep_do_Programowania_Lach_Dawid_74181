# Losowanie wielkości zbiorów
# Zadanie 7
import random
a = random.randint(3, 7)
b = random.randint(3, 7)

# Tworzenie zbiorów - używam pętli i add
X = set()
for i in range(a):
    X.add(random.randint(0, 10))

Y = set()
for i in range(b):
    Y.add(random.randint(0, 10))

print("Zbiór X:", X)
print("Zbiór Y:", Y)

# a) Czy X zawiera 5
if 5 in X:
    print("a) X zawiera 5")
else:
    print("a) X nie zawiera 5")

# b) Czy X podzbiorem Y
print("b) Czy X podzbiór Y?", X.issubset(Y))

# c) Czy Y podzbiorem X
print("c) Czy Y podzbiór X?", Y.issubset(X))

# d) Suma zbiorów (wszystkie elementy razem)
print("d) Suma:", X.union(Y)) # albo X | Y

# e) Różnica X - Y (elementy z X których nie ma w Y)
print("e) Różnica X-Y:", X.difference(Y)) # albo X - Y

# f) Różnica Y - X
print("f) Różnica Y-X:", Y.difference(X))

# g) Iloczyn (część wspólna)
print("g) Iloczyn:", X.intersection(Y)) # albo X & Y

# h) Najwyższy element w obu
# Łączę zbiory i szukam maxa
wszystkie = X.union(Y)
if len(wszystkie) > 0:
    print("h) Największy element:", max(wszystkie))

# i) Usuń z X pierwszy element i daj do Y
if len(X) > 0:
    element = X.pop() # pop w zbiorze usuwa losowy element (bo zbiór nie ma kolejności)
    Y.add(element)
    print(f"i) Przeniesiono {element}. X teraz: {X}, Y teraz: {Y}")

# j) Kopiowanie X do Y
Y.update(X) # dodaje wszystkie elementy z X do Y
print("j) Po skopiowaniu X do Y:", Y)

# k) Czyszczenie
X.clear()
Y.clear()
print("k) Wyczyszczone:", X, Y)
