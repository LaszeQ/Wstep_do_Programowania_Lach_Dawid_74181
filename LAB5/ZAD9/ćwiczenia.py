# Sposób 1: Import całego modułu
import f_mat

print("--- Sposób 1 ---")
print(f"Kwadrat 10: {f_mat.kwadrat(10)}")
print(f"Sześcian 3: {f_mat.szescian(3)}")
print(f"Suma 10 + 5: {f_mat.dodaj(10, 5)}")

# Sposób 2: Import wybranych funkcji
from f_mat import kwadrat, szescian, dodaj

print("\n--- Sposób 2 ---")
print(f"Kwadrat 10: {kwadrat(10)}")
print(f"Sześcian 3: {szescian(3)}")
print(f"Suma 10 + 5: {dodaj(10, 5)}")