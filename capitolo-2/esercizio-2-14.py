# Questo � il file esercizio-2-14.py
# 2.14: Scrivi un programma che ordina una lista di numeri in ordine crescente.
numeri = list(map(int, input("Inserisci una lista di numeri separati da spazi: ").split()))
numeri_ordinati = sorted(numeri)
print("Numeri ordinati:", numeri_ordinati)