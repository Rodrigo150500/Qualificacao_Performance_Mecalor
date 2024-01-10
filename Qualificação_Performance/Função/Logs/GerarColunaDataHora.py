
def gerarColunaDataHora(dados):

    dataHoras = dados.Data.unique()
    listaData = []
    listaHora = []
    for dataHora in dataHoras:
        dia = str(dataHora)[4:6]
        mes = str(dataHora)[2:4]
        ano = str(dataHora)[0:2]

        hora = str(dataHora)[6:8]
        min = str(dataHora)[8:10]
        seg = str(dataHora)[10:12]

        data = f"{dia}/{mes}/{ano}"
        horario = f"{hora}:{min}:{seg}"

        listaData.append(data)
        listaHora.append(horario)

    # Criando as colunas de Data e Hora
    dados["Data2"] = listaData
    dados["Hora"] = listaHora

    return dados