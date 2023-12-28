from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os
import streamlit as st


genai.configure(api_key=os.getenv("API_KEY"))


#Function to load gemini model and get responses

model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text



# Set up the app

st.set_page_config(page_title="Q&A", page_icon="🤖", layout="centered", initial_sidebar_state="expanded")

st.header("Ask me anything!")

input = st.text_input("Input: ",key="input" )
submit = st.button("Submit")


#When submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("Response: ")
    st.write(response)