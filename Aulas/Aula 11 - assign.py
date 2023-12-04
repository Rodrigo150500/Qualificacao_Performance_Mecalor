import pandas as pd

dados = pd.read_csv("aluguel.csv", sep=';')

#Criando uma coluna com dados de outras
dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro']

#Adicionando outra forma de inserir uma nova coluna
dados = dados.assign(k = 1)

print(dados.head())