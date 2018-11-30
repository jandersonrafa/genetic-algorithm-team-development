from entities.Parameter import Parameter
import copy
import json
import os
import numpy
import random
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)
other_file_path = os.path.join(current_file_dir, "developers.json")
with open(other_file_path) as fi:
  data = json.load(fi)
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# from entities.Developer import Developer
from entities.Chromosome import Chromosome
from entities.CombinationElement import CombinationElement

class GeneticService:
    def findAll():
      developers = [] 
      for dev in data:
        developers.append(CombinationElement(dev))

      return developers

    def calculate(parameter=Parameter()):
      developers = [] 
      for dev in data:
        developers.append(CombinationElement(dev))

      # Gera população inicial
      population = GeneticService.generatePopulation(developers, parameter)

      numberGenerations = parameter.numberGenerations
      # Funcao recursiva de novas gerações
      finalGeneration = GeneticService.nextGeneration(population, parameter, 0 , numberGenerations)

      bestIndividuo = sorted(finalGeneration, key = lambda y: (-(y.totalSalary < parameter.maxMonthlyProjectValue), -y.totalKnowledge, +y.totalSalary))[0]
      elementsPresent = []
      for element in bestIndividuo.combination:
        if element.isPresent:
          elementsPresent.append(element)
      # bestIndividuo.combination = list(filter(lambda x: x.isPresent, bestIndividuo.combination))
      bestIndividuo.combination = elementsPresent
      return bestIndividuo

    def nextGeneration(population, parameter, count, numberGenerations):
      # teste = sorted(population, key = lambda y: (-(y.totalSalary < parameter.maxMonthlyProjectValue), -y.totalKnowledge, +y.totalSalary))[0]
      count = count +1
      if (count >= numberGenerations):
        return population
      
      # numero de elementos que serão substituido na populacao
      numberElementsReplacement = int(len(population) * (parameter.crossoverRate / 100))
      # ordena por fitness populacao
      populationSorted = sorted(population, key = lambda y: (-(y.totalSalary < parameter.maxMonthlyProjectValue), -y.totalKnowledge, +y.totalSalary))
      # newPopulation = copy.deepcopy(populationSorted)
      newPopulation = GeneticService.clonePopulation(populationSorted)

      # obtem lista de filhos apartir de cruzamento
      childrensByCrossover = GeneticService.handleCrossover(populationSorted, numberElementsReplacement)

      # aplica mutação nos filhos gerados
      childrensMutation = GeneticService.handleMutation(childrensByCrossover, parameter.mutationRate)

      childrensMutationSorted = sorted(childrensMutation, key = lambda y: (-y.totalKnowledge, y.totalSalary))

      # remove elementos piores no ranking 
      newPopulation = newPopulation[0:len(newPopulation) - numberElementsReplacement]
      
      # adiciona filhos mutados e resultados de cruzamentos
      for child in childrensMutationSorted:
        newPopulation.append(child)

      return GeneticService.nextGeneration(newPopulation, parameter, count, numberGenerations)

    def generatePopulation(developers, parameter=Parameter()):
      population = []
      for x in range(0, parameter.populationSize):
        chromo = Chromosome()
        for d in developers:
          element = CombinationElement(None)
          element.name = d.name
          element.knowledge = d.knowledge
          element.knowledgeValue = d.knowledgeValue
          element.id = d.id
          element.salary = d.salary
          element.isPresent = d.isPresent
          chromo.combination.append(element)

        totalSalary = float(0.0)
        alcancou = True
        while alcancou:
          dev = random.choice(chromo.combination)
          if dev.isPresent:
            continue
          totalSalary += float(dev.salary)
          if totalSalary > parameter.maxMonthlyProjectValue:
            alcancou = False
            break;
          dev.isPresent = True
        GeneticService.calculateTotals(chromo)
        population.append(chromo)

      return population

      # if upper == 'TRAINEE':
      #     return 1 a 3
      # elif upper == 'JUNIOR':
      #     return 4 a 7
      # elif upper == 'PLENO':
      #     return 8 a 11
      # elif upper == 'SENIOR':
      #     return 12 a 17
      # elif upper == 'MASTER':
      #     return 18 a 22

    def handleCrossover(populationSorted, numberElementsReplacement):
      bestParents = populationSorted[0:int(numberElementsReplacement)]
      positionArrayToBreak = int(len(populationSorted[0].combination) / 2)

      childrens = []
      for x in range(0, int(len(bestParents)/2)):
        father = random.choice(bestParents) 
        bestParents.remove(father) 

        mother = random.choice(bestParents) 
        bestParents.remove(mother) 
        childrenOne = Chromosome()
        childrenOne.combination = father.combination[0:positionArrayToBreak] + mother.combination[positionArrayToBreak: len(mother.combination)]
  
        childrens.append(childrenOne)
        
        childrenTwo = Chromosome()
        childrenTwo.combination = mother.combination[0:positionArrayToBreak] + father.combination[positionArrayToBreak: len(father.combination)]
        childrens.append(childrenTwo)

      return childrens

    def handleMutation(childrensByCrossover, mutationRate):
      childrensMutation = childrensByCrossover
      numberPositionsMutation = int(len(childrensMutation[0].combination) * (mutationRate/100))
      for dev in childrensMutation:
        for x in range(0, numberPositionsMutation):
          elementMutation = random.choice(dev.combination) 
          elementMutation.isPresent = not elementMutation.isPresent

      for x in childrensMutation:
        GeneticService.calculateTotals(x)

      return childrensMutation

    def calculateTotals(chromo):
      for x in chromo.combination:
        if x.isPresent:
          chromo.totalKnowledge += x.knowledgeValue
          chromo.totalSalary += float(x.salary)
        
    def clonePopulation(populationSorted): 
      newPopulation = [] 
      for sort in populationSorted:
        chromo = Chromosome()
        elementsPresent = []
        for d in sort.combination:
          element = CombinationElement(None)
          element.name = d.name
          element.knowledge = d.knowledge
          element.knowledgeValue = d.knowledgeValue
          element.id = d.id
          element.salary = d.salary
          element.isPresent = d.isPresent
          elementsPresent.append(element)
        chromo.combination = elementsPresent
        chromo.totalSalary = sort.totalSalary
        chromo.totalKnowledge = sort.totalKnowledge
        newPopulation.append(chromo)
      return newPopulation
        


