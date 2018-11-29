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
from entities.Developer import Developer
from entities.Chromosome import Chromosome
from entities.CombinationElement import CombinationElement

class GeneticService:
    def calculate(parameter=Parameter()):
      developers = [] 
      for dev in data:
        developers.append(Developer(dev))

      # Gera população inicial
      population = GeneticService.generatePopulation(developers, parameter)

      numberGenerations = parameter.numberGenerations
      # Funcao recursiva de novas gerações
      finalGeneration = GeneticService.nextGeneration(population, parameter, 0 , numberGenerations)

      bestIndividuo = sorted(finalGeneration, key = lambda y: (-(y.totalSalary < parameter.maxMonthlyProjectValue), -y.totalKnowledge, +y.totalSalary))[0]
      bestIndividuo.combination = list(filter(lambda x: x.isPresent, bestIndividuo.combination))
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
      newPopulation = populationSorted

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
          combinationElement = CombinationElement() 
          combinationElement.developer = d
          combinationElement.isPresent = False
          chromo.combination.append(combinationElement)

        totalSalary = float(0.0)
        alcancou = True
        while alcancou:
          dev = random.choice(chromo.combination)
          totalSalary += float(dev.developer.salary)
          if totalSalary > parameter.maxMonthlyProjectValue:
            alcancou = False
            break;
          dev.isPresent = True

        
        GeneticService.calculateTotals(chromo)
        population.append(chromo)

      return population

    def handleKnowledge(knowledge):
      upper = knowledge.upper()
      if upper == 'TRAINEE':
          return 1
      elif upper == 'JUNIOR':
          return 4
      elif upper == 'PLENO':
          return 8
      elif upper == 'SENIOR':
          return 12
      elif upper == 'MASTER':
          return 18
      else:
        ValueError("Valor invalido")

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
          chromo.totalKnowledge += GeneticService.handleKnowledge(x.developer.knowledge)
          chromo.totalSalary += float(x.developer.salary)
        

        


