"""
lấy những ảnh đã được labels
"""


import os 
import glob

label = "D:\\raw\A05\CAM_1\doc\labels"
save_img = "D:\\raw\A05\CAM_1\doc\images"
root_img = "D:\\raw\A05\CAM1"
for file in glob.glob(label + "/*.txt"):
    name  = file.split("\\")[-1].split(".")[0] + ".bmp"
    os.replace(os.path.join(root_img,name), os.path.join(save_img,name))