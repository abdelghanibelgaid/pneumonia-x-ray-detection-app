import streamlit as st
import numpy as np
import functions
from PIL import Image

# App Title
st.title("Pneumonia X-Ray Detection App")

# Introduction text
st.markdown(unsafe_allow_html=True, body="<p>Welcome to Pneumonia X-Ray Detection App</p>"
                                         "<p>With this app, you can upload a Chest X-Ray image and predict if the patient "
                                         "from that image suffers pneumonia or not.</p>"
                                         "<p>The model used is a Convolutional Neural Network (CNN) and in this "
                                         "moment has a test accuracy of "
                                         "<strong>+90%.</strong></p>")

# Img uploader
img = st.file_uploader(label="Load X-Ray Chest image", type=['jpeg', 'jpg', 'png'], key="xray")

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
    model = functions.load_model()

    # Predicting result
    prob, prediction = functions.predict(model, p_img)

    loading_msg.text('')

    if prediction:
        st.markdown(unsafe_allow_html=True, body="<span style='color:red; font-size: 35px'><strong><h3>Pneumonia!</h3></strong></span>")
    else:
        st.markdown(unsafe_allow_html=True, body="<span style='color:green; font-size: 35px'><strong><h3>Healthy!</h3></strong></span>")

    st.text(f"Probability of pneumonia is {round(abs(prob[0]) * 100, 2)}%")
