from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dados.DadosPadrao import dadosPadrao
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Classes.DadosPadrao import DadosPadrao
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dados.DadosEquipamento import dadosEquipamento
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Classes.DadosEquipamento import DadosEquipamento
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dados.DadosSala import dadosSala
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Classes.DadosSala import DadosSala
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Dados.DadosTuboFluxo import dadosTuboFluxo
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Classes.DadosTuboFluxo import DadosTuboFluxo
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.GerarLogs.GerarLogSalas import verificarLogSalas
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.Geral.LimparLogs import limparLogs
from Qualificacao_Performance_Mecalor.Qualificação_Performance.Função.GerarLogs.GerarLogTuboFluxo import verificarLogTuboFluxo
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


    #Limpando os logs da pasta LogsAtuzalidos
    limparLogs()

    #Verificando, gerando o novo log com os novos dados
    verificarLogSalas(salaExames=salaExame, salaTecnica=salaTecnica, listaLog=listaLog)

    #Verificando e gerando o novo log do tubo de fluxo
    verificarLogTuboFluxo(tuboFluxo=tuboFluxo, listaLog=listaLog)

