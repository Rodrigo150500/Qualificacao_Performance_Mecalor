
def gerarColunaTuboFluxo(dados,tuboFluxo):

    dados = dados.rename(columns={"TempAlimAG (C/10)":"Temp AlimAG (°C)"} )
    dados = dados.rename(columns={"VzAlimAG (l/min/10)":"Vz AlimAG (l/min)"})
    dados["Temp AlimAG Min (°C)"] = int(tuboFluxo.minTemp)
    dados["Temp AlimAG Max (°C)"] = int(tuboFluxo.maxTemp)
    dados["Vz AlimAG Min (l/min)"] = int(tuboFluxo.minVazao)
    dados["Vz AlimAG Max (l/min)"] = int(tuboFluxo.maxVazao)

    return dados

