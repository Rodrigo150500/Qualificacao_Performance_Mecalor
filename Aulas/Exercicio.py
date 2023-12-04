#Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.
import pandas as pd

dir = "alunos.txt"

dados = pd.read_csv(dir)

#2) Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.
print(dados.head(7))
print(dados.tail())

#3) Confira a quantidade de linhas e colunas desse DataFrame.
print(dados.shape)

#4) Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.
print(dados.info())

print(dados.describe())