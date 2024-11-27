# Questo � il file esercizio-6-15.py
# 6.15: Salva e recupera dati persistenti utilizzando il modulo `pickle`.
import pickle
dati = {"nome": "Alice", "età": 25, "città": "Roma"}
with open("dati.pkl", "wb") as file:
    pickle.dump(dati, file)

with open("dati.pkl", "rb") as file:
    dati_caricati = pickle.load(file)
print(dati_caricati)