import pandas as pd

dados = {
    'Nome': ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0],
    'IPVA': [2000.0, 5000.0, 1700.0, 2200.0, 1000.0],
    'Desconto': [380.0, 450.0, 277.0, 400.0, 150.0]
}

dados = pd.DataFrame(dados)

dados['Valor_total'] = dados['Valor'] + dados['IPVA']- dados['Desconto']
print(dados)