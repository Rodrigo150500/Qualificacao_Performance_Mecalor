
def gerarColunaTuboFluxo(dados,tuboFluxo):

    dados = dados.rename(columns={"TempAlimAG (C/10)":"Temp AlimAG (°C)"} )
    dados = dados.rename(colums={"VzAlimAG (l/min/10)":"Vz AlimAG (l/min)"})
    dados["Temp AlimAG Min (°C)"] = tuboFluxo.minTemp
    dados["Temp AlimAG Max (°C)"] = tuboFluxo.maxTemp
    dados["Vz AlimAG Min (l/min)"] = tuboFluxo.minVazao
    dados["Vz AlimAG Max (l/min)"] = tuboFluxo.maxVazao

    return dados

