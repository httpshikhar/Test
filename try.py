import os
import openai
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

client = OpenAI()
#my_secret = "skTUNl4gZBVyAYqIbFlGprT3BlbkFJ03m95oWXvlHMdPxbeRUt"
openai.api_key = os.getenv("OPEN_API_KEY")
response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

print(image_url)
