import glob
import os

folder = "D:\\Kha\\raw\\A06-CONVERT\\CAM_1"

for file in glob.glob(folder + "/*.ifz"):
    os.remove(file)
