# Questo � il file esercizio-7-7.py
# 7.7: Crea un DataFrame con `pandas` e calcola la media di una colonna.
df = pd.DataFrame({"Nome": ["Alice", "Bob", "Charlie"], "Età": [25, 30, 35]})
media_eta = df["Età"].mean()
print(f"La media delle età è {media_eta}")

