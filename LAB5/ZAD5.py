import keyword

slowa = ["for", "print", "break", "done", "bad"]

print("Weryfikacja słów kluczowych:")
for slowo in slowa:
    czy_kluczowe = keyword.iskeyword(slowo)
    print(f"'{slowo}': {czy_kluczowe}")