# Questo � il file esercizio-2-10.py
# 2.10: Genera una lista di numeri pari fino a un numero dato dall’utente.
limite = int(input("Inserisci un numero limite: "))
numeri_pari = [x for x in range(0, limite + 1) if x % 2 == 0]
print("Numeri pari:", numeri_pari)

