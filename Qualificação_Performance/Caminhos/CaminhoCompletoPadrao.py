from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dados.DadosPadrao import dadosPadrao
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Classes.DadosPadrao import DadosPadrao
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dados.DadosEquipamento import dadosEquipamento
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Classes.DadosEquipamento import DadosEquipamento
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dados.DadosSala import dadosSala
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Classes.DadosSala import DadosSala
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dados.DadosTuboFluxo import dadosTuboFluxo
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Classes.DadosTuboFluxo import DadosTuboFluxo
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Geral.LimparLogs import limparResultados
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Geral.VerificarLogs import verificarLog
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dataframe.GerarDataframeSalas import gerarDataframeSalas
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dataframe.GerarDataframeTuboFluxo import \
    gerarDataframeTuboFluxo
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Grafico.ImportarNovasAbas import importarNovasAbas
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Grafico.ImportarDados import \
    importarDados
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Grafico.GerarGrafico import gerarGrafico
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Grafico.GraficoPreviewCCP import graficoPreviewCCP
def caminhoCompletoPadrao(listaLog):

    #Mostrando uma preview do grafico sem os limites
    while True:
        dataSalas = graficoPreviewCCP(1,listaLog)
        dataTuboFluxo = graficoPreviewCCP(5,listaLog)

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
        padrao = DadosPadrao(nome=dadosPadraoCCP[0], sigla=dadosPadraoCCP[1], cliente=dadosPadraoCCP[2],
                             OS=dadosPadraoCCP[3], dataColeta=dadosPadraoCCP[4])

        print("\nDados do Equipamento\n")
        dadosEquipamentoCCP = dadosEquipamento()
        equipamento = DadosEquipamento(nomeEquip=dadosEquipamentoCCP[0], nomeFab=dadosEquipamentoCCP[1],
                                       nomeMod=dadosEquipamentoCCP[2])

        print("\nDados da Sala de Exame\n")
        dadosSalaExameCCP = dadosSala(True)
        salaExame = DadosSala(minTemp=dadosSalaExameCCP[0], maxTemp=dadosSalaExameCCP[1], setTemp=dadosSalaExameCCP[2],
                              minUmid=dadosSalaExameCCP[3], maxUmid=dadosSalaExameCCP[4], setUmid=dadosSalaExameCCP[5])

        print("\nDados da Sala Técnica\n")
        dadosSalaTecnicaCCP = dadosSala(False)
        salaTecnica = DadosSala(minTemp=dadosSalaTecnicaCCP[0], maxTemp=dadosSalaTecnicaCCP[1],
                                setTemp=dadosSalaTecnicaCCP[2], minUmid=dadosSalaTecnicaCCP[3],
                                maxUmid=dadosSalaTecnicaCCP[4], setUmid=dadosSalaTecnicaCCP[4])

        print("\nTubo de Fluxo\n")
        dadosTuboFluxoCCP = dadosTuboFluxo()
        tuboFluxo = DadosTuboFluxo(minTemp=dadosTuboFluxoCCP[0], maxTemp=dadosTuboFluxoCCP[1],
                                   setTemp=dadosTuboFluxoCCP[2], minVazao=dadosTuboFluxoCCP[3],
                                   maxVazao=dadosTuboFluxoCCP[4], setVazao=dadosTuboFluxoCCP[5])


        print("="*20)
        print("CARREGANDO...")
        print("="*20)


        #Limpando os logs da pasta LogsAtuzalidos
        limparResultados()

        #Verificando os logs se condizem ao que foi selecionado, retorna:
        #0 - Diretorio
        #1 - Nome do log
        diretorioSalas, nomeSalasArquivo, nomeSalas = verificarLog(listaLog=listaLog, n=1)

        nomeSalaExame = nomeSalas.split("/")[0]
        nomeSalaTecnica = nomeSalas.split("/")[1]

        diretorioTuboFluxo, nomeTuboFluxoArquivo, nomeTuboFluxo = verificarLog(listaLog=listaLog, n=5)


        #Criando uma aba para as salas de Exame e Técnica
        dataFrameSalas,colunaEquip, colunaExame = gerarDataframeSalas(salaTecnica=salaTecnica, salaExames=salaExame,
                                                  diretorio=diretorioSalas,
                                                  nome=nomeSalasArquivo, datas=dataSalas)

        #Criando uma aba para o tubo de fluxo
        dataFrameTubo, colunaTuboFluxo = gerarDataframeTuboFluxo(tubofluxo=tuboFluxo, diretorio=diretorioTuboFluxo,
                                                nome=nomeTuboFluxoArquivo)


        #Importando os dataframes no excel em cada aba
        importarNovasAbas(dataFrameSalas,dataFrameTubo,nomeSalasArquivo,nomeTuboFluxoArquivo)

        #Gerando gráfico da Sala Ténica
        gerarGrafico(dataFrames=dataFrameSalas,
                     colunas=colunaEquip,
                     nomeImg=nomeSalaTecnica,
                     titulo=nomeSalaTecnica)

        #Gerando gráfico da Sala de Exames
        gerarGrafico(dataFrames=dataFrameSalas,
                     colunas=colunaExame,
                     nomeImg=nomeSalaExame,
                     titulo=nomeSalaExame)


        #Gerando gráfico do Tubo de Fluxo
        gerarGrafico(dataFrames=dataFrameTubo,
                     colunas=colunaTuboFluxo,
                     nomeImg=nomeTuboFluxo,
                     titulo=nomeTuboFluxo)

        posicoes = ["B11", "B36", "B62"]
        nomes = [nomeSalaTecnica,nomeSalaExame,nomeTuboFluxo]


        #Implementando o grafico no excel
        #Importando os dados padrão para preenchimento do excel
        importarDados(padrao, equipamento, salaTecnica, salaExame, tuboFluxo, posicoes, nomes)

        #Incluindo dados no QP
        print("FINALIZADO!!!")
    else:
        print("FINALIZADO!!!")
