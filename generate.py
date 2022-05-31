import pyrosim.pyrosim as ps

def Create_World():
    ps.Start_SDF("world.sdf")
    ps.Send_Cube(name="Box", pos=[x-2,y+2,z], size=[length,width,height])
    ps.End()

def Create_Robot():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="BackLeg", pos=[x,y,z], size=[length,width,height])
    ps.Send_Joint(name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [1,0,1])

    ps.Send_Cube(name="Torso", pos=[0.5,0,0.5], size=[length,width,height])

    ps.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,0,0])
    ps.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length,width,height])

    ps.End()

length = 1
width = 1
height = 1

x = 0.5
y = 0
z = 0.5

Create_World()
Create_Robot()