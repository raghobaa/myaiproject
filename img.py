
from PIL import Image
import google.generativeai as ai
import os
import matplotlib.pyplot as plt

image_path = "/Users/raghav/Desktop/untitled folder/pexels-anjana-c-169994-674010.jpg" 
img = Image.open(image_path)
plt.imshow(img)
ai.configure(api_key="AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI")  
model = ai.GenerativeModel(model_name="gemini-1.5-pro")
response=model.generate_content([img,"describe the image"])
print(response.text)

