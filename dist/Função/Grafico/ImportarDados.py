import os
import openpyxl
from openpyxl.drawing.image import Image

import sys
def get_executable_path():
    """Obter o caminho do executável atual."""
    if getattr(sys, 'frozen', False):
        # Estamos em um executável empacotado com PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Estamos executando um script Python normal
        return os.path.dirname(__file__)
def importarDados(dadosPadrao, dadosEquipamento, salaTecnica, salaExame, tuboFluxo, posicao, nome):
    caminho = os.path.normpath(os.path.join(get_executable_path(),"../../Resultado/Qualificacao.xlsx"))


    workbook = openpyxl.load_workbook(caminho)

    abaGrafico = workbook["Grafico"]

    #Dados Padrão
    abaGrafico["C2"] = dadosPadrao.cliente
    abaGrafico["F2"] = dadosPadrao.OS
    abaGrafico["I2"] = dadosPadrao.dataColeta
    abaGrafico["C88"] = dadosPadrao.nome
    abaGrafico["J88"] = dadosPadrao.sigla



    #Dados Equipamentos
    abaGrafico["D6"] = dadosEquipamento.nomeFab
    abaGrafico["G6"] = dadosEquipamento.nomeMod
    abaGrafico["D32"] = dadosEquipamento.nomeFab
    abaGrafico["G32"] = dadosEquipamento.nomeMod
    abaGrafico["D58"] = dadosEquipamento.nomeFab
    abaGrafico["G58"] = dadosEquipamento.nomeMod


    #Dados Sala Técnica
    abaGrafico["D8"] = salaTecnica.minTemp
    abaGrafico["F8"] = salaTecnica.minUmid
    abaGrafico["I8"] = salaTecnica.setTemp
    abaGrafico["D9"] = salaTecnica.maxTemp
    abaGrafico["F9"] = salaTecnica.maxUmid
    abaGrafico["I9"] = salaTecnica.setUmid

    #Dados Sala Exames
    abaGrafico["D33"] = salaExame.minTemp
    abaGrafico["F33"] = salaExame.minUmid
    abaGrafico["I33"] = salaExame.setTemp
    abaGrafico["D34"] = salaExame.maxTemp
    abaGrafico["F34"] = salaExame.maxUmid
    abaGrafico["I34"] = salaExame.setUmid

    #Dados Tubo de Fluxo
    abaGrafico["D59"] = tuboFluxo.minTemp
    abaGrafico["F59"] = tuboFluxo.minVazao
    abaGrafico["I59"] = tuboFluxo.setTemp
    abaGrafico["D60"] = tuboFluxo.maxTemp
    abaGrafico["F60"] = tuboFluxo.maxVazao
    abaGrafico["I60"] = tuboFluxo.setVazao



    for i in range (0,len(posicao),1):
        caminhoImagem = os.path.normpath(os.path.join(get_executable_path(), "../../Resultado/FotosGrafico",
                                                      nome[i]+".png"))

        img = Image(caminhoImagem)
        abaGrafico.add_image(img, posicao[i])

    workbook.save(caminho)




