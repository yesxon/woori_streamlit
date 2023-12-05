import streamlit as st
import pandas as pd
from PIL import Image
#입력

photo_list = ['팝캣','사이버펑크','좋은아침']
img_list = ['https://i.imgur.com/RpnRQ19.jpg', 
            'https://i.imgur.com/j2lNHNl.jpg',
            'https://i.imgur.com/sGv1eeA.jpeg']

data = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
search = st.text_input("Enter the text")

for pho_ in photo_list:
    if search in pho_:
        img_idx = photo_list.index(pho_)

if search != '':
    st.image(img_list[img_idx])
    
#출력
st.button("Click me")

st.download_button(
    label="Download data as CSV",
    data='안년하세요',
    file_name='app_df.csv',
    mime='text/csv',
)

button_result = st.button('Hit me')
if button_result == True:
    st.data_editor(data)

#st.link_button("Go to gallery", url)

a = st.checkbox("I agree")
if a == True:
    st.data_editor(data)

st.toggle("Enable")
st.radio("Pick one", ["cats", "dogs"])
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.camera_input("Take a picture")
st.color_picker("Pick a color")