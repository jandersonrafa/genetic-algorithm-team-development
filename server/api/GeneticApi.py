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

        # list response test
        return json.dumps([ob.__dict__ for ob in GeneticService.calculate(parameter)[0:10]])
        # return json.dumps(listResponse.__dict__)
    def post(self):
        return {"message": "POST Hello, World!"}