# Import necessary libraries
import streamlit as st
import os
from PIL import Image

# Configure the generative AI model
import google.generativeai as genai

# Set the API key directly
API_KEY = "AIzaSyArF2Fp_p07sadEH0x12nnM5frc6kEPdZo"
genai.configure(api_key=API_KEY)

# Function to load OpenAI model and get responses
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Fitness Fusion")

# Header
st.header("Snap Track")
# Default prompt
default_prompt = "Detect the food item and give me the calories and macros of the food according to the quantity of the food which is detected in the image"

# Input prompt field with default value
input_text = st.text_input("Input Prompt: ", value=default_prompt, key="input")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", width=300)  # Adjust the width here

# Submit button
submit = st.button("Tell me about the image")

# If submit button is clicked
if submit:
    if image is not None:
        response = get_gemini_response(input_text, image)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload an image before submitting.")
