# Questo � il file esercizio-3-13.py
# 3.13: Interrompi un ciclo quando viene trovato un numero divisibile per 7.
for i in range(1, 50):
    if i % 7 == 0:
        print(f"Numero divisibile per 7 trovato: {i}")
        break
    print(i)