import streamlit as st
import numpy as np
from PIL import Image
import time
import about
import functions

st.set_page_config(page_title='Rhazes.io',
                   page_icon='https://raw.githubusercontent.com/abdelghanibelgaid/pneumonia-x-ray-detection-app/master/Rhazes.png',
                   initial_sidebar_state='expanded')

menu_list = ['About', 'Pneumonia Detection','Breast Cancer Detection', 'Brain Tumor Detection']
    
# Display the Sidebar
st.sidebar.title('Navigation')
menu_selection = st.sidebar.radio('Go to', menu_list, index=2, key=None)
    
# Display text in Sidebar
about.display_sidebar()
    
# Selecting About Menu
if menu_selection == 'About':
    about.display_about()
    
# Selectiong Pneumonia Detection Web App
if menu_selection == 'Pneumonia Detection':
    st.title("Pneumonia X-Ray Detection App")
    # Introduction text
    st.markdown(unsafe_allow_html=True, body="<p>Welcome to the Pneumonia X-Ray Detection App</p>"
                                         "<p>Upload a Chest X-Ray image and predict whether the patient "
                                         "suffers pneumonia or not.</p>"
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
        MODEL_1 = "pneumonia_detection_cnn.h5"
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
        
    # Additional Text
    ## Dataset Details
    st.markdown('### About the Dataset and Testing Strategy')
    st.markdown('text')
    ## Model Overview and Metrics
    st.markdown('### Model Overview and Metrics')
    st.markdown('text') 
    
# Selectiong Breast Cancer Detection Web App
if menu_selection == 'Breast Cancer Detection':
    about.display_about()
    
# Selectiong Brain Tumor Detection Web App
if menu_selection == 'Brain Tumor Detection':
    about.display_about()
