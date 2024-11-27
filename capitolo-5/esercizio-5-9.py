# Questo � il file esercizio-5-9.py
# 5.9: Rimuovi una città dal dizionario.

# Creazione del dizionario con alcune città
citta = {"Roma": 2873000, "Milano": 1372000, "Napoli": 962000}

# Chiedi all'utente quale città rimuovere
citta_da_rimuovere = input("Inserisci il nome della città da rimuovere: ")

# Controlla se la città è presente nel dizionario
if citta_da_rimuovere in citta:
    del citta[citta_da_rimuovere]
    print(f"La città '{citta_da_rimuovere}' è stata rimossa.")
else:
    print(f"La città '{citta_da_rimuovere}' non è presente nel dizionario.")

# Stampa il dizionario aggiornato
print("Dizionario aggiornato:", citta)
