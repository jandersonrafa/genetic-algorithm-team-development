from entities.Parameter import Parameter
import json
import os
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)
other_file_path = os.path.join(current_file_dir, "developers.json")
with open(other_file_path) as fi:
  data = json.load(fi)
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from entities.Developer import Developer

class GeneticService:
    def calculate(parameter=Parameter()):
      print(parameter.populationSize)
      print(parameter.minimumTeamSize)
      print(parameter.percentageStop)
      print(parameter.mutationRate)

      developers = [] 
      for dev in data:
        developers.append(Developer(dev))

      return developers