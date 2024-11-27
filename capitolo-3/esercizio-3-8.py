# Questo � il file esercizio-3-8.py
# 3.8: Scrivi un programma che calcola il fattoriale di un numero.
numero = int(input("Inserisci un numero: "))
fattoriale = 1
for i in range(1, numero + 1):
    fattoriale *= i
print(f"Il fattoriale di {numero} è {fattoriale}.")

