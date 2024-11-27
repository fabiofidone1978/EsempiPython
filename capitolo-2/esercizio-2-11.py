# Questo � il file esercizio-2-11.py
# 2.11: Scrivi un programma che trova il numero più piccolo in una lista data dall’utente.
numeri = list(map(int, input("Inserisci una lista di numeri separati da spazi: ").split()))
print(f"Il numero più piccolo è {min(numeri)}.")

