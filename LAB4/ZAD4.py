def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    print(f"Twoje BMI wynosi: {bmi:.2f}")

    if bmi < 18.5:
        print("Zakres: niedowaga")
    elif 18.5 <= bmi < 25:
        print("Zakres: wartość prawidłowa")
    elif 25 <= bmi < 30:
        print("Zakres: nadwaga")
    else:
        print("Zakres: otyłość")


oblicz_bmi(70, 1.75)