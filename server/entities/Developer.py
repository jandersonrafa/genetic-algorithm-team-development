import json

class Developer(object):
    def __init__(self, data):
        self.name = data['name']
        self.knowledge = data['knowledge']
        self.knowledgeValue = data['knowledgeValue']
        self.id = data['id']
        self.salary = data['salary']