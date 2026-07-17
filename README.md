# AI Code Corrector & Reviewer

An intelligent Streamlit web application that uses Google's Gemini AI to review, debug, and correct code. Submit code directly or upload images, PDFs, or Word documents containing code for AI-powered error detection and correction.

## Features

- 🤖 **AI Code Debugging** - Uses Gemini 2.0 API to identify and correct code errors
- 📸 **Image Support** - Extract and analyze code from image uploads (JPG, JPEG, PNG)
- 📄 **PDF Support** - Process code from PDF documents
- 📝 **Word Document Support** - Extract code from DOCX files
- 💬 **Direct Input** - Paste code directly or type your query
- 🎯 **Error-Focused** - System prompt configured specifically for debugging and error correction

## Tech Stack

- **Framework:** Streamlit
- **AI Model:** Google Generative AI (Gemini 2.0)
- **Libraries:**
  - `google-generativeai` - Gemini API integration
  - `streamlit` - Web UI framework
  - `Pillow (PIL)` - Image processing
  - `pdfplumber` - PDF text extraction
  - `docx2txt` - Word document parsing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/raghobaa/myaiproject.git
cd myaiproject
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Get your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

2. Open `new.py` and add your API key:
```python
GEMINI_API = "your_actual_api_key_here"
```

## Usage

Run the application:
```bash
streamlit run new.py
```

The app will open in your browser at `http://localhost:8501`

### How to Use:

1. **Option 1 - Direct Code Input:**
   - Enter your code or error description in the text area
   - Click "Submit" to get AI feedback and corrections

2. **Option 2 - Upload Files:**
   - Upload an image (JPG/JPEG/PNG) with code
   - Or upload a PDF/DOCX document containing code
   - Click "Submit" to extract and analyze the code

## Project Structure

```
myaiproject/
├── new.py              # Main Streamlit application
├── chatbot.py          # Standalone Q&A generation script
├── img.py              # Image analysis utility
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Requirements

See `requirements.txt` for all dependencies:
- streamlit
- google-generativeai
- Pillow
- pdfplumber
- docx2txt

## Notes

- API key should be kept secure (consider using environment variables in production)
- The system prompt is configured to focus on error detection and debugging
- Supports Gemini 2.0 Pro experimental model for advanced code analysis
- Vision capabilities available for image-based code review

## License

Open source - modify and use as needed.

## Author

[raghobaa](https://github.com/raghobaa)
