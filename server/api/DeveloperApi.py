from flask_restful import Resource, request
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from entities.Parameter import Parameter
from entities.GeneticResponse import GeneticResponse
from services.GeneticService import GeneticService
import json

class DeveloperApi(Resource):
    def get(self):
        developers = GeneticService.findAll()

        return json.dumps([ob.__dict__ for ob in developers])