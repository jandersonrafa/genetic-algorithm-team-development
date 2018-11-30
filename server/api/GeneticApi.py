from flask_restful import Resource, request
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from entities.Parameter import Parameter
from entities.GeneticResponse import GeneticResponse
from services.GeneticService import GeneticService
import json

class GeneticApi(Resource):
    def get(self):
        args = request.args
        if 'populationSize' in args:
            populationSize = args['populationSize']
        else:
            populationSize = 10

        if 'numberGenerations' in args:
            numberGenerations = args['numberGenerations']
        else:
            numberGenerations = 10

        if 'mutationRate' in args:
            mutationRate = args['mutationRate']
        else:
            mutationRate = 0.5

        if 'crossoverRate' in args:
            crossoverRate = args['crossoverRate']
        else:
            crossoverRate = 60

        if 'maxMonthlyProjectValue' in args:
            maxMonthlyProjectValue = args['maxMonthlyProjectValue']
        else:
            maxMonthlyProjectValue = 50000

        parameter = Parameter(populationSize, numberGenerations, mutationRate, crossoverRate, maxMonthlyProjectValue)

        # Gambi para serializar
        bestIndividuo = GeneticService.calculate(parameter)
        combination = []
        for c in bestIndividuo.combination:
            combination.append(c.__dict__)
        bestIndividuo.combination = combination
        response = bestIndividuo.__dict__

        return json.dumps(response)
        # return "asdsad"
    def post(self):
        return {"message": "POST Hello, World!"}