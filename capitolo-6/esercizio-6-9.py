# Questo � il file esercizio-6-9.py
# 6.9: Salva un dizionario in un file JSON.
import json
dati = {"nome": "Alice", "età": 25, "città": "Roma"}
with open("dati.json", "w") as file:
    json.dump(dati, file)