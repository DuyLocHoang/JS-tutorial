import os
import glob 

# ================================================================
# Xuat file txt

label_path = "D:\LOC\yolov5\\runs\detect\A77-CAM1\labels"
txt_file = "filter-A77-CAM1.txt"
# i = 0
for label_file in glob.glob(label_path + "/*.txt"):
    with open(label_file,'r') as f :
        lines = f.readlines()
        lines = [data.split() for data in lines]
    classes = []
    for line in lines :
        classes.append(line[0])
    print(classes)
    if not (len(classes) == 0 or len(classes) == 1) :
        if "2" not in classes:
            if not os.path.exists(txt_file):
                with open(txt_file,'w') as f :
                    f.write(label_file)
                    f.write("\n")
            else :
                with open(txt_file,'a') as f :
                    f.write(label_file)
                    f.write("\n")            
    
    # if i == 4:
    #     break 
    # i += 1 

#==================================================================
# Doc anh va split img

img_path = "D:\\raw\A77\CAM1\doc"
txt_file = "filter-A77-CAM1.txt"
filter_folder = os.path.join(img_path,"filter")
with open(txt_file,'r') as f:
    lines = f.readlines()
for line in lines :
    name = line.split('\\')[-1].split(".")[0] + ".bmp"
    print(name)
    if not os.path.exists(filter_folder) :
        os.makedirs(filter_folder)
    os.replace(os.path.join(img_path,name), os.path.join(filter_folder,name))
