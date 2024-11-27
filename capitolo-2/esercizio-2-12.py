# Questo � il file esercizio-2-12.py
# 2.12: Chiedi all’utente una parola e verifica se è un palindromo.
parola = input("Inserisci una parola: ")
if parola == parola[::-1]:
    print(f"La parola '{parola}' è un palindromo.")
else:
    print(f"La parola '{parola}' non è un palindromo.")

