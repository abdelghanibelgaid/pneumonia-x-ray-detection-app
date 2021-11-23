import streamlit as st
import numpy as np
from PIL import Image
import about
import functions
import pneumonia
def main():
    menu_list = ['About', 'Pneumonia Detection','Breast Cancer Detection', 'Brain Tumor Detection']
    
    # Display the Sidebar
    st.sidebar.title('Navigation')
    menu_selection = st.sidebar.radio('', menu_list, index=2, key=None)
    
    # Display text in Sidebar
    about.display_sidebar()
    
    # Selecting About Menu
    if menu_selection == 'About':
        about.display_about()
    
    # Selectiong Pneumonia Detection Web App
    if menu_selection == 'Pneumonia Detection':
        display_webapp_1()
    
    # Selectiong Breast Cancer Detection Web App
    if menu_selection == 'Breast Cancer Detection':
        about.display_about()
    
    # Selectiong Brain Tumor Detection Web App
    if menu_selection == 'Brain Tumor Detection':
        about.display_about()

if __name__ == '__main__':
    main()
