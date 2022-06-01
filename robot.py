from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as ps


class ROBOT:
    def __init__(self):
        self.sensors = {}#SENSOR()
        self.motors = {}#MOTOR()

    def Prepare_To_Act(self):
        for jointName in ps.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Prepare_To_Sense(self):
        for linkName in ps.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)
        #backLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #frontLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("FrontLeg")