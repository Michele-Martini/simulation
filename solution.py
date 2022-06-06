import os
import numpy as np
import pyrosim.pyrosim as ps
import random
from constants import length, width, height


class SOLUTION:
    def __init__(self):
        self.weights = 2 * np.random.rand(3, 2) - 1

    def Evaluate(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python simulate.py " + mode)  
        with open("fitness.txt", "r") as f:
            self.fitness = float(f.read())

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow,randomColumn] = 2*random.random() - 1

    def Create_World(self):
        ps.Start_SDF("world.sdf")
        ps.Send_Cube(name="Box", pos=[-2,2,0.5], size=[length,width,height])
        ps.End()

    def Create_Body(self):
        ps.Start_URDF("body.urdf")
        ps.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length,width,height])

        ps.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [1,0,1])
        ps.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length,width,height])
   
        ps.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [2,0,1])
        ps.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length,width,height])

        ps.End()

    def Create_Brain(self):
        ps.Start_NeuralNetwork("brain.nndf")
        ps.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        ps.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        ps.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        ps.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
        ps.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(0,2):
                ps.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])

        ps.End()

