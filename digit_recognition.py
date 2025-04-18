# -*- coding: utf-8 -*-

# **Deep Learning Project: Street View Housing Number Digit Recognition**

## **Mount the drive**

Let us start by mounting the Google drive. You can run the below cell to mount the Google drive.
"""

from google.colab import drive
drive.mount('/content/drive')

pip install tensorflow

"""## **Importing the necessary libraries**"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import h5py
import sklearn
import tensorflow as tf
import h5py

#importing Train/Test Split
from sklearn.model_selection import train_test_split

# Keras Sequential Model
from tensorflow.keras.models import Sequential

# Importing all the different layers and optimizers
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization, Activation, LeakyReLU
from tensorflow.keras.optimizers import Adam,SGD

# The below code can be used to ignore the warnings that may occur due to deprecations
import warnings
warnings.filterwarnings("ignore")

#importing classification report and CM

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix

"""**Let us check the version of tensorflow.**"""

print(tf.__version__)

with h5py.File('/content/drive/MyDrive/MIT Python Work/Elective Project/SVHN_single_grey1 (1).h5', 'r') as file:
        # Print the keys to understand the file structure
        print("Keys:", file.keys())

data = h5py.File('/content/drive/MyDrive/MIT Python Work/Elective Project/SVHN_single_grey1 (1).h5', 'r')

X_train = data['X_train'][:]
y_train = data['y_train'][:]
X_test = data['X_test'][:]
y_test = data['y_test'][:]

#Checking the number of images in the training and the testing dataset.
len(X_train), len(X_test),len(y_train), len(y_test)

#visualizing first ten images

plt.figure(figsize = (10, 1))

for i in range(10):

    plt.subplot(1, 10, i+1)

    plt.imshow(X_train[i], cmap = "gray")

    plt.axis('off')

plt.show()
print('Number Labels', (y_train[0:11]))

#Prints size of first image in both training sets
print(X_train[0].shape)
print(y_train[0].shape)

#Normalizing pixel values in the images
X_train = X_train/255
X_test = X_test/255
Y_train = y_train/255
Y_test = y_test/255

#checking shape of images
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

#One-hot encode output
y_train_encoded = tf.keras.utils.to_categorical(y_train)

y_test_encoded = tf.keras.utils.to_categorical(y_test)

# Setting random seed
np.random.seed(42)

import random

random.seed(42)

tf.random.set_seed(42)

#reshaping images to fit an ANN model
X_train_flattened = X_train.reshape(X_train.shape[0], 1024)
X_test_flattened = X_test.reshape(X_test.shape[0], 1024)

def ANN_model1():

# Create the first ANN Model
  model = Sequential()

# Add first layer with 64 neurons to the sequental object
  model.add(Dense(64, input_shape = (1024, ), activation = 'relu'))

# Add second layer with 32 neurons to the sequental object
  model.add(Dense(32, activation = 'relu'))

# Output layer with 10 neurons as it has 10 classes
  model.add(Dense(10, activation = 'softmax'))

  return model

model = ANN_model1()

model.compile(

    loss = 'categorical_crossentropy',

    # Using Adam optimizer with 0.001
    optimizer = tf.keras.optimizers.Adamax(learning_rate = 0.001),

    metrics=['accuracy'])

# Printing the model summary
model.summary()

history_1 = model.fit(

            X_train_flattened, y_train_encoded,

            epochs = 20,

            validation_split = 0.2,

            batch_size = 128,

            shuffle = True,

            verbose = 1
)

plt.plot(history_1.history['accuracy'])

plt.plot(history_1.history['val_accuracy'])

plt.title('Model Accuracy')

plt.ylabel('Accuracy')

plt.xlabel('Epoch')

plt.legend(['Train', 'Validation'], loc = 'upper left')

# Display the plot
plt.show()

# Clearing backend

from tensorflow.keras import backend

backend.clear_session()

# Fixing the seed for random number generators
np.random.seed(42)

import random

random.seed(42)

tf.random.set_seed(42)

def ANN_model2():

# Creat a Sequential Object
  model_2 = Sequential()

# Add first layer with 256 neurons to the sequental object
  model_2.add(Dense(256, input_shape = (1024, ), activation = 'relu'))

# Add second layer with 128 neurons to the sequental object
  model_2.add(Dense(128, activation = 'relu'))

# Adding a Dropout layer with a rate of 0.2
  model_2.add(Dropout(0.2))

# Add third layer with 64 neurons to the sequental object
  model_2.add(Dense(64, activation = 'relu'))

