#ZAD6

cena_paliwa = (6.5)#zł/litr
droga = float(input(f"Podaj drogę pokonaną przez samochód w kilometrach\n"))
spalanie = float(input(f"Podaj średnie spalanie swojego samochodu (w litrach na 100km)\n"))

zużycie_paliwa = droga / 100 * spalanie
koszt_podróży = zużycie_paliwa * cena_paliwa

print(f"Zużycie paliwa wyniesie: {zużycie_paliwa} litrów \n"f"Koszt podróży wyniesie: {koszt_podróży} zł")

