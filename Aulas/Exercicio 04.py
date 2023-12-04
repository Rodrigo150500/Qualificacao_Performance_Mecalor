import pandas as pd

dir = "aluguel.csv"

dados = pd.read_csv(dir, sep=';')

media = dados["Quartos"].mean()
print(media)

bairros = dados['Bairro'].value_counts()
print(bairros)

aluguel = dados.groupby('Bairro')['Valor'].mean().sort_values()
print(aluguel.tail())


print(dados['Quartos'].mean())
print(len(dados['Bairro'].unique()))
print(dados['Bairro'].nunique())

print(dados.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False))

