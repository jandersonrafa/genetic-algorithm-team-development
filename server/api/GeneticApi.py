from flask_restful import Resource
import random

class GeneticApi(Resource):
    def get(self):
        return {"message": "GET Hello, World!" + str(random.randint(1,99999))}
    def post(self):
        return {"message": "POST Hello, World!"}