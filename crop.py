from cProfile import label
from unicodedata import name
import cv2
import glob
import torch 
import os 
import time
import numpy as np

# model_path = "D:\\LOC\\yolov5\\weights\\best-6.pt"
# model = torch.hub.load("yolov5","custom",path = model_path, source = "local", force_reload = False)
#-------------------------CROP ALL IMAGES ---------------------------------------
root = "D:\\DUYLOC\\Report\\2022-11-18\\MAT-R\\NQVL-NG-judgement"
crop_path = f"{root}\\crop"
if not os.path.exists(crop_path + "/kim"):
    os.makedirs(os.path.join(crop_path,"images"))
    # os.makedirs(os.path.join(crop_path,"kim"))
    # os.makedirs(os.path.join(crop_path,"bactruc"))
#     os.makedirs(os.path.join(crop_path,"labels"))    
# doc = (860 ,60)
# label_path = "D:\\DUYLOC\\merge\\labels"
# dim = None
# width_crop,height_crop = None
for file in glob.glob(root + "/*.bmp"):
    start_time = time.time()
    img = cv2.imread(file)
    name_img = file.split("\\")[-1].split('.')[0]
    scale_percent = 100 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    # print(width,height)
    dim = (width, height) #1600-1200
    img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
    # Ngoai quan motor-doc
    x1,x2,y1,y2 = 157/640,501/640,26/480,426/480 #Standard
    img = img[int(y1*height)+50:int(y2*height)+10,int(x1*width)-20:int(x2*width)-20]

    # Ngoai quan motor-ngang
    # x1,x2,y1,y2 = 101/640,532/640,76/480,389/480 #Standard
    # img = img[int(y1*height):int(y2*height),int(x1*width):int(x2*width)]
    # print(img.shape)
    # print(img.shape[1],img.shape[0])
    # height = int(img.shape[0] * scale_percent / 100)
    # img1 = img[100:500,350:750]
    # img2 = img[600:750,370:700]
    # img3 = img[450:700,300:750]
    # width_crop, height_crop = img.shape[1],img.shape[0]
    # print(width_crop, height_crop)
    cv2.imwrite(os.path.join(crop_path,"images",file.split("\\")[-1]),img)
    # width_crop,height_crop =  int(x2*width)-int(x1*width), 
    # cv2.imwrite(os.path.join(crop_path,"kim",file.split("\\")[-1]),img1)
    # cv2.imwrite(os.path.join(crop_path,"bactruc",file.split("\\")[-1]),img2)
    # cv2.imshow("Kim",img1)
    # cv2.imshow("BacTruc",img3)
    # cv2.waitKey(0)
    # for txt_file in glob.glob(label_path + "/*.txt"):
#---------------------------------------------------------------------
    # txt_file = os.path.join(label_path,name_img + ".txt")
    # name_file = txt_file.split("\\")[-1]
    # save_file = os.path.join(crop_path,"labels",name_file)
    # lines = []
    # with open(txt_file,"r") as f :
    #     lines = f.readlines()
    # print(lines)
    # for line in lines :
    #     print(line)
    #     classes,x,y,w,h = line.strip().split(" ")
        
    #     x_un,y_un,w_un,h_un = float(x)*width,float(y)*height,float(w)*width,float(h)*height
    #     # print( x_un,y_un,w_un,h_un)
    #     x_un,y_un = x_un - (int(x1*width)-20), y_un - (int(y1*height)+50)
    #     # print()
    #     xn,yn,wn,hn = x_un/width_crop, y_un/height_crop, w_un/width_crop, h_un/height_crop
    #     print( xn,yn,wn,hn)
    #     temp = [int(classes),xn,yn,wn,hn]
    #     print(temp)
    #     if not os.path.exists(save_file) :
    #         with open(save_file,'w') as f :
    #             for data in temp :
    #                 f.write(str(data))
    #                 f.write(' ')
    #             f.write('\n')
    #     else :
    #         with open(save_file,'a') as f :
    #             for data in temp :
    #                 f.write(str(data))
    #                 f.write(' ')
    #             f.write('\n')
