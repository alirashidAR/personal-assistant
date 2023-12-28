from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai
import os
import streamlit as st
import PIL

genai.configure(api_key=os.getenv("API_KEY"))


# Function to load gemini model and get responses

model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Image Analysis", page_icon="🤖", layout="centered", initial_sidebar_state="expanded")

st.header("Image Analysis")
input = st.text_input("Input: ",key="input" )

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
image =""

if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)



submit = st.button("Submit")

if submit:
    response = get_gemini_response(input,image)

    st.subheader("Response: ") 
    st.write(response)