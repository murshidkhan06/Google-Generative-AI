##FalconSpark
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')
image = Image.open("Image.jpeg")
input_prompt = "What so funny about this image ?"
print(model.generate_content([input_prompt, image]).text)