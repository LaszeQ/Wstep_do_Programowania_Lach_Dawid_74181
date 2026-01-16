def hanoi(n, start, cel, pomoc):
    if n == 1:
        print(f"Przenieś krążek 1 z {start} na {cel}")
        return
    hanoi(n - 1, start, pomoc, cel)
    print(f"Przenieś krążek {n} z {start} na {cel}")
    hanoi(n - 1, pomoc, cel, start)

hanoi(3, 'A', 'C', 'B')