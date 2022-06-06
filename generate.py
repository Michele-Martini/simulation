import pyrosim.pyrosim as ps
import random
from constants import length, width, height

def Create_World():
    ps.Start_SDF("world.sdf")
    ps.Send_Cube(name="Box", pos=[-2,2,0.5], size=[length,width,height])
    ps.End()

def Generate_Body():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length,width,height])

    ps.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [1,0,1])
    ps.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length,width,height])
   
    ps.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [2,0,1])
    ps.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length,width,height])

    ps.End()

def Generate_Brain():
    ps.Start_NeuralNetwork("brain.nndf")
    ps.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    ps.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    ps.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    ps.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
    ps.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")

    for i in range(3):
        for j in range(3,5):
            ps.Send_Synapse(sourceNeuronName = i, targetNeuronName = j, weight = random.uniform(-1.0, 1.0))

    ps.End()

Create_World()
Generate_Body()
Generate_Brain()