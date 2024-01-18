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
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.GerarLogs.GerarLogSalas import gerarLogSalas
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.GerarLogs.GerarLogTuboFluxo import \
    gerarLogTuboFluxo
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dataframe.GerarDataframeSalas import gerarDataframeSalas
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dataframe.GerarDataframeTuboFluxo import \
    gerarDataframeTuboFluxo
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Grafico.ImportarDadosQP import importarDadosQP
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Grafico.ImportarDadosPadrao import \
    importarDadosPadrao
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Grafico.GerarGrafico import gerarGrafico

def caminhoCompletoPadrao(listaLog):
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
    diretorioSalas, nomeSalas = verificarLog(listaLog=listaLog, n=1)
    nomeSalaExame = nomeSalas[0]
    nomeSalaTecnica = nomeSalas[1]
    diretorioTuboFluxo, nomeTuboFluxo = verificarLog(listaLog=listaLog, n=5)


    #Criando uma aba para as salas de Exame e Técnica
    dataFrameSalas,colunaEquip, colunaExame = gerarDataframeSalas(salaTecnica=salaTecnica, salaExames=salaExame,
                                              diretorio=diretorioSalas,
                                                nome=nomeSalas)


    #Criando uma aba para o tubo de fluxo
    dataFrameTubo, colunaTuboFluxo = gerarDataframeTuboFluxo(tubofluxo=tuboFluxo, diretorio=diretorioTuboFluxo,
                                            nome=nomeTuboFluxo)



    #Importando os dataframes no excel
    importarDadosQP(dataFrameSalas,dataFrameTubo,nomeSalas,nomeTuboFluxo)

    #Importando os dados padrão para preenchimento do excel
    importarDadosPadrao(padrao, equipamento, salaTecnica, salaExame, tuboFluxo)

    #Gerando gráfico da Sala Ténica
    gerarGrafico(dataFrames=dataFrameSalas,
                 colunas=colunaEquip,
                 nomeImg=nomeSalaTecnica,
                 titulo="Sala Técnica",
                 posicao="B11")

    #Gerando gráfico da Sala de Exames
    gerarGrafico(dataFrames=dataFrameSalas,
                 colunas=colunaExame,
                 nomeImg=nomeSalaExame,
                 titulo="Sala Exames",
                 posicao="B36")

    #Gerando gráfico do Tubo de Fluxo
    gerarGrafico(dataFrames=dataFrameTubo,
                 colunas=colunaTuboFluxo,
                 nomeImg=nomeTuboFluxo,
                 titulo="Tubo de Fluxo",
                 posicao="B62")




    #Incluindo dados no QP
    print("FINALIZADO!!!")



    #Verificando os logs das salas importados
    #gerarLogSalas(salaExames=salaExame, salaTecnica=salaTecnica, diretorio=diretorioSalas[0], nome=diretorioSalas[1])

    #Verificando os logs do tubo de fluxo
    #gerarLogTuboFluxo(tuboFluxo=tuboFluxo, diretorio = diretorioTuboFluxo[0], nome=diretorioTuboFluxo[1])

    #Importando os logs para a planilha QP
    #gerarNovaAbaLog([["SalaExameTecnica", diretorioSalas[1]],["TuboFluxo",diretorioTuboFluxo[1]]])


