import streamlit as st
import google.generativeai as genai
from PIL import Image
import docx2txt
import pdfplumber

genai.configure(api_key="AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI")  # Replace with your actual API key


sys_prompt = """Assume you are an error debugger. First, identify the errors, then correct them. Do not answer any other questions."""
gemini_model = genai.GenerativeModel(model_name="models/gemini-2.0-pro-exp-02-05", system_instruction=sys_prompt)
gemini_vision_model = genai.GenerativeModel(model_name="gemini-pro-vision")


st.title("AI Code Reviewer with Image & Document Support")
user_input = st.text_area(label="Enter your query/issue", placeholder="Explain the concept of for loops")
uploaded_file = st.file_uploader("Upload an Image/PDF/DOCX (Optional)", type=["jpg", "jpeg", "pdf", "docx"])


def extract_docx_text(file):
    return docx2txt.process(file)

def extract_pdf_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

response = None

if uploaded_file:
    file_name = uploaded_file.name.lower()

    if file_name.endswith(("jpg", "jpeg", "png")):
        img = Image.open(uploaded_file)
        response = gemini_vision_model.generate_content([img, "extract code from image"])

    elif file_name.endswith(".pdf"):
        pdf_text = extract_pdf_text(uploaded_file)
        response = gemini_model.generate_content([pdf_text, "extract code "])

    elif file_name.endswith(".docx"):
        docx_text = extract_docx_text(uploaded_file)
        response = gemini_model.generate_content([docx_text, "extract code "])

if st.button("Submit"):
    if response:
        st.write(response.text)
    elif user_input:
        response = gemini_model.generate_content(user_input)
        st.write(response.text)
    else:
        st.warning("Please enter a query or upload a file.")