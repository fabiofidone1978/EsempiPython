# Questo � il file esercizio-6-4.py
# 6.4: Leggi un file riga per riga e stampa ciascuna riga.
with open("testo.txt", "r") as file:
    for riga in file:
        print(riga.strip())