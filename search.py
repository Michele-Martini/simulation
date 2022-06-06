import os
from hillclimber import HILLCLIMBER

hc = HILLCLIMBER()
hc.Evolve()
hc.Show_Best()


#for i in range(2):
#    os.system("python generate.py")
#    os.system("python simulate.py")