from solution import SOLUTION
from constants import numberOfGenerations
import copy

class HILLCLIMBER:
    def __init__(self):
        # Hillclimber is an instance of a solution, comprising a world (environment), a body (agent), and a brain (controller)

        self.parent = SOLUTION()


    def Evolve(self):
        self.parent.Evaluate("DIRECT")

        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()
            if currentGeneration == 0 or currentGeneration == numberOfGenerations-1:
                #self.Print()
                pass


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()


    def Spawn(self):
        self.child = copy.deepcopy(self.parent)


    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child


    def Print(self):
        print("\n----------")
        print(self.parent.fitness, self.child.fitness)
        print("---------- \n")


    def Show_Best(self):
        self.parent.Evaluate("GUI")