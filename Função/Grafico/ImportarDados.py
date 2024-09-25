import os
import openpyxl
from openpyxl.drawing.image import Image
from Função.Geral.AcharCaminhoExecutadoPyinstaller import acharCaminhoExecutado



def importarDados(dadosPadrao, dadosEquipamento, salaTecnica, salaExame, tuboFluxo, posicao, nome):

    caminhoExcel = os.path.join(acharCaminhoExecutado("Resultado/Qualificacao.xlsx"))

    workbook = openpyxl.load_workbook(caminhoExcel)

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
    abaGrafico["I59"] = tuboFluxo.setVazao
    abaGrafico["D60"] = tuboFluxo.maxTemp
    abaGrafico["F60"] = tuboFluxo.maxVazao
    abaGrafico["I60"] = tuboFluxo.setTemp


    for i in range (0,len(posicao),1):



        caminhoImagem = os.path.join(acharCaminhoExecutado("Resultado/FotosGrafico"), nome[i]+".png")
        img = Image(caminhoImagem)
        abaGrafico.add_image(img, posicao[i])

    workbook.save(acharCaminhoExecutado("Resultado/Qualificacao.xlsx"))




