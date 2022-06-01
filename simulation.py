from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as pb
import pyrosim.pyrosim as ps
import pybullet_data
import time



class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()
        self.physicsClient = pb.connect(pb.GUI)
        pb.setGravity(0,0,-9.81)
        pb.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.planeId = pb.loadURDF("plane.urdf")
        self.robotId = pb.loadURDF("body.urdf")
        pb.loadSDF("world.sdf")
        ps.Prepare_To_Simulate(self.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def __del__(self):
        for i in self.robot.sensors:
            print(self.robot.sensors[i].values)
        pb.disconnect()

    def Run(self):
        for i in range(c.n):
            time.sleep(1/30)
            self.robot.Sense(i)
            self.robot.Act(self.robotId, i)
            pb.stepSimulation()