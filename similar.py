

from multiprocessing import reduction
from turtle import forward

import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import shutil
import time
import threading
import torch
#from pytorch_ssim import ssim
#from ignite.metrics import SSIM
from ignite.engine import Engine
from torchmetrics import StructuralSimilarityIndexMeasure as SSIM
from torch.nn import MSELoss

# SETUP HERE
thresh = 0.85
root = "D:\\raw\A68\CAM1\doc\\"
batch_size = 32

move_folder = "D:\\raw\A68\CAM1\\similar\\"

#ssim_loss = pytorch_ssim.SSIM().cuda()

metric = SSIM(data_range=1.0, device='cuda', reduction =None)

loss = MSELoss(size_average =False).cuda()
a= [True, False]
b= ['mean','sum','none']

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

    
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(img1, img2, title, thresh=0.83, txt =''):
    # compute the mean squared error and structural similarity
    # index for the images
    imageA = img1['image'].float().cuda()
    imageB = img2['image'].float().cuda()

    names = img2['name']
    name1 = img1['name']
    idx  = img1['iter']

    # print(imageA.shape)
    # print(imageB.shape)

    #m = mse(imageA, imageB)
    
    state = metric(imageA, imageB).cpu().numpy()
    

    print(txt + ' is not similar', end= '\r')

    for name, conf in zip(names[state>thresh], state[state>thresh]):
        if os.path.exists(name[:-4] + '.json'):
            pass
            #os.remove(name[:-4] + '.json') 

        print('Similar', conf, 'between in {}: '.format(idx), name1, name, 'so we gonna delete')
        if not os.path.exists(move_folder + idx):
            os.mkdir(move_folder + idx)
            # shutil.copy(name1, move_folder + idx +'/origin_' + name1.split('/')[-1])
        shutil.move(name, move_folder + name.split('\\')[-1])   

    #if state.metrics['ssim'] < thresh:
        #print(txt + ' is not similar', end= '\r')
    #    return False 
    
    # setup the figure
    # fig = plt.figure(title)
    # plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    # # show first image
    # ax = fig.add_subplot(1, 2, 1)
    # plt.imshow(imageA, cmap = plt.cm.gray)
    # plt.axis("off")
    # # show the second image
    # ax = fig.add_subplot(1, 2, 2)
    # plt.imshow(imageB, cmap = plt.cm.gray)
    # plt.axis("off")
    # # show the images
    # plt.show()
    #print('Similar between: ', img1['name'], img2['name'], 'so we gonna delete')
    #if os.path.exists(img2['name'][:-4] + '.json'):
    #    os.remove(img2['name'][:-4] + '.json')
    #os.remove(img2['name'])
    pass
    



def get_files(root):
    
    files = [root + x for x in os.listdir(root) if 'bmp' in x or 'png' in x or 'jpg' in x]
    return files

