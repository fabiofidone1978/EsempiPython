# Questo � il file esercizio-6-13.py
# 6.13: Scrivi un programma che legge un file e conta le righe.
with open("testo.txt", "r") as file:
    righe = sum(1 for _ in file)
print(f"Il file contiene {righe} righe.")