# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob
import os
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    # print(m)
    # print(m)
    return m,s
    # print(s)
	# setup the figure
    # fig = plt.figure(figsize=(15,15))
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

# load the images -- the original, the original + contrast,
# # and the original + photoshop
# original = cv2.imread("D:\\raw\A02\CAM_1\doc\images\\2022-06-02_07-01-26-6040.bmp",0)
# contrast = cv2.imread("D:\\raw\A02\CAM_1\doc\images\\2022-06-03_06-57-50-5070.bmp",0)
# # shopped = cv2.imread("D:\\raw\A02\CAM_1\doc\images\\2022-06-02_07-01-29-5340.bmp")
# # convert the images to grayscale
# # original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
# # contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
# # shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)
# compare_images(original,contrast)
# fig = plt.figure(figsize=(15,15))
# # plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
# # show first image
# ax = fig.add_subplot(1, 2, 1)
# plt.imshow(original, cmap = plt.cm.gray)
# plt.axis("off")
# # show the second image
# ax = fig.add_subplot(1, 2, 2)
# plt.imshow(contrast, cmap = plt.cm.gray)
# plt.axis("off")
# # show the images
# plt.show()
# # initialize the figure

# # fig = plt.figure("Images")
# # images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)
# # # loop over the images

# # for (i, (name, image)) in enumerate(images):
# # 	# show the image
# # 	ax = fig.add_subplot(1, 3, i + 1)
# # 	ax.set_title(name)
# # 	plt.imshow(image, cmap = plt.cm.gray)
# # 	plt.axis("off")
# # # show the figure

# plt.show()
# compare the images
root = "D:\\raw\A76\CAM2\\ngang"
save_path = "D:\\raw\A76\CAM2\\ngang\same_img"

img = []
for img_path in glob.glob(root + "/*.bmp"):
    img.append(img_path)
same_img = []
for i in range(1,len(img)-1):
    m,s = compare_images(cv2.imread(img[i],0),cv2.imread(img[i+1],0))
    print(s)
    if s > 0.85 :
        same_img.append(img[i+1])



if not os.path.exists(save_path):
    os.makedirs(save_path)

for img in same_img :
    os.replace(img,os.path.join(save_path,img.split('\\')[-1].split(".")[0]+ ".bmp"))
        # fig = plt.figure("Images")
        # images = ("Original", img[i]), ("Contrast", img[i+1])
#    
# 
#      # loop over the images

# for i in range(len(img)):
#     for j in range(i+1,100):
#         m = compare_images(cv2.imread(img[i],0),cv2.imread(img[j],0))
#         # print(s)
#         if m < 200 :
#             same_img.append(img[i+1])
#             fig = plt.figure(figsize=(15,15))
#             # plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
#             # show first image
#             ax = fig.add_subplot(1, 2, 1)
#             plt.imshow(cv2.imread(img[i],0), cmap = plt.cm.gray)
#             plt.axis("off")
#             # show the second image
#             ax = fig.add_subplot(1, 2, 2)
#             plt.imshow(cv2.imread(img[j],0), cmap = plt.cm.gray)
#             plt.axis("off")
#             # show the images
#             plt.show()
#     print("---------------------------------------")



            # loop over the images

        # fig = plt.figure(figsize=(15,15))
        # plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
        # # show first image
        # ax = fig.add_subplot(1, 2, 1)
        # plt.imshow(img[i], cmap = plt.cm.gray)
        # plt.axis("off")
        # # show the second image
        # ax = fig.add_subplot(1, 2, 2)
        # plt.imshow(img[i+1], cmap = plt.cm.gray)
        # plt.axis("off")
        # # show the images
        # plt.show()

# for i in range(len(img)):
#     for j in range(i,len(img)):
#         compare_images(img[i],img[j])
#     break

