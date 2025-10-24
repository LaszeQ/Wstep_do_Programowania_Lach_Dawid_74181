#ZAD7
import random

cena_paliwa = 6.5 # zł/l
spalanie = float(input(f"Podaj średnie spalanie swojego samochodu (w litrach na 100km)\n"))
droga = random.randint(10,1000)
zużycie_paliwa = droga / 100 * spalanie
koszt_podróży = zużycie_paliwa * cena_paliwa

print(f"Losowa długość drogi wynosi: {droga} kilometrów\n"f"Przewidywane zużycie paliwa wynosi: {zużycie_paliwa} litrów\n"f"Przewidywany koszt podróży wynosi: {koszt_podróży} złotych")

'''
Wartości generowane przez funkcję randint() z biblioteki 'random' są pseudolosowe, dzieje się tak, ponieważ są one tworzone za pomocą deterministycznych algorytmów 
które są inicjowane przez "ziarno" (seed), oznacza to, że jeśli użyje się tego samego ziarna, ciąg wygenerowanych liczb będzie zawsze taki sam.
'''
