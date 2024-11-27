# Questo � il file esercizio-3-9.py
# 3.9: Stampa una tabella di moltiplicazione per un numero scelto dall’utente.
numero = int(input("Inserisci un numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")