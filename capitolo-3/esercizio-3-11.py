# Questo � il file esercizio-3-11.py
# 3.11: Stampa un triangolo di asterischi con altezza scelta dall'utente.
altezza = int(input("Inserisci l'altezza del triangolo: "))
for i in range(1, altezza + 1):
    print("*" * i)