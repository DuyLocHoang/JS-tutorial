"""
Chia tập dữ liệu thành tập train và validation
"""

# import os
# import shutil
# img_path = "D:\\raw\\class\\merge\\images"

# label_path = "D:\\raw\\class\\merge\\labels"

# # class_names = ["divat","matbactruc","me","namchamcao","nut","traybactruc"]

# save_path = "D:\\raw\\class\\merge\\"
# img_files = []

# if not os.path.exists(os.path.join(save_path,"train","images")):
#     os.makedirs(os.path.join(save_path,"train","images"))
#     os.makedirs(os.path.join(save_path,"train","labels"))
#     os.makedirs(os.path.join(save_path,"val","images"))
#     os.makedirs(os.path.join(save_path,"val","labels"))


# for img in os.listdir(img_path):
#     data = img.split('.')[0]
#     img_files.append(data)


# number = round(len(img_files)*0.8)
# print(number)


# for i in range(number):
#     shutil.copy(os.path.join(img_path,img_files[i]+".bmp"),os.path.join(save_path,"train","images",img_files[i]+".bmp"))
#     shutil.copy(os.path.join(label_path,img_files[i]+".txt"),os.path.join(save_path,"train","labels",img_files[i]+".txt"))

# for j in range(round(len(img_files)*0.8),len(img_files)):
#     shutil.copy(os.path.join(img_path,img_files[j]+".bmp"),os.path.join(save_path,"val","images",img_files[j]+".bmp"))
#     shutil.copy(os.path.join(label_path,img_files[j]+".txt"),os.path.join(save_path,"val","labels",img_files[j]+".txt"))

import pandas as pd 
import glob
import os
from sklearn.model_selection import train_test_split
import shutil

def split_img_label_into_folder(data_train,data_test,folder_train,folder_test):
    # print(data_train[0])    
    # print(data_test)
    for file in data_train :
        names = file.split("\\")[-1].split('.')[0]
        file_txt = os.path.join(label_path, names + ".txt")
        shutil.copy(file,os.path.join(folder_train,"images",names + ".bmp"))
        shutil.copy(file_txt,os.path.join(folder_train,"labels",names + ".txt"))
    
    for file in data_test:
        names = file.split("\\")[-1].split('.')[0]
        file_txt = os.path.join(label_path, names + ".txt")
        shutil.copy(file,os.path.join(folder_test,"images",names + ".bmp"))
        shutil.copy(file_txt,os.path.join(folder_test,"labels",names + ".txt"))        

# -----------------------------------------------
img_path = "D:\\raw\A76\CAM1\\bactruc\\images"
label_path = "D:\\raw\A76\CAM1\\bactruc\\labels"
folder_train = "D:\\raw\A76\CAM1\\bactruc\\train"
folder_test = "D:\\raw\A76\CAM1\\bactruc\\val"
# -----------------------------------------------
img_list = glob.glob(img_path + "/*.bmp")

if not os.path.exists(folder_train):
    os.makedirs(os.path.join(folder_train,"images"))
    os.makedirs(os.path.join(folder_train,"labels"))

if not os.path.exists(folder_test):
    os.makedirs(os.path.join(folder_test,"images"))
    os.makedirs(os.path.join(folder_test,"labels"))

df = pd.DataFrame(img_list)

data_train, data_test, labels_train, labels_test = train_test_split(df[0], df.index, test_size=0.20, random_state=42)

split_img_label_into_folder(data_train,data_test,folder_train,folder_test)
