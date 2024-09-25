import json
from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado

def JsonCaminho():

    execucaoPyinstaller = acharCaminhoExecutado()

    caminhoJson = "Json/caminhos.json" if execucaoPyinstaller == True else "../../JsonPath/caminhos.json"
    with open(caminhoJson, 'r') as json_file:
        return json.load(json_file)

