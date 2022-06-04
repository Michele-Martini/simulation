import constants as c
import numpy as np
import pybullet as pb
import pyrosim.pyrosim as ps

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, robotId, desiredAngle):
        ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = pb.POSITION_CONTROL, 
                                  targetPosition = desiredAngle, maxForce = 70)