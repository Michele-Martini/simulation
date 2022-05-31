import pybullet as pb
import pybullet_data
import time

physicsClient = pb.connect(pb.GUI)
pb.setGravity(0,0,-9.81)
pb.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = pb.loadURDF("plane.urdf")
robotId = pb.loadURDF("body.urdf")
pb.loadSDF("world.sdf")
for i in range(600):
  time.sleep(1/30)
  print(i)
  pb.stepSimulation()
pb.disconnect()