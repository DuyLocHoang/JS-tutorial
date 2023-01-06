"""
Làm đa dạng dữ liệu dùng albumentations

"""

import os
import albumentations as alb
import cv2
import glob
transform = alb.Compose([alb.HorizontalFlip(p=1)],
                        bbox_params=alb.BboxParams(format='yolo', label_fields=['class_labels']))
# # root_path = "ts/ts"
img_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\\data\\A13-BMP\\val\\images\\"
labels_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\\data\\A13-BMP\\val\\labels\\"
aug_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\\data\\A13-BMP\\aug_data\\"

img = cv2.imread("C:\\Users\\vnmuser\\Desktop\\DUYLOC\\data\\class\\MERGE\\train\\images\\2021-12-16_07-03-20-9720_0.bmp")
print(img)
for file in glob.glob(labels_path + '*.txt'):
    bbox_images = []
    labels_names = []
    # print(file)
    img_file = file.split("\\")[-1].split('.')[0] + '.bmp'
    # print(img_file)
    with open(file,'r') as f:
        data = f.readlines()
        for i in data :
            convert = i.split()
            h = [float(i) for i in convert[1:]]
#             print(h)
            bbox_images.append(h)
            labels_names.append(convert[0])
    img = cv2.imread(img_path+img_file)
    # print(img)
    transformed = transform(image = img,bboxes = bbox_images,class_labels=labels_names)
    transformed_image = transformed['image']
    cv2.imwrite(os.path.join(aug_path,"images",file.split("\\")[-1].split('.')[0]+'_hor.bmp'),transformed_image)

    transformed_bboxes = transformed['bboxes']
    transformed_class_labels = transformed['class_labels']
    transform_path = file.split("\\")[-1].split('.')[0] +"_hor.txt"

    with open(os.path.join(aug_path,"labels",transform_path),"w") as f:
        # f.write('\n')
        for i in range(len(transformed_bboxes)) :
            line = [transformed_class_labels[i]] +  list(str(round(i,4)) for i in transformed_bboxes[i])
            data = ' '.join(line)
            f.write(data + '\n')
    
    print('---------------------')
print('\n')

for file in glob.glob(aug_path + "images\\*.bmp"):
    # print(file.split("\\")[-1])
    os.replace(file,img_path + file.split("\\")[-1])

for file in glob.glob(aug_path + "labels\\*.txt"):
    os.replace(file,labels_path + file.split("\\")[-1])