# Add fourth layer with 64 neurons to the sequental object
  model_2.add(Dense(64, activation = 'relu'))

# Add five layer with 64 neurons to the sequental object
  model_2.add(Dense(32, activation = 'relu'))

#Adding Batch Normalization
  model_2.add(BatchNormalization())

# Output layer with 10 neurons as it has 10 classes
  model_2.add(Dense(10, activation = 'softmax'))

  return model

model_2 = ANN_model2()

model_2.compile(

    loss = 'categorical_crossentropy',

    # Using Adam optimizer with 0.0005
    optimizer = tf.keras.optimizers.Adamax(learning_rate = 0.0005),

    metrics=['accuracy'])

# Printing the model summary
model_2.summary()

history_2 = model_2.fit(

            X_train_flattened, y_train_encoded,

            epochs = 30,

            validation_split = 0.2,

            shuffle = True,

            verbose = 1
)

plt.plot(history_2.history['accuracy'])

plt.plot(history_2.history['val_accuracy'])

plt.title('Model Accuracy')

plt.ylabel('Accuracy')

plt.xlabel('Epoch')

plt.legend(['Train', 'Validation'], loc = 'upper left')

# Display the plot
plt.show()

#creates our predictive variable from our X_test
y_pred=model_2.predict(X_test_flattened)

# Obtaining the categorical values from y_test_encoded and y_pred
y_pred_arg=np.argmax(y_pred,axis=1)
y_test_arg=np.argmax(y_test_encoded,axis=1)

# Plotting the Confusion Matrix
confusion_matrix = tf.math.confusion_matrix(y_test_arg,y_pred_arg)
f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(
    confusion_matrix,
    annot=True,
    linewidths=.4,
    fmt="d",
    square=True,
    ax=ax
)
plt.show()

data = h5py.File('/content/drive/MyDrive/MIT Python Work/Elective Project/SVHN_single_grey1 (1).h5', 'r')

X_train = data['X_train'][:]
y_train = data['y_train'][:]
X_test = data['X_test'][:]
y_test = data['y_test'][:]

"""Check the number of images in the training and the testing dataset."""

# Reshaping the dataset to four dimensions for a CNN model

X_train = X_train.reshape(X_train.shape[0], 32, 32, 1)

X_test = X_test.reshape(X_test.shape[0], 32, 32, 1)

#Normalizing pixel values across images
X_train_normalized = X_train/255
X_test_normalized = X_test/255
Y_train_normalized = y_train/255
Y_test_normalized = y_test/255

#One-hot encode the labels in the target variable y_train and y_test.
y_train_encoded = tf.keras.utils.to_categorical(y_train)

y_test_encoded = tf.keras.utils.to_categorical(y_test)

# Fixing the seed for random number generators
np.random.seed(42)

import random

random.seed(42)

tf.random.set_seed(42)

def CNN_model():

# Initialized a sequential model
  model = Sequential()

# Adding the first convolutional layer with 16 filters and the kernel size of 3x3, and 'same' padding
  model.add(Conv2D(filters = 16, kernel_size = (3, 3), padding = "same", input_shape = (32, 32, 1)))

# Adding LeakyRelu activation function with a negative slope of 0.1
  model.add(LeakyReLU(0.1))

# Adding the second convolutional layer with 32 filters and the kernel size of 3x3
  model.add(Conv2D(filters = 32, kernel_size = (3, 3), padding = 'same'))

# Adding LeakyRelu activation function with a negative slope of 0.1
  model.add(LeakyReLU(0.1))

# Adding max pooling to reduce the size of the output of second convolutional layer
  model.add(MaxPooling2D(pool_size = (2, 2)))

# Flattening the 3-d output of the convolutional layer after max pooling to make it ready for creating dense connections
  model.add(Flatten())

# Adding a fully connected dense layer with 32 nodes)
  model.add(Dense(32))

# Adding LeakyRelu activation function with a negative slope of 0.1
  model.add(LeakyReLU(0.1))

# Adding the output layer with 10 neurons and 'softmax' activation function

  model.add(Dense(10, activation = 'softmax')) # Output layer with 10 classes (0-9)

  return model

model = CNN_model()

# Printing the model summary
model.summary()

model.compile(

    loss = 'categorical_crossentropy',

    # Using Adam optimizer with 0.001
    optimizer = tf.keras.optimizers.Adamax(learning_rate = 0.001),

    metrics=['accuracy']
)

