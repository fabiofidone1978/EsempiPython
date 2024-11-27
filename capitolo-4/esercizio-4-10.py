# Questo � il file esercizio-4-10.py
# 4.10: Crea una funzione che verifica se una parola è un palindromo.
def is_palindromo(parola):
    return parola == parola[::-1]
print(is_palindromo("radar"))