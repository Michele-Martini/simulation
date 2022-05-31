import pyrosim.pyrosim as ps

length = 1
width = 1
height = 1

x = 0
y = 0
z = height/2

#ps.Start_SDF("boxes.sdf")

#ps.Send_Cube(name="Box1", pos=[x-length,y,z], size=[length,width,height])
#ps.Send_Cube(name="Box2", pos=[x,y,z+height], size=[length,width,height])

ps.Start_SDF("tower.sdf")
for k in range(3):

    for j in range(3):
        h_i = 0

        for i in range(10):
            scale = pow(0.9,i)
            x_i = x + k*length
            y_i = y + j*width
            z_i = h_i + (scale*height)/2
            ps.Send_Cube(name="Box"+str(i), pos=[x_i,y_i,z_i], size=[length*scale,width*scale,height*scale])
            h_i += scale*height

ps.End()