# Questo � il file esercizio-6-7.py
# 6.7: Crea un file CSV con tre righe e tre colonne.
import csv
with open("dati.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Età", "Città"])
    writer.writerow(["Alice", 25, "Roma"])
    writer.writerow(["Daniela", 30, "Milano"])
    writer.writerow(["Luca", 35, "Napoli"])