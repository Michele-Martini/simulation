#from cmath import pi
import pybullet as pb
import pyrosim.pyrosim as ps
import numpy as np
#import matplotlib.pylab as plt
import pybullet_data
import time
import random

T_b = 100
amplitude_b = np.pi/4
frequency_b = (2*np.pi)/T_b
phaseOffset_b = 0

T_f = 100
amplitude_f = np.pi/4
frequency_f = (2*np.pi)/T_f
phaseOffset_f = np.pi/4

physicsClient = pb.connect(pb.GUI)
pb.setGravity(0,0,-9.81)
pb.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = pb.loadURDF("plane.urdf")
robotId = pb.loadURDF("body.urdf")
pb.loadSDF("world.sdf")
ps.Prepare_To_Simulate(robotId)

n = 400
backLegSensorValues = np.zeros(n)
frontLegSensorValues = np.zeros(n)
back_targetAngles = np.zeros(n)
front_targetAngles = np.zeros(n)
#x = np.linspace(-np.pi, np.pi, n)
#targetAngles = np.sin(x) * (np.pi/4)
for i in range(n):
  time.sleep(1/30)
  pb.stepSimulation()
  back_targetAngles[i] = amplitude_b * np.sin(frequency_b*i + phaseOffset_b)
  front_targetAngles[i] = amplitude_f * np.sin(frequency_f*i + phaseOffset_f)
  backLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("BackLeg")
  frontLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = pb.POSITION_CONTROL, targetPosition = back_targetAngles[i], maxForce = 70)
  ps.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = pb.POSITION_CONTROL, targetPosition = front_targetAngles[i], maxForce = 70)

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
#np.save("data/targetAngles", targetAngles)
pb.disconnect()