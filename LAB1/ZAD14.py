# Program sprawdzający, czy plik jest arkuszem Excel

# Funkcja input() pobiera nazwę pliku od użytkownika
nazwa_pliku = input("Podaj nazwę pliku (z rozszerzeniem): ")

# Metoda .endswith() sprawdza, czy ciąg znaków (string) kończy się określonym fragmentem tekstu.
# Zwraca True (prawda), jeśli warunek jest spełniony, w przeciwnym razie False.
# Można przekazać jeden warunek (np. '.xlsx') lub kilka w formie krotki (np. ('.xls', '.xlsx'))

if nazwa_pliku.lower().endswith((".xls", ".xlsx", ".xlsm", ".xlsb")):
    print("To jest plik arkusza Excel.")
else:
    print("To nie jest plik Excel.")

# Najczęściej spotykane rozszerzenia plików Excel:
# - .xls  → starszy format (Excel 97-2003)
# - .xlsx → nowszy format (od Excela 2007, bez makr)
# - .xlsm → nowszy format z obsługą makr
# - .xlsb → format binarny (szybszy w odczycie dużych arkuszy)