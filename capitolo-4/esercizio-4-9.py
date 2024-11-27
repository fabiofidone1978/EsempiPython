# Questo � il file esercizio-4-9.py
# 4.9: Scrivi una funzione ricorsiva che calcola il fattoriale di un numero.
def fattoriale(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * fattoriale(numero - 1)
print(fattoriale(5))