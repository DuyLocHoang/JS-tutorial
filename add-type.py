import glob
import os 
root = "D:\\raw\A02\CAM_1\doc\same_img"
for i in glob.glob(root + "/*"):
    name = i.split("\\")[-1]
    new_name = name + ".bmp"
    # print(name)
    os.renames(os.path.join(root,name),os.path.join(root,new_name))