class Read_Compare_MultiThread(object):
    def __init__(self, files):
        self.shape = ""
        self.files = files  
        self.queue = [] 
        self.iter = 0
        self.stop = False
        self.img1 = ''
        self.len_queue = 30

    def read2queue(self):
        print('Is starting thread 1')
        
        i = 0 
        while i < len(self.files): 
            while len(self.queue) < self.len_queue:
                if i == self.iter:
                    i+= 1
                #print('read image', i, len(self.queue), end ='\r')
                while i < len(self.files) and not os.path.exists(self.files[i]) :
                    i+= 1
                if i >= len(self.files):
                    self.stop = True
                    return
                img = cv2.imread(self.files[i], 0)
            
                
                img = cv2.resize(img, self.shape)/255 
                img = np.asarray([[img]])
                img = {'image': torch.tensor(img), 'name': self.files[i], 'iter': i}
                self.queue.append(img) 
                i+= 1
        self.stop = True
        return
    def th_compare(self):
        print('Is starting thread 2')
        while True:
            if len(self.queue) > 0:
                img2 = self.queue.pop(0)
                compare_images(self.img1, img2, ".", 0.83, txt= str(self.iter) + ' ' + str(img2['iter']))
                # print(self.iter, img2['iter'], end=' ')
                if img2['iter'] >= len(files):
                    print('finish')
                    return 
            else:
                if self.stop:
                    return
                print('sleep to wait. len q =', len(self.queue))
                time.sleep(1)
                

        print('exit thread compare')
    def forward(self):
        for self.iter in range(len(self.files)):
            fname = self.files[self.iter]
            if not os.path.exists(fname):
                continue
            img1 = cv2.imread(fname, 0) 
            self.shape = img1.shape[::-1]
            img1 = np.asarray([[img1]])/255
            self.img1 = {'image': torch.tensor(img1), 'name': fname, 'iter': self.iter}

            t1 = threading.Thread(target= self.read2queue)
            t1.start()
            self.stop = False
            threads = []
            for i in range(4):
                t = threading.Thread(target= self.th_compare)
                threads.append(t)
                t.start()

            
            
            
            t1.join()

            for t in threads:
                t.join()
                print('Killed!')
            
            


files = get_files(root)
print(len(files))
myclass = Read_Compare_MultiThread(files)
#myclass.forward()

# print("k")

def read2queue(shape, files, iter):
    print('Is starting thread 1')
    global q
    i = 0
    while i < len(files): 
        while len(q) < 15 and i < len(files):
            if i == iter:
                i+= 1
            print('read image', i, len(q))
            img = cv2.imread(files[i], 0)
            img = cv2.resize(img, shape)
            img = {'image': img, 'name': files[i], 'iter': i}
            q.append(img) 
            i+= 1
    return

def th_compare(img1):
    print('Is starting thread 2')
    while True:
        if len(q) > 0:
            img2 = q.pop(0)
            #compare_images(img1, img2, ".", 0.83)
            print(img1['iter'], img2['iter'], end='\r')
            if img2['iter'] >= len(files):
                print('finish')
                return 
        else:
            print('sleep to wait. len q =', len(q))
            time.sleep(1)
            

    print('exit thread compare')

for iter in range(len(files)):
    print(files[iter])
    if not os.path.exists(files[iter]):
        print("c")
        continue
    print("oke")
    img1 =  cv2.imread(files[iter], 0)/255
    print(img1)
    shape = img1.shape[::-1]
    img1 = np.asarray( [[img1]]*batch_size )
    #print(img1.shape)
    
    
    
    img1 = {'image': torch.tensor(img1), 'name': files[iter], 'iter': str(iter)}
    
    i = 0 
    txt = str(iter) + ' vs 0'
    queue_img = [] 
    queue_name = []
    while i < len(files):
        if i == iter:
            i+= 1
            continue

        if not os.path.exists(files[i]):
            i+=1
            continue
            
        if len(queue_img) < batch_size:
            
            


            img2 = cv2.imread(files[i], 0)/255
            img2 = cv2.resize(img2, shape)

            queue_img.append( [img2] )
            queue_name.append( files[i] )  
            

        else:
            txt = txt +  '->' + str(i-1)
            queue_img = torch.tensor(np.array(queue_img))

            img2 = {'image': queue_img, 'name': np.asarray(queue_name)}

            compare_images(img1, img2, "", thresh=thresh,  txt = txt)  

            queue_img = []
            queue_name = []
            txt = str(iter) + ' vs ' + str(i)
    
        i+= 1

    if len(queue_img) !=0:
        txt = txt +  '->' + str(i-1)
        queue_img = torch.tensor(np.array(queue_img))
        img2 = {'image': queue_img, 'name': np.asarray(queue_name)}

        img1['image'] = img1['image'][:len(img2['image'])]

        compare_images(img1, img2, "", thresh=thresh,  txt = txt)  
        
    


         

         
        
    

    
    
    
    
        
