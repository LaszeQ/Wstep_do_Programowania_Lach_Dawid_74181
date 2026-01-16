def srednia_listy(liczby):
    if not liczby:
        return 0
    return sum(liczby) / len(liczby)

moje_liczby = [10, 20, 30, 40, 50]
print(f"Średnia: {srednia_listy(moje_liczby)}")