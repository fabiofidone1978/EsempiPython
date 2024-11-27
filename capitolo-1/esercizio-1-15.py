# Questo � il file esercizio-1-15.py
# 1.15: Crea un programma che converte secondi in ore, minuti e secondi.
secondi = int(input("Inserisci il numero di secondi: "))
ore = secondi // 3600
minuti = (secondi % 3600) // 60
sec = secondi % 60
print(f"{secondi} secondi corrispondono a {ore} ore, {minuti} minuti e {sec} secondi.")
# Questo � il file esercizio-1-3.py