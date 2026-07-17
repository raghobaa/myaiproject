
from PIL import Image
import google.generativeai as ai
import os
import matplotlib.pyplot as plt

image_path = image_path
img = Image.open(image_path)
plt.imshow(img)

model = ai.GenerativeModel(model_name="gemini-1.5-pro")
response=model.generate_content([img,"describe the image"])
print(response.text)

