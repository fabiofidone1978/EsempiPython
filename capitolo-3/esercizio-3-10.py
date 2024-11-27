# Questo � il file esercizio-3-10.py
# 3.10: Trova tutti i numeri palindromi in un intervallo scelto dall'utente.
inizio = int(input("Inserisci l'inizio dell'intervallo: "))
fine = int(input("Inserisci la fine dell'intervallo: "))
for i in range(inizio, fine + 1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")
print()

