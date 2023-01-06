"""
Gộp file ảnh NG về 1 folder để sử dụng FH convert về bmp
"""

import os
import shutil

# root = "D:\\raw\A77"
# save_file = "D:\\raw\A77\CAM1"
# if not os.path.exists(save_file):
#     os.makedirs(save_file)
# cam = ["CAM_1"]
# for i in cam:
#     root_file = os.path.join(root,i)
#     for root,path,file in os.walk(root_file):
#         print(root,path,file)
#         if file != []:
#             for img in file:
#                 os.replace(os.path.join(root,img),os.path.join(save_file,img))

root = "D:\\DUYLOC\\Report\\2023-01-05"
save_file = "D:\\DUYLOC\\Report\\2023-01-05\\N_2023-01-05"
cam = ["N_2023-01-05"]
for i in cam :
    root_file = os.path.join(root,i)
    for root,path,file in os.walk(root_file):
        print(root,path,file)
        name = root.split("\\")[-1].split('.')[0] + ".bmp"
        if file != [] :
            for img in file :
                os.replace(os.path.join(root,img),os.path.join(save_file,name))