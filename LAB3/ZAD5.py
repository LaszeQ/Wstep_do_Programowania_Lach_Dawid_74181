#ZAD5
# Lista zakupów:
zakupy = {
    "Chleb": 4.50,
    "Mleko": 3.20,
    "Masło": 7.50,
    "Ser": 12.00
}

# Wyświetlanie i sumowanie
suma = 0
print("Twoja lista zakupów:")
for produkt in zakupy:
    cena = zakupy[produkt]
    print(f"- {produkt}: {cena} zł")
    suma += cena

print("Razem do zapłaty:", suma, "zł")