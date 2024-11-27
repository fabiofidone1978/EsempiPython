# Questo � il file esercizio-6-3.py
# 6.3: Aggiungi una nuova frase a un file esistente.
with open("testo.txt", "a") as file:
    file.write("\nQuesta è una nuova riga aggiunta.")