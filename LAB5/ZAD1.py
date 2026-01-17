import random
# a) Szczęśliwy numerek (zakładając grupę 30 osób)
szczesliwy_numerek = random.randint(1, 30)
print(f"Szczęśliwy numerek: {szczesliwy_numerek}")

# b) Szczęśliwy rocznik
roczniki = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004]
szczesliwy_rocznik = random.choice(roczniki)
print(f"Szczęśliwy rocznik: {szczesliwy_rocznik}")

# c) Symulacja Dużego Lotka (6 kul z 49)

wynik_lotto = random.sample(range(1, 50), 6)
wynik_lotto.sort() # sortowanie dla czytelności
print(f"Wyniki lotto: {wynik_lotto}")