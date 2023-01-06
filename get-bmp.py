import os
import glob

root = "D:\\KHA\\datasets\\A93\\another"
save_path = "D:\\KHA\\datasets\\A93\\another-bmp"
for file in glob.glob(root + "/*.bmp"):
    name = file.split('\\')[-1]
    os.replace(file,os.path.join(save_path,name))
