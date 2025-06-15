import streamlit as st 

st.set_page_config(page_title='Home',initial_sidebar_state='auto')

st.header('Wagon-R Resale Price Analysis')

text = """ 
This application : 
1. Has almost 1500+ data points (Wagon-R historical resale prices) collected from renowned classifieds website.
2. These datapoints are posted on website within year back from 16 june 2025.
3. It lets you filter out data based on your requirements.
5. Then fetches result for filtered out data.
5. Output contains - 
    \n\t5.1 Total entries for filtered data
    \n\t5.2 Mean resale price for filtered data
    \n\t5.3 Minimum resale price for filtered data
    \n\t5.4 Maximum resale price for filtered data
    \n\t5.5 Barplot of price counts 
"""

st.write(text)

if st.button(label='Application >>'):
    st.switch_page(page='pages/1_app.py')