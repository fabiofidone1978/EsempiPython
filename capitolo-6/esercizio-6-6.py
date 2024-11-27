# Questo � il file esercizio-6-6.py
# 6.6: Leggi un file di numeri e calcola la loro somma.
with open("numeri.txt", "r") as file:
    somma = sum(int(line.strip()) for line in file)
print(f"La somma dei numeri è {somma}")