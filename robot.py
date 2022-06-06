from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as ps
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Act(self):
        for jointName in ps.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, robotId):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(robotId, desiredAngle)

    def Prepare_To_Sense(self):
        for linkName in ps.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
