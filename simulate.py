import pybullet as pb
import time

physicsClient = pb.connect(pb.GUI)
for i in range(1000):
  time.sleep(1/30)
  print(i)
  pb.stepSimulation()
pb.disconnect()