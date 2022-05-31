import matplotlib.pyplot as mplt
import numpy as np

#frontLegSensorValues = np.load("data/targetAngles.npy")#np.load("data/frontLegSensorValues.npy")

T = 100
amplitude = np.pi/4
frequency = (2*np.pi)/T
phaseOffset = 0
n = 1000
targetAngles = np.zeros(n)
for i in range(n):
    targetAngles[i] = amplitude * np.sin(frequency * i + phaseOffset)

mplt.plot(targetAngles)
mplt.show()