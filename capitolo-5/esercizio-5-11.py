# Questo � il file esercizio-5-11.py
# 5.11: Accedi al terzo elemento di una tupla.
# Creazione della tupla con i giorni della settimana
giorni_settimana = ("Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica")

# Controllo che la tupla abbia almeno 3 elementi
if len(giorni_settimana) >= 3:
    print(f"Il terzo giorno della settimana è: {giorni_settimana[2]}")
else:
    print("La tupla non contiene almeno tre elementi.")

