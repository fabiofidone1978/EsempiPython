# Questo � il file esercizio-7-10.py
# 7.10: Leggi dati da un file Excel utilizzando `pandas`.
import pandas as pd
df_excel = pd.DataFrame({"Nome": ["Anna", "Luca"], "Età": [22, 28]})
df_excel.to_excel("dati.xlsx", index=False)
df_letti = pd.read_excel("dati.xlsx")
print(df_letti)

