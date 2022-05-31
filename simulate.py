import pybullet as pb
import pyrosim.pyrosim as ps
import numpy as np
import pybullet_data
import time

physicsClient = pb.connect(pb.GUI)
pb.setGravity(0,0,-9.81)
pb.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = pb.loadURDF("plane.urdf")
robotId = pb.loadURDF("body.urdf")
pb.loadSDF("world.sdf")
ps.Prepare_To_Simulate(robotId)

n = 150
frontLegSensorValues = np.zeros(n)
for i in range(n):
  time.sleep(1/30)
  #print(i)
  pb.stepSimulation()
  frontLegSensorValues[i] = ps.Get_Touch_Sensor_Value_For_Link("FrontLeg")

np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
pb.disconnect()