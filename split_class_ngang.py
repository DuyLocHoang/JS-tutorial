"""
Split file NG-OK về các class lỗi 
"""

from glob import glob
import os
import glob
labels_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\lib\\yolov5\\runs\\detect\\labels"
images_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\lib\\yolov5\\runs\\detect\\exp13-"
save_path = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\lib\\yolov5\\runs\\detect\\NGANG-exp13"
class_names = ["kim","divat","me","loikim","traybactruc","matbactruc","nut"]

label_files = []

for label in os.listdir(labels_path):
    data = label.split('.')[0]
    if data != 'classes':
        label_files.append(data)

for img in os.listdir(images_path):
    data = img.split('.')[0]
    if data not in label_files:
        if not os.path.exists(os.path.join(save_path,"Error","labels")):
            os.makedirs(os.path.join(save_path,"Error","labels"))
            os.makedirs(os.path.join(save_path,"Error","images"))
        os.replace(os.path.join(images_path,data+".bmp"),os.path.join(save_path,"Error","images",data + ".bmp"))



for file in glob.glob(os.path.join(labels_path,"*.txt")):
    # print(file)
    file_names = file.split('\\')[-1].split('.')[0]
    # print(file_names)
    check = []

    if file_names != 'classes':
        with open(file,'r') as f:
            data = f.readlines()
            for i in data :
                convert = i.split()[0]
                # print(convert)
                check.append(convert)
        print(check)
        # if check == [] :
        #     if not os.path.exists(os.path.join(save_path,"Error","labels")):
        #         os.makedirs(os.path.join(save_path,"Error","labels"))
        #         os.makedirs(os.path.join(save_path,"Error","images"))
        #     os.replace(file,os.path.join(save_path,"Error","labels",file.split('\\')[-1]))
        #     os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"Error","images",file_names+".bmp"))

        for i in check :
            if i == "3":
                if not os.path.exists(os.path.join(save_path,"loikim","labels")):
                    os.makedirs(os.path.join(save_path,"loikim","labels"))
                    os.makedirs(os.path.join(save_path,"loikim","images"))
                print(file,os.path.join(save_path,"loikim","labels",file.split('\\')[-1]))
                os.replace(file,os.path.join(save_path,"loikim","labels",file.split('\\')[-1]))
                os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"loikim","images",file_names + ".bmp"))
                break
            if i == "2":
                if not os.path.exists(os.path.join(save_path,"me","labels")):
                    os.makedirs(os.path.join(save_path,"me","labels"))
                    os.makedirs(os.path.join(save_path,"me","images"))
                os.replace(file,os.path.join(save_path,"me","labels",file.split('\\')[-1]))
                os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"me","images",file_names+".bmp"))
                break
            if i == "1":
                if not os.path.exists(os.path.join(save_path,"divat","labels")):
                    os.makedirs(os.path.join(save_path,"divat","labels"))
                    os.makedirs(os.path.join(save_path,"divat","images"))
                os.replace(file,os.path.join(save_path,"divat","labels",file.split('\\')[-1]))
                os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"divat","images",file_names+".bmp"))
                break
            if i == "5":
                if not os.path.exists(os.path.join(save_path,"matbactruc","labels")):
                    os.makedirs(os.path.join(save_path,"matbactruc","labels"))
                    os.makedirs(os.path.join(save_path,"matbactruc","images"))
                os.replace(file,os.path.join(save_path,"matbactruc","labels",file.split('\\')[-1]))
                os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"matbactruc","images",file_names+".bmp"))
                break
            if i == "4":
                if not os.path.exists(os.path.join(save_path,"traybactruc","labels")):
                    os.makedirs(os.path.join(save_path,"traybactruc","labels"))
                    os.makedirs(os.path.join(save_path,"traybactruc","images"))
                os.replace(file,os.path.join(save_path,"traybactruc","labels",file.split('\\')[-1]))
                os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"traybactruc","images",file_names+".bmp"))
                break
            if i == "6":
                if not os.path.exists(os.path.join(save_path,"nut","labels")):
                    os.makedirs(os.path.join(save_path,"nut","labels"))
                    os.makedirs(os.path.join(save_path,"nut","images"))
                os.replace(file,os.path.join(save_path,"nut","labels",file.split('\\')[-1]))
                os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"nut","images",file_names+".bmp"))
                break
            # if i == "6":
            #     if not os.path.exists(os.path.join(save_path,"divatkim","labels")):
            #         os.makedirs(os.path.join(save_path,"divatkim","labels"))
            #         os.makedirs(os.path.join(save_path,"divatkim","images"))
            #     os.replace(file,os.path.join(save_path,"divatkim","labels",file.split('\\')[-1]))
            #     os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"divatkim","images",file_names+".bmp"))
            #     break
            # if i == "":
            #     if not os.path.exists(os.path.join(save_path,"Error","labels")):
            #         os.makedirs(os.path.join(save_path,"Error","labels"))
            #         os.makedirs(os.path.join(save_path,"Error","images"))
            #     os.replace(file,os.path.join(save_path,"Error","labels",file.split('\\')[-1]))
            #     os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"Error","images",file_names+".bmp"))
            #     break
            # if i == "0":
            #     if not os.path.exists(os.path.join(save_path,"namcham","labels")):
            #         os.makedirs(os.path.join(save_path,"namcham","labels"))
            #         os.makedirs(os.path.join(save_path,"namcham","images"))
            #     os.replace(file,os.path.join(save_path,"namcham","labels",file.split('\\')[-1]))
            #     os.replace(os.path.join(images_path,file_names+".bmp"),os.path.join(save_path,"namcham","images",file_names+".bmp"))
            #     break
                        

        print("----------------------")