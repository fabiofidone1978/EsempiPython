# Questo � il file esercizio-3-7.py
# 3.7: Verifica se un numero dato dall'utente è primo.
numero = int(input("Inserisci un numero: "))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} non è un numero primo.")
            break
    else:
        print(f"{numero} è un numero primo.")
else:
    print(f"{numero} non è un numero primo.")