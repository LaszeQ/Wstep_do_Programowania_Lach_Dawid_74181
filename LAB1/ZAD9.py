# ZAD9
cena_dziecko = 0
cena_nastolatek= 10
cena_dorosly = 20
cena_student = cena_dorosly * 0.75

while True:
    try :
        wiek = int(input("Podaj swój wiek: "))
        if wiek < 0 or wiek > 150:
            print("Wpisz poprawny wiek")
            continue
        break
    except ValueError:
        print("Wpisz poprawny wiek")
if wiek < 4:
    print("Wchodzisz za darmo")
elif wiek >= 4 and wiek < 18:
    print("Bilet kosztuje 10 złotych")
else:
    student = input("Czy jesteś studentem? (tak/nie): ").strip().lower()
    if student == "tak":
        print("Twój bilet kosztuje" , int(20*0.75) ,"złotych")
    else:
        print("Twój bilet kosztuje 20 złotych")
