#ZAD14
# Program sprawdzający, czy plik jest arkuszem Excel

nazwa_pliku = input("Podaj nazwę pliku (z rozszerzeniem): ")

# Metoda .endswith() sprawdza, czy ciąg znaków (string) kończy się określonym fragmentem tekstu.
# Zwraca True (prawda), jeśli warunek jest spełniony, w przeciwnym razie False.
# Można przekazać jeden warunek (np. '.xlsx') lub kilka w formie krotki (np. ('.xls', '.xlsx'))

if nazwa_pliku.lower().endswith((".xls", ".xlsx", ".xlsm", ".xlsb")):
    print("To jest plik arkusza Excel.")
else:
    print("To nie jest plik Excel.")
