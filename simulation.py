from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as pb
import pyrosim.pyrosim as ps
import pybullet_data
import time



class SIMULATION:
    def __init__(self, directOrGUI):
        self.world = WORLD()
        self.robot = ROBOT()
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = pb.connect(pb.DIRECT)
        else:
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
        pb.disconnect()

    def Run(self):
        for i in range(c.n):
            if self.directOrGUI == "GUI":
                time.sleep(1/30)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(self.robotId)
            pb.stepSimulation()

    def Get_Fitness(self):
        self.robot.Get_Fitness(self.robotId, 0)