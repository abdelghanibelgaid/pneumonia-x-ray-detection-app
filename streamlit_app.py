import streamlit as st
import numpy as np
import functions
import time
from PIL import Image

# Models
MODEL_1 = "pneumonia_detection_cnn.h5"

# App Title
st.title("Pneumonia X-Ray Detection")

# Introduction text
st.markdown(unsafe_allow_html=True, body="<p>Welcome to the Pneumonia X-Ray Detection App</p>"
                                         "<p>In this section, we’re presenting the Pneumonia X-Ray Detection Web Application.</p>"
                                         "<p>Upload a Chest X-Ray image and predict whether the patient suffers from pneumonia or not.</p>")

# Img uploader
img = st.file_uploader(label="Load X-Ray Chest Image", type=['jpeg', 'jpg', 'png'], key="xray")

if img is not None:
    # Preprocessing Image
    p_img = functions.preprocess_image(img)
    if st.checkbox('Zoom image'):
        image = np.array(Image.open(img))
        st.image(image, use_column_width=True)
    else:
        st.image(p_img)

    # Loading model
    loading_msg = st.empty()
    loading_msg.text("Predicting...")
    model = functions.load_model(model=MODEL_1)

    # Predicting result
    start = time.process_time()
    prob, prediction = functions.predict(model, p_img)

    loading_msg.text('')

    if prediction is True:
        st.markdown(f'The model concluded that the patient has pneumonia, with a probability of having pneumonia of {round(abs(prob) * 100, 2)}%.')
    elif prediction is False:
        st.markdown(f'The model concluded that the patient doesn\'t have pneumonia with a probability of {100 - round(abs(prob) * 100, 2)}%.')
    else:
        st.markdown(f'The model concluded that the patient might have pneumonia, with a probability of having pneumonia of {round(abs(prob) * 100, 2)}%.')
    st.text(f'Time taken for prediction is {round(time.process_time() - start, 2)} sec')
  
#####################
