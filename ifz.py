import glob
import os

root = "D:\\raw\A77\CAM2"
for img_path in glob.glob(root +"/*.ifz"):
    os.remove(img_path)