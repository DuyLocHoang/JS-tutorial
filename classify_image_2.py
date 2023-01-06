
"""
Phân loại ảnh theo hướng dọc và ngang

"""


import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

data_dir = "D:\\raw\\nut"

batch_size = 1
img_height = 640
img_width = 480

# train_ds = tf.keras.utils.image_dataset_from_directory(
#   data_dir,
#   validation_split=0.2,
#   subset="training",
#   seed=123,
#   image_size=(img_height, img_width),
#   batch_size=batch_size)

# val_ds = tf.keras.utils.image_dataset_from_directory(
#   data_dir,
#   validation_split=0.2,
#   subset="validation",
#   seed=123,
#   image_size=(img_height, img_width),
#   batch_size=batch_size)

# class_names = train_ds.class_names
# print(class_names)

# # import matplotlib.pyplot as plt

# # plt.figure(figsize=(10, 10))
# # for images, labels in train_ds.take(1):
# #   for i in range(9):
# #     ax = plt.subplot(3, 3, i + 1)
# #     plt.imshow(images[i].numpy().astype("uint8"))
# #     plt.title(class_names[labels[i]])
# #     plt.axis("off")

# # for image_batch, labels_batch in train_ds:
# #   print(image_batch.shape)
# #   print(labels_batch.shape)
# #   break


# AUTOTUNE = tf.data.AUTOTUNE

# train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
# val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# normalization_layer = layers.Rescaling(1./255)

# normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
# image_batch, labels_batch = next(iter(normalized_ds))
# first_image = image_batch[0]
# # Notice the pixel values are now in `[0,1]`.
# print(np.min(first_image), np.max(first_image))

# num_classes = len(class_names)

# model = Sequential([
#   layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
#   layers.Conv2D(16, 3, padding='same', activation='relu'),
#   layers.MaxPooling2D(),
#   layers.Conv2D(32, 3, padding='same', activation='relu'),
#   layers.MaxPooling2D(),
#   layers.Conv2D(64, 3, padding='same', activation='relu'),
#   layers.MaxPooling2D(),
#   layers.Flatten(),
#   layers.Dense(128, activation='relu'),
#   layers.Dense(num_classes)
# ])

# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])

# model.summary()


# epochs=5
# history = model.fit(
#   train_ds,
#   validation_data=val_ds,
#   epochs=epochs
# )

# model.save("classify_model_NG_OK_3")


# model.summary()

import os
import shutil
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
model = tf.keras.models.load_model('classify_model_NG_OK_3')
img_height = 640
img_width = 480
class_names = ['NG','OK']
root_path = "D:\\raw\A02\CAM_1\doc\images"
save_path = "D:\\raw\\classify"
# cam = ["CAM_1","CAM_2"]
# a0 = ["A02","A03","A05","A06"]
# for k in a0:
#     root_path_1 = f"D:\\Kha\\raw\\{k}-CONVERT"
#     save_path = f"D:\\Kha\\raw\\{k}"
#     for i in cam :
#         root_path = root_path_1 + f"/{i}"
#         print(root_path)
for img_file in os.listdir(root_path):
    img = tf.keras.utils.load_img(os.path.join(root_path,img_file), target_size=(img_height, img_width))
    # print(img_file)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    if not os.path.exists(os.path.join(save_path,"NG")):
        os.mkdir(os.path.join(save_path,"NG")) 
        # print("ccc")
    if not os.path.exists(os.path.join(save_path,"OK")):
        os.mkdir(os.path.join(save_path,"OK")) 
        # print("ccc")
    if score[1] < 0.8 :
        print(score)
        # print(os.path.join(save_path,"NG",img_file))
        # print(os.path.join(root_path,img_file))
        shutil.copy(os.path.join(root_path,img_file),os.path.join(save_path,"NG",img_file))
    else :
        shutil.copy(os.path.join(root_path,img_file),os.path.join(save_path,"OK",img_file))
        print(score)


#         #     os.replace(os.path.join(root_path,img_file),os.path.join(save_path,"doc",i,img_file))
#         # elif class_names[np.argmax(score)] == "ngang":
#         #     os.replace(os.path.join(root_path,img_file),os.path.join(save_path,"ngang",i,img_file))


# from tensorflow.keras.applications import * #Efficient Net included here
# from tensorflow.keras import models
# from tensorflow.keras import layers
# from keras.preprocessing.image import ImageDataGenerator
# import os
# import shutil
# import pandas as pd
# from sklearn import model_selection
# from tqdm import tqdm
# from tensorflow.keras import optimizers
# import tensorflow as tf
# #Use this to check if the GPU is configured correctly
# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())

# # Options: EfficientNetB0, EfficientNetB1, EfficientNetB2, EfficientNetB3, ... up to  7
# # Higher the number, the more complex the model is. and the larger resolutions it  can handle, but  the more GPU memory it will need
# # loading pretrained conv base model
# #input_shape is (height, width, number of channels) for images
# conv_base = EfficientNetB6(weights="imagenet", include_top=False, input_shape=input_shape)
# model = models.Sequential()
# model.add(conv_base)
# model.add(layers.GlobalMaxPooling2D(name="gap"))
# #avoid overfitting
# model.add(layers.Dropout(dropout_rate=0.2, name="dropout_out"))
# # Set NUMBER_OF_CLASSES to the number of your final predictions.
# model.add(layers.Dense(NUMBER_OF_CLASSES, activation="softmax", name="fc_out"))
# conv_base.trainable = False