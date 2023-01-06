"""
Nếu ảnh không tồn tại thì xóa labels
Nếu ảnh tồn tại thì đổi địa chỉ lưu 
"""

import os 
import glob
img_path = "D:\\raw\\A06\\CAM_2\\doc\\images"
label_path = "D:\\raw\\A06\\CAM_2\\doc\\labels"
# save_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\\data\\A13-BMP\\train\\images"

labels = []
for file in os.listdir(label_path):
    label_file = file.split('.')[0] + ".txt"
    if not os.path.exists(os.path.join(img_path,label_file)):
        os.remove(os.path.join(label_path,file))
    # else:
    #     os.replace(os.path.join(img_path,img_file),os.path.join(save_path,img_file))

    # print(data)