# Remove cac file khong dc label

import os 
import glob

label_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\data\\class\\test\\val\\labels"
img_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\data\\class\\test\\val\\images"
labels_file = []
for label in os.listdir(label_path):
    data = label.split('.')[0]
    # print(label.split('.')[0])
    if data != "classes":
        labels_file.append(data)
    # print(labels_file)
print(len(labels_file))
i = 0
k = 0
img_files = []
for img in os.listdir(img_path):
    data = img.split('.')[0]
    img_files.append(data)
    k += 1
    if data not in labels_file:
        i += 1
        os.remove(os.path.join(img_path,img))
print(len(img_files))
# print(k-i)
        # os.remove(os.path.join(img_path,img))

for label in os.listdir(label_path):
    data = label.split('.')[0]
    k += 1
    if data not in img_files:
        i += 1
        os.remove(os.path.join(label_path,label))
# print(k-i)