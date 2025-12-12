#ZAD3
ciag = input("Podaj słowo do sprawdzenia palindromu: ")
# Palindrom czyta się tak samo wspak
# Używam [::-1] żeby odwrócić napis
ciag_odwrocony = ciag[::-1]

if ciag == ciag_odwrocony:
    print("Tak, to jest palindrom!")
else:
    print("Nie, to nie jest palindrom.")