wiek = float(input("Ile masz lat? "))
# Założenie wiek powinien zawierać się od zera
# Z: Wiek (0,150>

if wiek <= 0 or wiek >= 150:
    print( "Nie masz prawa żyć")
else:


    if wiek < 18.0:
        print("Jesteś niepełnoletni")
    else:
        print("Jesteś pełnoletni")