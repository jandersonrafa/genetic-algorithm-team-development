from flask_restful import Resource
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from entities.Parameter import Parameter
from entities.GeneticResponse import GeneticResponse
from services.GeneticService import GeneticService
import json

class GeneticApi(Resource):
    def get(self):
        parameter = Parameter()

        # Gambi para serializar
        lastGeneration = GeneticService.calculate(parameter)
        response = []
        for g in lastGeneration:
            combination = []
            for c in g.combination:
                comb = c
                comb.developer = c.developer.__dict__
                comb.isPresent = 0
                combination.append(comb.__dict__)
            teste = g
            teste.combination = combination
            response.append(teste.__dict__)

        return json.dumps(response)
    def post(self):
        return {"message": "POST Hello, World!"}