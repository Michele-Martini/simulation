import matplotlib.pyplot as mplt
import numpy as np

frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
mplt.plot(frontLegSensorValues)
mplt.show()