import pandas as pd

dir = "aluguel.csv"

dados = pd.read_csv(dir, sep=';')

#Deletando os valores que for 0 em valor e condominio
#Pegando os indices
removerIndices = dados.query("Valor == 0 | Condominio == 0").index
#Removendo e já atualizando a planilha
dados.drop(removerIndices, axis=0, inplace=True)

#Observando os dados que estão na coluna Tipo
print(dados.Tipo.unique())

#Removendo uma coluna inteira
dados.drop("Tipo", axis=1, inplace=True)