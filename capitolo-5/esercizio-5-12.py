# Questo � il file esercizio-5-12.py
# 5.12: Verifica se un elemento è presente in una lista.
# Crea una lista
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Chiedi all'utente un numero da cercare
numero_da_cercare = int(input("Inserisci il numero da cercare nella lista: "))

# Verifica se il numero è presente
esiste = numero_da_cercare in numeri

# Stampa il risultato
if esiste:
    print(f"Il numero {numero_da_cercare} è presente nella lista.")
else:
    print(f"Il numero {numero_da_cercare} non è presente nella lista.")