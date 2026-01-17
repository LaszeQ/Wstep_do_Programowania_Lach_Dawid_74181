import datetime


def analiza_dat():
    dzisiaj = datetime.date.today()


    ostatnie_lab = datetime.date(2025, 12, 13)
    kolokwium = datetime.date(2026, 1, 31)

    dni_od_lab = (dzisiaj - ostatnie_lab).days
    dni_do_kolokwium = (kolokwium - dzisiaj).days

    print(f"Od ostatnich laboratoriów minęło: {dni_od_lab} dni.")

    # Wyświetlenie w przystępny sposób z nazwą miesiąca
    # Formatowanie zależy od ustawień lokalnych systemu, %B to pełna nazwa miesiąca
    data_kol = kolokwium.strftime("%d %B %Y")
    print(f"Do kolokwium ({data_kol}) zostało: {dni_do_kolokwium} dni.")


analiza_dat()