# Questo � il file esercizio-3-15.py
# 3.15: Scrivi un programma che chiede all’utente di indovinare un numero casuale.
import random
numero_casuale = random.randint(1, 100)
tentativo = 0
while True:
    guess = int(input("Indovina il numero (1-100): "))
    tentativo += 1
    if guess < numero_casuale:
        print("Troppo basso!")
    elif guess > numero_casuale:
        print("Troppo alto!")
    else:
        print(f"Complimenti! Hai indovinato in {tentativo} tentativi.")
        break