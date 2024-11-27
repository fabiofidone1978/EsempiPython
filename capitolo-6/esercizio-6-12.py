# Questo � il file esercizio-6-12.py
# 6.12: Leggi i dati da un file binario e stampali.
with open("numeri.bin", "rb") as file:
    dati_binari = list(file.read())
print(dati_binari)