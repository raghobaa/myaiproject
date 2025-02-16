
import google.generativeai as genai

genai.configure(api_key="AIzaSyDv3zVBjzVttDt1lx36M5KO9oopKhG6SDg")

model=genai.GenerativeModel("models/gemini-2.0-pro-exp-02-05",system_instruction="your name is Jai Shree Ram,answer in 2 to 3 lines")
user_prompt=""" genrate 25 questions on ai" with 4options"""
response=model.generate_content(user_prompt)
print(response.text)

