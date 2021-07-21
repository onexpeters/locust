import ee 
import folium
import streamlit as st
import geehydro
import numpy as np
import time
from datetime import datetime as dt
from IPython.display import Image
from streamlit_folium import folium_static
import base64
st.title('DESERT LOCUST SIGHTING SYSTEM')
col1, col2 = st.beta_columns(2)
with col1:
    col1.write('Help us track Desert Locust in Kenya. Have you seen Desert locust where you are. A photo or video will be great!.')
main_bg = "ISIOLO.png"
main_bg_ext = "png"
st.markdown("""
<style>
body {
    color: ##fc0fc0;
    background-color: #7ce68d ;
}
</style>
    """, unsafe_allow_html=True)
side_bg = "ISIOLO.png"
side_bg_ext = "png"
option = st.selectbox('Select the county where you have spotted the DESERT Locust from?',('Mombasa', 'Kwale', 'Isiolo','Taita Taveta','Meru'))
with col2:
    col2.text_input("Please enter the specific location name in the selected county")
    col2.selectbox('Have You noticed their color',('Brown', 'Yellow', 'Pink/Red','Black/Yellow','Yellow/Brown'))
user_input2= st.text_input("Please your name")
user_input3= st.text_input("Enter your contacts")
st.markdown('<style>h1{color: green;}</style>', unsafe_allow_html=True)
start_date=st.date_input('Please select the date of sighting')
option2 = st.selectbox('What is the state of the locusts during the time of sighting?',('Moving', 'perched '))
fp = st.file_uploader("Upload any photo of the Desert Locust if possible")
st.button('Upload')
st.button('Submit')
    
