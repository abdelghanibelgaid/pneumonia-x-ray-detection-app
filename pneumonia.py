import streamlit as st
import numpy as np
import functions
from PIL import Image

# Display Pneumonia Web App

# Introduction
st.title("Pneumonia X-Ray Detection")
st.markdown('In this section, we’re presenting the Pneumonia X-Ray Detection Web Application')
    
# Load Image & Predict
img = st.file_uploader(label="Load X-Ray Chest Image", type=['jpeg', 'jpg', 'png'], key="xray")
    
## Preprocessing Image
if img is not None:
p_img = functions.preprocess_image(img)
if st.checkbox('Zoom Image'):
    image = np.array(Image.open(img))
    st.image(image, use_column_width=True)
else:
    st.image(p_img)
    
## Loading model
loading_msg = st.empty()
loading_msg.text("Predicting...")
model = functions.load_model()

## Predicting result
start = time.process_time()
prob, prediction = functions.predict(model, p_img)
loading_msg.text('')

if prediction is True:
    st.markdown(f'The model concluded that the patient has pneumonia with a probability of {round(abs(prob) * 100, 2)}%.')
elif prediction is False:
    st.markdown(f'The model concluded that the patient doesn\'t have pneumonia with a probability of having pneumonia of {100 - round(abs(prob) * 100, 2)}%.')
else:
    st.writemarkdown(f'The model concluded that the patient might have pneumonia, with a probability of having pneumonia of {round(abs(prob) * 100, 2)}%.')
st.text(f'Time taken for prediction is {round(time.process_time() - start, 2)} sec')
    
    # Additional Text
 Dataset Details
st.markdown('## About the Dataset and Testing Strategy')
st.markdown('')
## Model Overview and Metrics
st.markdown('## Model Overview and Metrics')
st.markdown('')
