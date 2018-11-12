import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#series é um array unidimensional/lista de valores
#o index é a coluna a esquerda

notas = pd.Series([2, 3, 5, 7, 11])
#foi criado um index padrão de 0 a 5 pois não atribuímos nenhum valor ou nome a ele
print("Sua series:\n", notas)
print("Valores:\n", notas.values)
print("--------------------")

notas = pd.Series([2, 3, 5, 7, 11], index = ["CE", "RJ", "RN", "MA", "SP"])
print("Sua nova series:\n", notas)
print("--------------------")

#para achar um específico:
print("Valor do Ceará:\t", notas["CE"])
print("--------------------")

print("DETALHES:\n", notas.describe())
#OBS: std = desvio padrão, mean = media
