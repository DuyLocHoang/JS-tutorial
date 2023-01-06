import os
import glob

label_path_kim = "D:\LOC\yolov5\\runs\detect\A77-CAM1-2kim\labels"
label_path = "D:\\raw\A77\CAM1\doc\labels"
for file in glob.glob(label_path_kim +"/*.txt"):
    name = file.split("\\")[-1].split(" ")[0]
    print(name)
    with open(file,'r') as f:
            lines = f.readlines()
    line = [data.split() for data in lines]
    print(line)
    # print(name)
    # with open()
    with open(os.path.join(label_path,name), 'a') as f :
        for data in line :
            if data[0] == "8":
                l = " ".join(data)
                f.write(l)
                f.write("\n")
    # break