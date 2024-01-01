class DadosPadrao():
    def __init__(self):
        self.nome
        self.sigla
        self.cliente
        self.OS
        self.dataColeta
        self.aprovacao = None

    def aprovar(self, txt):
        self.aprovacao = txt

    def cadastrar(self, nome, sigla, cliente, OS, dataColeta):
        self.nome = nome
        self.sigla = sigla
        self.cliente = cliente
        self.OS = OS
        self.dataColeta = dataColeta