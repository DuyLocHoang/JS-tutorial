import cv2
import glob
import os

def crop_image(img):
    original_crop = img.copy()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(img,125,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    arr = []
    for c in contours :
        rect = cv2.boundingRect(c)
        x,y,w,h = rect 
        cv2.rectangle(original_crop,(x,y),(x+w,y+h),(0,255,0),1)
        # cv2.imshow("Crop image",original_crop)
        if  600000 < w*h < 900000:
           arr.append([x,y,w,h])
    print(arr)
    if len(arr) > 1 :
        # print(arr)
        x,y,w,h = arr[0]
        # print(arr)
        # for x,y,w,h in arr :      
            # cv2.rectangle(original_crop,(x,y),(x+w,y+h),(255,0,0),1)
        img = img[y:y+h,x:x+w]
    elif len(arr) == 1 :
            x,y,w,h = arr[0]
            img = img[y:y+h,x:x+w]
    cv2.imwrite("D:\\crop-img\\a.bmp",img)
    return original_crop


if __name__ == "__main__":
    crop_path = "D:\\raw\\classify\\doc\\test\\NG"

    for i in glob.glob(crop_path + "/*.bmp"):
        img = cv2.imread(i)
        img = crop_image(img)
        cv2.imshow("IMG",img)
        cv2.waitKey(0)
        # cv2.imwrite(i,img)
