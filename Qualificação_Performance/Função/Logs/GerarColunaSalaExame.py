def gerarColunaSalaExame(dados, salaExames):
    dados = dados.rename(columns={"TempExame1 (C/10)":"Temp Exame (°C)" })
    dados = dados.rename(columns={"UmdExame1 (UR/10)":"Umid Exame (%)" })
    dados["Temp Exame Min (°C)"] = salaExames.minTemp
    dados["Temp Exame Max (°C)"] = salaExames.maxTemp
    dados["Umid Exame Min (%)"] = salaExames.minUmid
    dados["Umid Exame Max (%)"] = salaExames.maxUmid

    return dados