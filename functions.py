import os
import numpy as np
import keras
from tensorflow.keras.models import load_model
import streamlit as st
from keras import layers, models, optimizers
from PIL import Image

MODEL = "pneumonia_detection_cnn.h5"
img_size = 150

def predict(image1): 
    image = load_img(image1, target_size=(150, 150))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    #image = preprocess_input(image)
    # predict the probability across all output classes
    yhat = model.predict(image)
    if yhat > 0.5:
        prediction = True
    else:
        prediction = False
    return prob, prediction
