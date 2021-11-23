import streamlit as st
import numpy as np
import functions
from PIL import Image

# Display Pneumonia Web App
def display_webapp_1():
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
    ## Dataset Details
    st.markdown('## About the Dataset and Testing Strategy')
    st.markdown('We’re using a dataset of chest X-ray images of pediatric pneumonia with a total of  5,232 labeled chest X-ray images, including 3,883 characterized as depicting pneumonia (2,538 bacterial and 1,345 viral) and 1,349 normal, from a total of 5,856 patients to train the model. The model was then tested with 234 normal images and 390 pneumonia images (242 bacterial and 148 viral) from 624 patients. The dataset is under the CC BY 4.0 license that was collected as part of patients’ routine clinical care.')
    ## Model Overview and Metrics
    st.markdown('## Model Overview and Metrics')
    st.markdown('The model used is a Convolutional Neural Network (CNN), which is a specialized neural network for processing data that has an input shape like a 2D matrix like images. The model accuracy on the unseeing testing dataset is about 91.5%. The resulting high-accuracy model suggests that this model has the potential to effectively learn from increasingly complicated images with a high degree of generalization using a relatively small repository of data.')
