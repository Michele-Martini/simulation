from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as ps


class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}

    def Prepare_To_Act(self):
        for jointName in ps.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            self.motors[jointName].Prepare_To_Act()

    def Act(self, robotId, t):
        for i in self.motors:
            self.motors[i].Set_Value(robotId, t)

    def Prepare_To_Sense(self):
        for linkName in ps.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)