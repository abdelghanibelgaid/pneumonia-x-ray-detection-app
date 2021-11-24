import numpy as np
import streamlit as st
import tensorflow as tf
import tensorflow.keras as keras
from PIL import Image

MODEL = "pneumonia_detection_cnn.h5"

@st.cache(allow_output_mutation=True)
def load_model():
    print("loading model")
    model = keras.models.load_model(f"{MODEL}", compile=True)
    return model

def preprocess_image(img):
    image = Image.open(img).convert("RGB")
    p_img = image.resize((150, 150))
    return np.array(p_img) / 255

def predict(model, img):
    prob = model.predict(np.reshape(img, [-1, 150, 150, 1]))
    prob = prob.sum()/len(prob)
    if prob >= 0.60:
        prediction = True
    elif 0.40 < prob < 0.60:
        prediction = None
    else:
        prediction = False
    return prob, prediction
