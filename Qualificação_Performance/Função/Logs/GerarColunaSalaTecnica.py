def gerarColunaSalaTecnica(dados, salaTecnica):
    dados = dados.rename(columns={"TempEquip1 (C/10)": "Temp Equip (°C)"})
    dados = dados.rename(columns={"UmdEquip1 (UR/10)": "Umid Equip (%)"})
    dados["Temp Equip Min (°C)"] = salaTecnica.minTemp
    dados["Temp Equip Max (°C)"] = salaTecnica.maxTemp
    dados["Umid Equip Min (%)"] = salaTecnica.minUmid
    dados["Umid Equip Max (%)"] = salaTecnica.maxUmid

    return dados