# Questo � il file esercizio-5-15.py
# 5.15: Crea un dizionario invertendo le chiavi e i valori di un altro dizionario.
# Creazione del dizionario
citta = {}
citta[ input("Scrivi il nome della prima città: ") ] = input("Scrivi il nome della seconda città: ")

# Inversione delle chiavi e dei valori
citta_invertito = {v: k for k, v in citta.items()}

# Stampa del risultato
print("Dizionario originale:", citta)
print("Dizionario invertito:", citta_invertito)
