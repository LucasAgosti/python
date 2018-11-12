import pandas as pd
import matplotlib as plt
import numpy as np

df = pd.DataFrame({"Aluno" : ["Lucas", "Paulo", "Nivardo"],
                   "Faltas" : [0, 5, 18],
                   "Nota": [10, 8, 9],
                   "Trabalho" : [9.5, 8.2, 9.8]})

print("DataFrame:\n", df)
print("----------------------")
print("Nomes das colunas:\n", df.columns)
print("---------------------------------------")
print("Notas de trabalho:\n", df["Trabalho"])
