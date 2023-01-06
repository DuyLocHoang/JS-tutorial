
"""
Phân loại ảnh theo hướng dọc và ngang

"""


import matplotlib.pyplot as plt
import numpy as np
# import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

# data_dir = "C:\\Users\\vnmuser\\Desktop\\DUYLOC\\lib\\classify_image"

# batch_size = 1
# img_height = 640
# img_width = 480

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


# epochs=10
# history = model.fit(
#   train_ds,
#   validation_data=val_ds,
#   epochs=epochs
# )

# model.save("classify_model")


# new_model.summary()

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
model = tf.keras.models.load_model('..\\classify_image')
img_height = 640
img_width = 480
class_names = ['doc','ngang']
root_path = "D:\\raw\A77\CAM1\\doc"
save_path = "D:\\raw\A77\doc-2"

if not os.path.exists(save_path):
    os.makedirs(save_path)

for img_file in os.listdir(root_path):
    img = tf.keras.utils.load_img(
        os.path.join(root_path,img_file), target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    if class_names[np.argmax(score)] == "doc":
        os.replace(os.path.join(root_path,img_file),os.path.join(save_path,img_file))