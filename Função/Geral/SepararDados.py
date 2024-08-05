def separarDados(listaLog, opcao):
    for item in listaLog:
        if (item["Input"] == opcao["Sala Exames/Sala Técnica"]):
            diretorioLog = item["Diretorio"]
            nomeArquivoLog = item["Log"]
            nomeOpcao = item["Opcao"]

            return diretorioLog, nomeArquivoLog, nomeOpcao

        elif (item["Input"] == opcao[""])