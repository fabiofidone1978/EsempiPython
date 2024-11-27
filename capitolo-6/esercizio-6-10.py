# Questo � il file esercizio-6-10.py
# 6.10: Leggi un dizionario da un file JSON.
import json
with open("dati.json", "r") as file:
    dati_letti = json.load(file)
print(dati_letti)