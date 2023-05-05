### IMPORT UTILITIES LIBRARIES ###
import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import pickle
import boto3

### SET CONNECTION TO S3 BUCKET ###
s3_client = boto3.client('s3')
bucketName = "cloud-computing-model-bucket" 

### DOWNLOAD CIFAR10 DATASET ###
cifar100 = tf.keras.datasets.cifar100

### DIVIDE DATASET IN TRAINING AND VALIDATION ###
(x_train, y_train), (x_val, y_val) = cifar100.load_data()

### CHECK SIZES ###
print(x_train.shape, y_train.shape, x_val.shape, y_val.shape)

### CHECK IF GPU IS AVAILABLE ###
### if available tensorflow will use it automatically ###
#print('GPU name: ', tf.config.experimental.list_physical_devices('GPU'))

### CREATE THE TENSOR TO BE USED IN THE MODEL ###
y_train = tf.one_hot(y_train, 
                     depth=y_train.max()+1,
                     dtype=tf.float64)

y_val = tf.one_hot(y_val,
                   depth=y_val.max()+1,
                   dtype=tf.float64)

y_train = tf.squeeze(y_train)
y_val = tf.squeeze(y_val)

### CREATE THE MODEL ###
model = tf.keras.models.Sequential([
  layers.Conv2D(16,(3,3),activation='relu',
                input_shape=(32,32,3),padding='same'),
  layers.Conv2D(32,(3,3),activation='relu',
                input_shape=(32,32,3),padding='same'),
  layers.Conv2D(64,(3,3),activation='relu',
                input_shape=(32,32,3),padding='same'),
  layers.MaxPooling2D(2,2),
  layers.Conv2D(128,(3,3),activation='relu',
                input_shape=(32,32,3),padding='same'),
  
  layers.Flatten(),
  layers.Dense(256, activation='relu'),
  layers.BatchNormalization(),
  layers.Dense(256, activation='relu'),
  layers.Dropout(0.3),
  layers.BatchNormalization(),
  layers.Dense(100, activation='softmax')
])

### COMPILE THE MODEL ###
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    optimizer='adam',
    metrics=['AUC', 'accuracy']
)

### TRAIN THE MODEL ###
### notice that a log containing the eta and the metrics measured will be produced in real time ###
hist = model.fit(x_train, y_train,
                 epochs=5,
                 batch_size=64,
                 verbose=1,
                 validation_data=(x_val, y_val))

### CREATE A NEW MODEL STARTING FROM THE PREVIOUS ONE ###
temp = model.get_layer('conv2d_3')
last_output = temp.output
last_output.shape

x = layers.Flatten()(last_output)

x = layers.Dense(256, activation='relu')(x)
x = layers.BatchNormalization()(x)

x = layers.Dense(256, activation='relu')(x)
x = layers.Dropout(0.3)(x)
x = layers.BatchNormalization()(x)

output = layers.Dense(10, activation='softmax')(x)

model_new = keras.Model(model.input, output)

### COMPILE THE NEW MODEL ###
model_new.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['AUC', 'accuracy']
)

### DOWNLOAD THE CIFAR10 DATASET AND DIVIDE IT IN TRAIN AND TEST ###
### also check the size of train and test ###
cifar10 = tf.keras.datasets.cifar10

(x_train, y_train), (x_val, y_val) = cifar10.load_data()
print(x_train.shape, y_train.shape, x_val.shape, y_val.shape)

### CREATE THE TENSOR TO BE USED IN THE MODEL ###
y_train = tf.one_hot(y_train, 
                     depth=10,
                     dtype=tf.float64)

y_val = tf.one_hot(y_val,
                   depth=10,
                   dtype=tf.float64)

y_train = tf.squeeze(y_train)
y_val = tf.squeeze(y_val)

### TRAIN THE MODEL ###
### notice that a log containing the eta and the metrics measured will be produced in real time ###
history = model_new.fit(x_train, y_train,
                 epochs=10,
                 batch_size=64,
                 verbose=1,
                 validation_data=(x_val, y_val))

### SAVE THE MODEL IN A PICKLE FILE ###
fileName = 'finalized_model.sav'
pickle.dump(model_new, open(fileName, 'wb'))

### SAVE THE TRAINED MODEL TO S3 BUCKET ###
s3_client.upload_file(fileName, bucketName, fileName)