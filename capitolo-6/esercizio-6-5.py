# Questo � il file esercizio-6-5.py
# 6.5: Scrivi un elenco di numeri in un file (uno per riga).
numeri = [1, 2, 3, 4, 5]
with open("numeri.txt", "w") as file:
    for numero in numeri:
        file.write(f"{numero}\n")