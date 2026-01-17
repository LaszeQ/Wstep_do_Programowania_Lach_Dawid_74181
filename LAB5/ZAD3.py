import time

def sekundnik(czas_w_sekundach):
    print("Start odliczania...")
    while czas_w_sekundach > 0:
        print(f"Pozostało: {czas_w_sekundach} s")
        time.sleep(1) # "Zamrożenie" programu na 1 sekundę
        czas_w_sekundach -= 1
    print("Koniec czasu!")

# Przykładowe wywołanie:
sekundnik(20)