#ZAD5

a = float(input("Podaj długość pierwszego boku prostokąta (a): "))
if a <= 0: print( "Wpisano nieprawidłową wartość")
b = float(input("Podaj długość drugiego boku prostokąta (b): "))
if b <= 0: print( "Wpisano nieprawidłową wartość")


O=2*(a+b)
P=a*b

print(f"Obwód prostokąta= {O}")
print(f"Pole prostokąta= {P}")
# jak upewnic sie ze user wpisuje liczby

'''
Funkcja input() pobiera dane od użytkownika, które wpisze w konsoli, w tym przypadku musi być wpisana liczba rzeczywista
Wystarczy wpisać treść pytania jako argument funkcji input()
'''

