# Questo � il file esercizio-3-14.py
# 3.14: Usa `continue` per saltare i numeri pari in un ciclo da 1 a 10.
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)