from Função.Dados.DadosPadrao import dadosPadrao
from Classes.DadosPadrao import DadosPadrao
from Função.Dados.DadosEquipamento import dadosEquipamento
from Classes.DadosEquipamento import DadosEquipamento
from Função.Dados.DadosSala import dadosSala
from Classes.DadosSala import DadosSala
from Função.Dados.DadosTuboFluxo import dadosTuboFluxo
from Classes.DadosTuboFluxo import DadosTuboFluxo
from Função.Geral.LimparLogs import limparResultados
from Função.Geral.SepararDados import separarDados
from Função.Dataframe.GerarDataframeSalas import gerarDataframeSalas
from Função.Dataframe.GerarDataframeTuboFluxo import \
    gerarDataframeTuboFluxo
from Função.Grafico.ImportarNovasAbas import importarNovasAbas
from Função.Grafico.ImportarDados import \
    importarDados
from Função.Grafico.GerarGrafico import gerarGrafico
from Função.Grafico.GraficoPreview import graficoPreview


def caminhoCompletoPadrao(listaLog):

    opcao = {'Sala Exames/Sala Técnica': 1,
             'Sala Exames':2,
             'Sala Técnica':3,
             'Sala Adicional':4,
             'Tubo de Fluxo':5
             }

    #Mostrando uma preview do grafico sem os limites
    while True:
        dataSalas = graficoPreview(listaLog, opcao["Sala Exames/Sala Técnica"])
        dataTuboFluxo = graficoPreview(listaLog, opcao["Tubo de Fluxo"])

        resposta = int(input("Deseja ver novamente: \n"
                             "[1] - Sim\n"
                             "[2] - Não\n"))
        if resposta == 2:
            break

    continuar = int(input("Deseja continuar: \n"
                          "[1] - Sim\n"
                          "[2] - Não\n"))
    while (continuar <= 0 or continuar >= 3):
       print("Valores Incorretos")
       continuar = int(input("Deseja continuar: \n"
                             "[1] - Sim\n"
                             "[2] - Não\n"))
       if continuar == 1 or continuar == 2:
            break
    if continuar == 1:
        #Importando os inputs do usuario
        print("Dados Padrão\n")
        dadosPadraoCCP = dadosPadrao()
        padrao = DadosPadrao(nome=dadosPadraoCCP["Nome"], sigla=dadosPadraoCCP["Sigla"],
                             cliente=dadosPadraoCCP["Cliente"],OS=dadosPadraoCCP["OS"],
                             dataColeta=dadosPadraoCCP["DataColeta"])

        print("\nDados do Equipamento\n")
        dadosEquipamentoCCP = dadosEquipamento()
        equipamento = DadosEquipamento(equipamento=dadosEquipamentoCCP["Equipamento"],
                                       fabricante=dadosEquipamentoCCP["Fabricante"],
                                       modelo=dadosEquipamentoCCP["Modelo"])

        print("\nDados da Sala de Exame\n")
        dadosSalaExameCCP = dadosSala("Exames")
        salaExame = DadosSala(minTemp=dadosSalaExameCCP["MinTemp"], maxTemp=dadosSalaExameCCP["MaxTemp"],
                              setTemp=dadosSalaExameCCP["SetpointTemp"], minUmid=dadosSalaExameCCP["MinUmid"],
                              maxUmid=dadosSalaExameCCP["MaxUmid"], setUmid=dadosSalaExameCCP["SetpointUmid"])

        print("\nDados da Sala Técnica\n")
        dadosSalaTecnicaCCP = dadosSala("Técnica")
        salaTecnica = DadosSala(minTemp=dadosSalaTecnicaCCP["MinTemp"], maxTemp=dadosSalaTecnicaCCP["MaxTemp"],
                                setTemp=dadosSalaTecnicaCCP["SetpointTemp"], minUmid=dadosSalaTecnicaCCP["MinUmid"],
                                maxUmid=dadosSalaTecnicaCCP["MaxUmid"], setUmid=dadosSalaTecnicaCCP["SetpointUmid"])

        print("\nTubo de Fluxo\n")
        dadosTuboFluxoCCP = dadosTuboFluxo()
        tuboFluxo = DadosTuboFluxo(minTemp=dadosTuboFluxoCCP["MinTemp"], maxTemp=dadosTuboFluxoCCP["MaxTemp"],
                                   setTemp=dadosTuboFluxoCCP["SetpointTemp"], minVazao=dadosTuboFluxoCCP["MinVazao"],
                                   maxVazao=dadosTuboFluxoCCP["MaxVazao"], setVazao=dadosTuboFluxoCCP["SetpointVazao"])


        print("="*20)
        print("CARREGANDO...")
        print("="*20)


        #Limpando os logs da pasta LogsAtuzalidos
        limparResultados()
        print("Resultados Limpos\n")

        #Verificando os logs se condizem ao que foi selecionado, retorna
        diretorioSalas, nomeSalasArquivo, nomeSalas = separarDados(listaLog=listaLog, opcao=opcao['Sala Exames/Sala Técnica'])

        nomeSalaExame = nomeSalas.split("/")[0]
        nomeSalaTecnica = nomeSalas.split("/")[1]

        diretorioTuboFluxo, nomeTuboFluxoArquivo, nomeTuboFluxo = separarDados(listaLog=listaLog, opcao=opcao['Tubo de Fluxo'])

        print("Logs Verificados\n")

        #Criando uma aba para as salas de Exame e Técnica
        dataFrameSalas, colunaEquip, colunaExame = gerarDataframeSalas(salaTecnica=salaTecnica, salaExames=salaExame,
                                                  diretorio=diretorioSalas,
                                                  nome=nomeSalasArquivo, datas=dataSalas)

        #Criando uma aba para o tubo de fluxo
        dataFrameTubo, colunaTuboFluxo = gerarDataframeTuboFluxo(tubofluxo=tuboFluxo, diretorio=diretorioTuboFluxo,
                                                nome=nomeTuboFluxoArquivo, datas = dataTuboFluxo)

        print("Abas para as salas e tubo criadas\n")

        #Importando os dataframes no excel em cada aba
        importarNovasAbas(dataFrameSalas,dataFrameTubo,nomeSalasArquivo,nomeTuboFluxoArquivo)

        #Gerando gráfico da Sala Ténica
        gerarGrafico(dataFrames=dataFrameSalas,
                     colunas=colunaEquip,
                     nomeImg=nomeSalaTecnica,
                     titulo=nomeSalaTecnica,
                     )

        #Gerando gráfico da Sala de Exames
        gerarGrafico(dataFrames=dataFrameSalas,
                     colunas=colunaExame,
                     nomeImg=nomeSalaExame,
                     titulo=nomeSalaExame,
                     )


        #Gerando gráfico do Tubo de Fluxo
        gerarGrafico(dataFrames=dataFrameTubo,
                     colunas=colunaTuboFluxo,
                     nomeImg=nomeTuboFluxo,
                     titulo=nomeTuboFluxo,
                     )

        posicoes = ["B11", "B36", "B62"]
        nomes = [nomeSalaTecnica, nomeSalaExame, nomeTuboFluxo]


        #Implementando o grafico no excel
        #Importando os dados padrão para preenchimento do excel
        importarDados(padrao, equipamento, salaTecnica, salaExame, tuboFluxo, posicoes, nomes)

        #Incluindo dados no QP
        print("FINALIZADO!!!")
    else:
        print("FINALIZADO!!!")
