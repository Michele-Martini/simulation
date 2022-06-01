import constants as c
import numpy as np
#import pybullet as pb
import pyrosim.pyrosim as ps

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.n)

    def Get_Value(self, t):
        self.values[t] = ps.Get_Touch_Sensor_Value_For_Link(self.linkName)
        