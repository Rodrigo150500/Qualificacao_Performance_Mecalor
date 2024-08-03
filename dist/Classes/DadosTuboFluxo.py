class DadosTuboFluxo():
    def __init__(self, minTemp, maxTemp, setTemp, minVazao, maxVazao, setVazao):
        self.minTemp = int(minTemp)
        self.maxTemp = int(maxTemp)
        self.setTemp = int(setTemp)
        self.minVazao = int(minVazao)
        self.maxVazao = int(maxVazao)
        self.setVazao = int(setVazao)
        self.obs = None