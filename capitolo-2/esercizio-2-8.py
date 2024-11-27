# Questo � il file esercizio-2-8.py
# 2.8: Scrivi un programma che verifica se una stringa contiene una parola specifica.
frase = input("Inserisci una frase: ")
parola = input("Inserisci una parola da cercare: ")
if parola in frase:
    print(f"La parola '{parola}' è nella frase.")
else:
    print(f"La parola '{parola}' non è nella frase.")

