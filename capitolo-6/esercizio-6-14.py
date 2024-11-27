# Questo � il file esercizio-6-14.py
# 6.14: Gestisci un errore durante la lettura di un file inesistente.
try:
    with open("inesistente.txt", "r") as file:
        contenuto = file.read()
except FileNotFoundError:
    print("Errore: il file non esiste.")