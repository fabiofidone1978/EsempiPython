# Questo � il file esercizio-2-15.py
# 2.15: Chiedi all’utente una lista di parole e stampa solo le parole con più di 5 lettere
parole = input("Inserisci una lista di parole separate da spazi: ").split()

# Filtra solo le parole con più di 5 lettere
parole_lunghe = [parola for parola in parole if len(parola) > 5]

# Stampa le parole filtrate
print("Parole con più di 5 lettere:", parole_lunghe)