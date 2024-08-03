class DadosPadrao():
    def __init__(self, nome, sigla, cliente, OS, dataColeta):
        self.nome = nome
        self.sigla = sigla
        self.cliente = cliente
        self.OS = OS
        self.dataColeta = dataColeta
        self.aprovacao = None

    def aprovar(self, txt):
        self.aprovacao = txt

