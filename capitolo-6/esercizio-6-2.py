# Questo � il file esercizio-6-2.py
# 6.2: Leggi il contenuto di un file di testo e stampalo.
with open("testo.txt", "r") as file:
    contenuto = file.read()
print(contenuto)