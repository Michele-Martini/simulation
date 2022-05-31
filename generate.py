import pyrosim.pyrosim as ps

def Create_World():
    ps.Start_SDF("world.sdf")
    ps.Send_Cube(name="Box", pos=[-2,2,0.5], size=[length,width,height])
    ps.End()

def Create_Robot():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length,width,height])
    ps.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [1,0,1])

    ps.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length,width,height])
   
    ps.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [2,0,1])
    ps.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length,width,height])

    ps.End()

length = 1
width = 1
height = 1

Create_World()
Create_Robot()