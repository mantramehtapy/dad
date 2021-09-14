import streamlit as st
import cv2
import numpy as np
filename = "/home/mantra/Desktop/Dev/dadproject/GitHub-logo.jpg"
img = cv2.imread(filename, 1)
image = np.array([img])

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 48px;">Model Created by Rajiv Mehta</p>'
st.markdown(new_title, unsafe_allow_html=True)

option1 = st.text_input("input","enter your choice")

option2 = st.text_input("input 2","enter your input")

if st.button('test'):

    """idk put some ccode in here"""



from PIL import Image
img = Image.open("/home/mantra/Desktop/Dev/dadproject/iron_man_discord_icon.gif")
st.image(img,width=100)  
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 20px;">frontend Created by Mantra Mehta</p>'
st.markdown(new_title, unsafe_allow_html=True)