#-----------------------------------------------------------------------------------------------
    # break
        # print(xn,yn,wn,hn)
    # break
            


    # cv2.imshow("Crop",img)
    # cv2.waitKey(0)
#-------------------------CROP ALL IMAGES ---------------------------------------

#-------------------------CROP MG ---------------------------------------
# crop_path = "D:\\CHECK\\check"
# for file in glob.glob(root + "/*.bmp"):
#     img = cv2.imread(file)
#     scale_percent = 100 # percent of original size
#     width = int(img.shape[1] * scale_percent / 100)
#     height = int(img.shape[0] * scale_percent / 100)
#     print(width,height)
#     dim = (width, height)
#     img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
#     x1,x2,y1,y2 = 187/640,475/640,58/480,270/480 #Standard
    
#     # img = img[26:427,164:487]
#     img = img[int(y1*height):int(y2*height)+50,int(x1*width):int(x2*width)+40]
#     # cv2.imwrite(os.path.join(crop_path,file.split("\\")[-1]),img)
#     cv2.imshow("Crop",img)
#     cv2.waitKey(0)
#-------------------------CROP MG ---------------------------------------


# variables
# ix = -1
# iy = -1
# drawing = False
# file  = "D:\\raw\A77\CAM1\\ngang\\2022-04-27_03-27-17-5720.bmp"
# img = cv2.imread(file)
# scale_percent = 40 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
# def draw_rectangle_with_drag(event, x, y, flags, param):
      
#     global ix, iy, drawing, img
      
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix = x
#         iy = y            
#         print(ix,iy)
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             cv2.rectangle(img, pt1 =(ix, iy),
#                           pt2 =(x, y),
#                           color =(0, 255, 255),)
      
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         cv2.rectangle(img, pt1 =(ix, iy),
#                       pt2 =(x, y),
#                       color =(0, 255, 255),
#                       thickness =0)
#         print(x,y)
# cv2.namedWindow(winname = "Title of Popup Window")
# cv2.setMouseCallback("Title of Popup Window", 
#                      draw_rectangle_with_drag)
  
# while True:
#     cv2.imshow("Title of Popup Window", img)
    
#     if cv2.waitKey(10) == 'q':
#         break
    

# cv2.destroyAllWindows()
# import the necessary packages
# import argparse
# import cv2
# # initialize the list of reference points and boolean indicating
# # whether cropping is being performed or not
# refPt = []
# cropping = False
# def click_and_crop(event, x, y, flags, param):
# 	# grab references to the global variables
# 	global refPt, cropping
# 	# if the left mouse button was clicked, record the starting
# 	# (x, y) coordinates and indicate that cropping is being
# 	# performed
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		refPt = [(x, y)]
# 		cropping = True
# 	# check to see if the left mouse button was released
# 	elif event == cv2.EVENT_LBUTTONUP:
# 		# record the ending (x, y) coordinates and indicate that
# 		# the cropping operation is finished
# 		refPt.append((x, y))
# 		cropping = False
# 		# draw a rectangle around the region of interest
# 		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
# 		cv2.imshow("image", image)
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())
# # load the image, clone it, and setup the mouse callback function
# image = cv2.imread(args["image"])
# clone = image.copy()
# cv2.namedWindow("image")
# cv2.setMouseCallback("image", click_and_crop)
# # keep looping until the 'q' key is pressed
# while True:
# 	# display the image and wait for a keypress
# 	cv2.imshow("image", image)
# 	key = cv2.waitKey(1) & 0xFF
# 	# if the 'r' key is pressed, reset the cropping region
# 	if key == ord("r"):
# 		image = clone.copy()
# 	# if the 'c' key is pressed, break from the loop
# 	elif key == ord("c"):
# 		break
# # if there are two reference points, then crop the region of interest
# # from teh image and display it
# if len(refPt) == 2:
# 	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
# 	cv2.imshow("ROI", roi)
# 	cv2.waitKey(0)
# # close all open windows
# cv2.destroyAllWindows()