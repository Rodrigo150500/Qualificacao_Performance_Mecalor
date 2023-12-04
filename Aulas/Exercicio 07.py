import pandas as pd

dados = pd.read_csv('./alunos.txt')

dados = dados.fillna(0)
dados = dados.assign(Pontos_extras = dados['Notas']*0.4)
dados = dados.assign(Notas_finais = dados['Pontos_extras'] + dados['Notas'])
dados['Aprovado_final'] = dados['Notas_finais'].apply(lambda x: "Aprovado" if x >=6 else "Reprovado")
