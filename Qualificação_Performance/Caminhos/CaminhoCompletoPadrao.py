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

    print(''
          '- Limpar os logs\n'
          '- Limpar as os gráficos\n' 
          '- Verificando os logs\n'
          '- Criando a folha das salas\n'
          '- Criando a folha do tubo de fluxo\n'
          '- Importando os dados\n'
          '- Gerando gráfico da Sala Técnica\n'
          '- Gerando gráfico da Sala de Exames\n'
          '- Gerando gráfico do Tubo de Fluxo\n')
    #Limpando os logs da pasta LogsAtuzalidos
    limparResultados()
    print("="*10 +" 12% " +"="*10)

    print(''
          'OK Limpar os logs\n'
          'OK Limpar as os gráficos\n'
          '- Verificando os logs\n'
          '- Criando a folha das salas\n'
          '- Criando a folha do tubo de fluxo\n'
          '- Importando os dados\n'
          '- Gerando gráfico da Sala Técnica\n'
          '- Gerando gráfico da Sala de Exames\n'
          '- Gerando gráfico do Tubo de Fluxo\n')

    #Verificando os logs se condizem ao que foi selecionado, retorna:
    #0 - Diretorio
    #1 - Nome do log
    diretorioSalas, nomeSalasArquivo, nomeSalas = verificarLog(listaLog=listaLog, n=1)
    nomeSalaExame = nomeSalas.split("/")[0]
    nomeSalaTecnica = nomeSalas.split("/")[1]
    diretorioTuboFluxo, nomeTuboFluxoArquivo,nomeTuboFluxo = verificarLog(listaLog=listaLog, n=5)
    print("="*10 +" 25% " +"="*10)

    print(''
          'OK Limpar os logs\n'
          'OK Limpar as os gráficos\n'
          'OK Verificando os logs\n'
          '- Criando a folha das salas\n'
          '- Criando a folha do tubo de fluxo\n'
          '- Importando os dados\n'
          '- Gerando gráfico da Sala Técnica\n'
          '- Gerando gráfico da Sala de Exames\n'
          '- Gerando gráfico do Tubo de Fluxo\n')

    #Criando uma aba para as salas de Exame e Técnica
    dataFrameSalas,colunaEquip, colunaExame = gerarDataframeSalas(salaTecnica=salaTecnica, salaExames=salaExame,
                                              diretorio=diretorioSalas,
                                                nome=nomeSalasArquivo)
    print("="*10 +" 37% " +"="*10)

    print(''
          'OK Limpar os logs\n'
          'OK Limpar as os gráficos\n'
          'OK Verificando os logs\n'
          'OK Criando a folha das salas\n'
          '- Criando a folha do tubo de fluxo\n'
          '- Importando os dados\n'
          '- Gerando gráfico da Sala Técnica\n'
          '- Gerando gráfico da Sala de Exames\n'
          '- Gerando gráfico do Tubo de Fluxo\n')
    #Criando uma aba para o tubo de fluxo
    dataFrameTubo, colunaTuboFluxo = gerarDataframeTuboFluxo(tubofluxo=tuboFluxo, diretorio=diretorioTuboFluxo,
                                            nome=nomeTuboFluxoArquivo)
    print("="*10 +" 49% " +"="*10)

    print(''
          'OK Limpar os logs\n'
          'OK Limpar as os gráficos\n'
          'OK Verificando os logs\n'
          'OK Criando a folha das salas\n'
          'OK Criando a folha do tubo de fluxo\n'
          '- Importando os dados\n'
          '- Gerando gráfico da Sala Técnica\n'
          '- Gerando gráfico da Sala de Exames\n'
          '- Gerando gráfico do Tubo de Fluxo\n')


    #Importando os dataframes no excel
    importarDadosQP(dataFrameSalas,dataFrameTubo,nomeSalasArquivo,nomeTuboFluxoArquivo)

    #Importando os dados padrão para preenchimento do excel
    importarDadosPadrao(padrao, equipamento, salaTecnica, salaExame, tuboFluxo)
    print("="*10 +" 61% " +"="*10)

    print(''
          'OK Limpar os logs\n'
          'OK Limpar as os gráficos\n'
          'OK Verificando os logs\n'
          'OK Criando a folha das salas\n'
          'OK Criando a folha do tubo de fluxo\n'
          'OK Importando os dados\n'
          '- Gerando gráfico da Sala Técnica\n'
          '- Gerando gráfico da Sala de Exames\n'
          '- Gerando gráfico do Tubo de Fluxo\n')
    #Gerando gráfico da Sala Ténica
    gerarGrafico(dataFrames=dataFrameSalas,
                 colunas=colunaEquip,
                 nomeImg=nomeSalaTecnica,
                 titulo=nomeSalaTecnica,
                 posicao="B11")
    print("="*10 +" 73% " +"="*10)

    print(''
          'OK Limpar os logs\n'
          'OK Limpar as os gráficos\n'
          'OK Verificando os logs\n'
          'OK Criando a folha das salas\n'
          'OK Criando a folha do tubo de fluxo\n'
          'OK Importando os dados\n'
          'OK Gerando gráfico da Sala Técnica\n'
          '- Gerando gráfico da Sala de Exames\n'
          '- Gerando gráfico do Tubo de Fluxo\n')

    #Gerando gráfico da Sala de Exames
    gerarGrafico(dataFrames=dataFrameSalas,
                 colunas=colunaExame,
                 nomeImg=nomeSalaExame,
                 titulo=nomeSalaExame,
                 posicao="B36")
    print("="*10 +" 85% " +"="*10)

    print(''
          'OK Limpar os logs\n'
          'OK Limpar as os gráficos\n'
          'OK Verificando os logs\n'
          'OK Criando a folha das salas\n'
          'OK Criando a folha do tubo de fluxo\n'
          'OK Importando os dados\n'
          'OK Gerando gráfico da Sala Técnica\n'
          'OK Gerando gráfico da Sala de Exames\n'
          '- Gerando gráfico do Tubo de Fluxo\n')

    #Gerando gráfico do Tubo de Fluxo
    gerarGrafico(dataFrames=dataFrameTubo,
                 colunas=colunaTuboFluxo,
                 nomeImg=nomeTuboFluxo,
                 titulo=nomeTuboFluxo,
                 posicao="B62")
    print("="*10 +" 100% " +"="*10)
    print(''
          'OK Limpar os logs\n'
          'OK Limpar as os gráficos\n'
          'OK Verificando os logs\n'
          'OK Criando a folha das salas\n'
          'OK Criando a folha do tubo de fluxo\n'
          'OK Importando os dados\n'
          'OK Gerando gráfico da Sala Técnica\n'
          'OK Gerando gráfico da Sala de Exames\n'
          'OK Gerando gráfico do Tubo de Fluxo\n')

    #Incluindo dados no QP
    print("FINALIZADO!!!")

