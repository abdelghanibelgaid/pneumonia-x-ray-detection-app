import os
import numpy as np
import keras
#import cv2
import streamlit as st
from keras import layers, models, optimizers
from PIL import Image

MODEL = "pneumonia_detection_cnn.h5"
img_size = 150

@st.cache(allow_output_mutation=True)
def load_model():
    print("loading model")
    model = keras.models.load_model(f"{MODEL}", compile=True)
    return model

def preprocess_image(img):
    image = Image.open(img).convert("RGB")
    img_arr = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    resized_arr = cv2.resize(img_arr, (img_size, img_size))
    p_img = resized_arr.resize((150, 150))
    return np.array(p_img) / 255.0

def predict(model, img):
    prob = model.predict(np.reshape(img, [-1, 150, 150, 1]))
    if prob > 0.5:
        prediction = True
    else:
        prediction = False
    return prob, prediction
