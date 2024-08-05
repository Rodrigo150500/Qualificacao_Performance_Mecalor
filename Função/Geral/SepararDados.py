def separarDados(listaLog, opcao):
    for item in listaLog:

        diretorioLog = item["Diretorio"]
        nomeArquivoLog = item["Log"]
        nomeOpcao = item["Opcao"]


        print(f'separar dados {diretorioLog}')
        if (item["Input"] == opcao):
            return diretorioLog, nomeArquivoLog, nomeOpcao
        elif (item["Input"] == opcao or item["Input"] == opcao):
            return diretorioLog, nomeArquivoLog, nomeOpcao
        elif (item["Input"] == opcao):
            return diretorioLog, nomeArquivoLog, nomeOpcao
        elif (item["Input"] == opcao):
            return diretorioLog, nomeArquivoLog, nomeOpcao
