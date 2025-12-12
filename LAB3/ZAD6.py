#ZAD6
# Rachunki za prąd (miesiąc - kwota)
rachunki = {
    "Styczeń": 120,
    "Luty": 135,
    "Marzec": 110,
    "Kwiecień": 150
}

#A Statystyki
wartosci = list(rachunki.values()) # Wyciągam same kwoty do listy
max_rachunek = max(wartosci)
min_rachunek = min(wartosci)
suma_rachunkow = sum(wartosci)
srednia = suma_rachunkow / len(wartosci)

print(f"a) Max: {max_rachunek}, Min: {min_rachunek}, Suma: {suma_rachunkow}, Średnia: {srednia}")

#B Sprawdzenie ostatniego miesiąca
# Pobieram wartość ostatniego elementu listy wartości
ostatni_rachunek = wartosci[-1]

if ostatni_rachunek > srednia:
    print("b) Trzeba zacisnąć pasa!")
else:
    print("b) Wszystko okay.")
