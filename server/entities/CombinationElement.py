class CombinationElement:
    def __init__(self, data):
        if data is None:
            self.name = ""
            self.knowledge = ""
            self.knowledgeValue = None
            self.id = None
            self.salary = None
            self.isPresent = False
        else:
            self.name = data['name']
            self.knowledge = data['knowledge']
            self.knowledgeValue = data['knowledgeValue']
            self.id = data['id']
            self.salary = data['salary']
            self.isPresent = False