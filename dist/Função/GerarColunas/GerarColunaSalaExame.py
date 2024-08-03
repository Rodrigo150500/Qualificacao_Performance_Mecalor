def gerarColunaSalaExame(dados, salaExames):
    dados = dados.rename(columns={"TempExame1 (C/10)":"Temp Exame (°C)" })
    dados = dados.rename(columns={"UmdExame1 (UR/10)":"Umid Exame (%)" })
    dados["Temp Exame Min (°C)"] = int(salaExames.minTemp)
    dados["Temp Exame Max (°C)"] = int(salaExames.maxTemp)
    dados["Umid Exame Min (%)"] = int(salaExames.minUmid)
    dados["Umid Exame Max (%)"] = int(salaExames.maxUmid)

    return dados