def gerarColunaSalaTecnica(dados, salaTecnica):
    dados = dados.rename(columns={"TempEquip1 (C/10)": "Temp Equip (°C)"})
    dados = dados.rename(columns={"UmdEquip1 (UR/10)": "Umid Equip (%)"})
    dados["Temp Equip Min (°C)"] = str(int(salaTecnica.minTemp))
    dados["Temp Equip Max (°C)"] = str(int(salaTecnica.maxTemp))
    dados["Umid Equip Min (%)"] = str(int(salaTecnica.minUmid))
    dados["Umid Equip Max (%)"] = str(int(salaTecnica.maxUmid))

    return dados