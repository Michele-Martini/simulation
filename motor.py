import constants as c
import numpy as np
import pybullet as pb
import pyrosim.pyrosim as ps

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(c.n)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude_b
        self.frequency = c.frequency_b
        self.offset = c.phaseOffset_b
        for t in range(c.n):
            self.motorValues[t] = self.amplitude * np.sin(self.frequency * t + self.offset)

    def Set_Value(self, robotId, t):
        ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = pb.POSITION_CONTROL, 
                                  targetPosition = self.motorValues[t], maxForce = 70)