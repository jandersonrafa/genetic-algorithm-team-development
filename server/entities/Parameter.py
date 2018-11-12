class Parameter:
    def __init__(self):
        # tamanho da populacao
        self.populationSize = 10
        # tamanho minimo do time servindo como criterio para parada, repensar possibilidade de parada ser numero de geracoes
        self.minimumTeamSize = 5
        # percentual de parada usado para calcular valor aceitavel de (tamanho de time  * grau conhecimento master )
        self.percentageStop = 80
        # taxa de mutação 
        self.mutationRate = 0.5
        # taxa de cruzamento usado para definir numero de trocas que serao feitas
        self.crossoverRate = 60
        # elitism rate
        self.elitismRate = 0