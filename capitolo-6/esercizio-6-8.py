# Questo � il file esercizio-6-8.py
# 6.8: Leggi i dati da un file CSV e stampali.
import csv


with open("dati.csv", "r") as file:
    reader = csv.reader(file)
    for riga in reader:
        print(riga)