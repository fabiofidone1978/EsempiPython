# Questo � il file esercizio-3-6.py
# 3.6: Crea una sequenza Fibonacci fino a un limite dato dall'utente.
limite = int(input("Inserisci il limite della sequenza Fibonacci: "))
a, b = 0, 1
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b
print()

