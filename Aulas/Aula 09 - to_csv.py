import pandas as pd

dir = 'aluguel.csv'

dados = pd.read_csv(dir)

#Salvando o arquivo sem o index e separando por ;
dados.to_csv("Aluguel2.csv", index=False, sep=';')

