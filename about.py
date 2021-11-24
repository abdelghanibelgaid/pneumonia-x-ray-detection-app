import streamlit as st

# Display About
def display_about():
    st.image('![Rhazes.io Logo](https://raw.githubusercontent.com/abdelghanibelgaid/pneumonia-x-ray-detection-app/master/Rhazes.png)', width=80)
    
    st.markdown('## Project Description')
    st.markdown('')
    
    st.markdown('## Our Products')
    st.markdown('Classifier: description')
    st.markdown('![Rhazes.io Logo](github_link)')

    st.markdown('## Milestones')
    st.markdown('')
    
    st.markdown('## Survey')
    st.markdown('')
    
    st.markdown('## Afterword')
    st.markdown('')
    
# Display Sidebar
def display_sidebar():
    st.sidebar.markdown('---')
    
    st.sidebar.title('Sponsor us')
    st.sidebar.info('Our project relies on our own personal funding. You can support us via \
    [Paypal](https://paypal.me/abdelghanibelgaid). \
    Your support will allow us to reach the next milestone. We sincerely thank all of our supporters!')
    
    st.sidebar.title('Join us')
    st.sidebar.info('We’re constantly looking for devoted talents who are excited about this project. \
    We are open to a wide variety of talents from all backgrounds, levels, and experiences. \
    Feel free to reach out and let us know a little bit about yourself.')
    
    st.sidebar.title('Contact us')
    st.sidebar.info('This app is maintained by Rhazes.io. If you want to know more about us or just \
    share with us your experience, e-mail us at abdelghani.belgaid[at]gmail.com, and we\'ll be sure \
    to get back to you as soon as we can!')
