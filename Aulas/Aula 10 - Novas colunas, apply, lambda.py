import pandas as pd

dir = 'aluguel.csv'

dados = pd.read_csv(dir,sep=';')

#Criando coluna binaria
dados['Possui_suite'] = dados['Suites'].apply(lambda x: 'Sim' if x >0 else "Não")
print(dados)
