import json

class Developer(object):
    def __init__(self, data):
        self.name = data['name']
        self.knowledge = data['knowledge']
        self.salary = data['salary']