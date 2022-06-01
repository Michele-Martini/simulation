import constants as c
import numpy as np
#import pybullet as pb
import pyrosim.pyrosim as ps

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        #self.values = np.zeros(c.n)
