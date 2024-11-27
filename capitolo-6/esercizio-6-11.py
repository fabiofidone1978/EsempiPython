# Questo � il file esercizio-6-11.py
# 6.11: Crea un file binario e scrivi alcuni numeri.
with open("numeri.bin", "wb") as file:
    file.write(bytearray([10, 20, 30, 40, 50]))