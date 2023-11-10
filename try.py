import os
import openai
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import streamlit as st

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

client = OpenAI()
#my_secret = "skTUNl4gZBVyAYqIbFlGprT3BlbkFJ03m95oWXvlHMdPxbeRUt"
openai.api_key = os.getenv("OPEN_API_KEY")

st.sidebar.title("Image Generator")
name = st.sidebar.text_input("Give a prompt for the image", value = "", max_chars = 25)
if st.sidebar.button("Generate"):
    response = client.images.generate(
        model="dall-e-3",
        prompt= name,
        size="1024x1024",
        quality="standard",
        n=1,
    )

image_url = response.data[0].url

st.image(image_url)
