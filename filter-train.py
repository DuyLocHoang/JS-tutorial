import glob
import os
from subprocess import check_call
from tabnanny import check
root = "D:\\raw\divat"
# img_file = ""
save_path = "D:\\raw\divat\\namcham"

if not os.path.exists(save_path) :
    os.makedirs(os.path.join(save_path,"images"))
    os.makedirs(os.path.join(save_path,"labels"))

files=  []
for file in glob.glob(root +"/labels"+ "/*.txt") :
    # files = []
    name = file.split("\\")[-1].split(".")[0]
    print(name)
    # break
    check = False
    with open(file,'r') as f :
        lines = f.readlines()
        arr = []
        for line in lines :
            classes = line.split(' ')[0]
            arr.append(classes)
        # print(arr)cd 
        if len(arr) == 1 or len(arr) == 0 :
            if '2' not in arr :
                # print(arr)
                # print(file)
                # print(file.split('\\')[-1])
                check = True

    check = True
    # # print(check)
    if check:
        files.append(file)
        os.replace(file,os.path.join(save_path,"labels",file.split("\\")[-1]))
        os.replace(os.path.join(root,"images",name + ".bmp"),os.path.join(save_path,"images",name + ".bmp"))

# print(files)
# for 
# os.replace()

    # print(files)