history_1 = model.fit(

            X_train_normalized, y_train_encoded,

            epochs = 20,

            validation_split = 0.2,

            shuffle = True,

            verbose = 1
)

"""### **Plot the Training and Validation Accuracies and Write your observations.**"""

plt.plot(history_1.history['accuracy'])

plt.plot(history_1.history['val_accuracy'])

plt.title('Model Accuracy')

plt.ylabel('Accuracy')

plt.xlabel('Epoch')

plt.legend(['Train', 'Validation'], loc = 'upper left')

# Display the plot
plt.show()

# Clearing the backend
from tensorflow.keras import backend

backend.clear_session()

# Fixing the seed for random number generators
np.random.seed(42)

import random

random.seed(42)

tf.random.set_seed(42)

def CNN_model2():
# Initialized a sequential model
  model_2 = Sequential()

# Adding the first convolutional layer with 16 filters and the kernel size of 3x3, and 'same' padding

  model_2.add(Conv2D(filters = 16, kernel_size = (3, 3), padding = "same", input_shape = (32, 32, 1)))

# Adding  first LeakyRelu activation function with a negative slope of 0.1
  model_2.add(LeakyReLU(0.1))

# Adding the second convolutional layer with 32 filters and the kernel size of 3x3
  model_2.add(Conv2D(filters = 32, kernel_size = (3, 3), padding = 'same'))

# Adding second LeakyRelu activation function with a negative slope of 0.1
  model_2.add(LeakyReLU(0.1))

# Adding max pooling to reduce the size of the output of second convolutional layer
  model_2.add(MaxPooling2D(pool_size = (2, 2)))

#Adding Batch Normalization to the second convolutional layer
  model_2.add(BatchNormalization())

# Adding the third convolutional layer with 32 filters and the kernel size of 3x3
  model_2.add(Conv2D(filters = 32, kernel_size = (3, 3), padding = 'same'))

# Adding third LeakyRelu activation function with a negative slope of 0.1
  model_2.add(LeakyReLU(0.1))

# Adding the fourth convolutional layer with 32 filters and the kernel size of 3x3
  model_2.add(Conv2D(filters = 64, kernel_size = (3, 3), padding = 'same'))

# Adding fourth LeakyRelu activation function with a negative slope of 0.1
  model_2.add(LeakyReLU(0.1))

# Adding max pooling to reduce the size of the output of fourth convolutional layer
  model_2.add(MaxPooling2D(pool_size = (2, 2)))

#Adding Batch Normalization to the fourth convolutional layer
  model_2.add(BatchNormalization())

# Flattening the 3-d output of the convolutional layer after max pooling to make it ready for creating dense connections
  model_2.add(Flatten())

# Adding a fully connected dense layer with 32 nodes)
  model_2.add(Dense(32))

# Adding fifth LeakyRelu activation function with a negative slope of 0.1
  model_2.add(LeakyReLU(0.1))

# Adding a Dropout layer with a rate of 0.5
  model_2.add(Dropout(0.5))

# Adding the output layer with 10 neurons and 'softmax' activation function

  model_2.add(Dense(10, activation = 'softmax'))

  return model_2

model_2 = CNN_model2()

# Printing the model summary
model_2.summary()

model_2.compile(

    loss = 'categorical_crossentropy',

    # Using Adam optimizer with 0.001 learning rate
    optimizer = tf.keras.optimizers.Adamax(learning_rate = 0.001),

    metrics=['accuracy']
)

history_2 = model_2.fit(

            X_train_normalized, y_train_encoded,

            epochs = 30,

            validation_split = 0.2,

            shuffle = True,

            verbose = 1
)

"""### **Plot the Training and Validation accuracies and write your observations.**"""

plt.plot(history_2.history['accuracy'])

plt.plot(history_2.history['val_accuracy'])

plt.title('Model Accuracy')

plt.ylabel('Accuracy')

plt.xlabel('Epoch')

plt.legend(['Train', 'Validation'], loc = 'upper left')

# Display the plot
plt.show()

#Predictions on test data using Model 2
y_pred=model_2.predict(X_test)

# Obtaining the categorical values from y_test_encoded and y_pred
y_pred_arg=np.argmax(y_pred,axis=1)
y_test_arg=np.argmax(y_test_encoded,axis=1)

# Plotting the Confusion Matrix using confusion matrix
confusion_matrix = tf.math.confusion_matrix(y_test_arg,y_pred_arg)
f, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(
    confusion_matrix,
    annot=True,
    linewidths=.4,
    fmt="d",
    square=True,
    ax=ax
)
plt.show()
