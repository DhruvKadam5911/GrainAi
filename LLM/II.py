import google.generativeai as genai
from PIL import Image
from flask import request,jsonify
import os
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the API key
Api_key = os.getenv('API_KEY')


def Image_Define(path, prompt):

   generation_config = {
   "temperature": 0.7,
   "top_p": 1,
   "top_k": 1,
   "max_output_tokens": 300,
   }

   safety_settings = [
   {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_ONLY_HIGH"
   },
   {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_ONLY_HIGH"
   },
   {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_ONLY_HIGH"
   },
   {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_ONLY_HIGH"
   },
   ]

   model = genai.GenerativeModel(
   model_name="gemini-1.5-flash",
   generation_config=generation_config,
   safety_settings=safety_settings)
   genai.configure(api_key=Api_key)

   def eyes(path, prompt):

      print("called Gemini-vision")
      
      image_path = path

      image = Image.open(image_path)

      response = model.generate_content(image)
   
      response = model.generate_content([prompt, image])
      text_response = response.text
      with open("Dataset\Dataset.txt" ,"w") as i:
            info = i.write(text_response)
      return response.text
   
   eyes(f"{path}", f"{prompt}")