class Parameter:
    def __init__(self, populationSize = 10, numberGenerations = 10, mutationRate = 0.5, crossoverRate = 60, maxMonthlyProjectValue=50000):
        # tamanho da populacao
        self.populationSize = int(populationSize)
        # numero de gerações
        self.numberGenerations = int(numberGenerations)
        # taxa de mutação 
        self.mutationRate = float(mutationRate)
        # taxa de cruzamento usado para definir numero de trocas que serao feitas
        self.crossoverRate = float(crossoverRate)
        # valor mensal maximo para projeto
        self.maxMonthlyProjectValue = float(maxMonthlyProjectValue)