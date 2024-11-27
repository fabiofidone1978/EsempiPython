# Questo � il file esercizio-4-8.py
# 4.8: Crea una funzione che conta le vocali in una stringa.
def conta_vocali(stringa):
    vocali = "aeiouAEIOU"
    return sum(1 for char in stringa if char in vocali)
print(conta_vocali("Python è fantastico"))

