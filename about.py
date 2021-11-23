import streamlit as st

# Display About
def display_about():
    # st.markdown('![Rhazes.io Logo](github_link)')
    
    st.markdown('## Project Description')
    st.markdown('Rhazes.io is an AI platform enabling medical practitioners to review and process medical images faster, more accurately, and more cost-efficiently. We\'re employing deep learning models to detect and classify diseases, perform advanced medical imaging diagnoses, and generate medical reports. This web application serves as a minimum viable product (MVP) to showcase and pre-validate our products. It\'s also used to attract talents, talk to potential users, and raise seed funds. \n Artificial intelligence (AI) has been applied in medical image classification via deep learning algorithms trained on massive amounts of supervised data. These models extend complex image analysis beyond human capabilities and help automatically detect and classify structural patterns. It also optimizes the processing time and quality of image-based workflows. These models are improving rapidly and have moved into clinical trials. Fortunately for this application, there are plenty of existing datasets. Even though these datasets only contain a couple of thousands of images from patient cases, we use transfer learning to improve performance in the small data regime. In order to improve our model\'s accuracy, multiple input datasets, transfer learning, and pre-trained models were used, and a stacking ensembled method was employed for each final classification. We already achieved 80%~90% accuracy on the unseeing testing dataset. More improvements are undergoing on these models.')
    
    st.markdown('## Our Products')
    st.markdown('Classifier: description')
    st.markdown('![Rhazes.io Logo](github_link)')

    st.markdown('## Milestones')
    st.markdown('')
    
    st.markdown('## Survey')
    st.markdown('As mentioned above, the purpose of this MVP is to present our core product. Thus it doesn’t include the signing up section, dashboard, and other web application sections. Additional features will be added to our core product, such as generating a downloadable report that sums up the diagnosis. We want to know (i) what do you think about this product and what do you like about it, (ii) what features you’re would you like to have in the basic and best solution, (iii) do you think that MDs are willing to purchase this kind of service, (iv) what would make you recommend it.')
    
    st.markdown('## Afterword')
    st.markdown('P.S. The current classifiers presented on this MVP contain only one model with little to no complex feature engineering and hyperparameter tuning to reduce the computation requirements, the runtime and avoid additional steps that don\'t meet our initial attention, which is building an MVP asap. Even some models achieved +90% on the testing dataset, they might raise some accuracy failures. Consequently, these models should only be used as a showcase, and not to conduct real-world medical diagnoses. There are limitations to be considered, such as model interpretability and learning from limited labeled data, which are the primary limitations we’re addressing in this project.')

# Display Sidebar
def display_sidebar():
    st.sidebar.markdown('---')
    
    st.sidebar.title('Sponsor us')
    st.sidebar.info('Our project relies on our own personal funding. You can support us by \
    purchasing [extra cloud storage](https://paypal.me/abdelghanibelgaid). \
    Your support will allow us to reach the next milestone. We sincerely thank all of our supporters!')
    
    st.sidebar.title('Join us')
    st.sidebar.info('We’re constantly looking for devoted talents who are excited about this project. \
    We are open to a wide variety of talents from all backgrounds, levels, and experiences. \
    Feel free to reach out and let us know a little bit about yourself.')
    
    st.sidebar.title('Contact us')
    st.sidebar.info('This app is maintained by Rhazes.io. If you want to know more about us or just \
    share with us your experience, e-mail us at abdelghani.belgaid[at]gmail.com, and we\'ll be sure \
    to get back to you as soon as we can!')
