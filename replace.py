import glob
import os 
import shutil
img_path = "D:\\raw\A76\CAM1\\ngang\\images"
root = "D:\\raw\A76\CAM1\\bactruc\labels"
save_path = "D:\\raw\A76\CAM1\\bactruc\images"

# if not os.path.exists(save_path):
#     os.makedirs(save_path)

for file in glob.glob(root + "/*.txt"):
    name = file.split("\\")[-1].split('.')[0] + ".bmp"
    shutil.copy(os.path.join(img_path,name),os.path.join(save_path,name))