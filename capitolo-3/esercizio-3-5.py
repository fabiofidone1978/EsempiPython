# Questo � il file esercizio-3-5.py
# 3.5: Trova il primo numero divisibile sia per 3 che per 5 in un intervallo scelto dall'utente.
inizio = int(input("Inserisci l'inizio dell'intervallo: "))
fine = int(input("Inserisci la fine dell'intervallo: "))
for i in range(inizio, fine + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"Il primo numero divisibile per 3 e 5 è {i}")
        break