# Questo � il file esercizio-4-15.py
# 4.15: Scrivi una funzione che converte una lista di gradi Celsius in Fahrenheit.
def lista_celsius_to_fahrenheit(lista):
    return [(c * 9/5) + 32 for c in lista]
print(lista_celsius_to_fahrenheit([0, 20, 100]))