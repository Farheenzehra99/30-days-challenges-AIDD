import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Agent Definition
AGENT = {
    "name": "PDF Summarizer Agent",
    "role": "Expert Document Summarizer",
    "instructions": """You are an expert PDF summarizer agent. Your task is to:
    1. Analyze documents
    2. Extract key points
    3. Create concise summaries
    4. Maintain accuracy and clarity""",
    "model": "gemini-2.0-flash"
}

def get_summary(text: str) -> str:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel(AGENT["model"])
    
    prompt = f"""
    {AGENT['instructions']}
    
    You are an expert in summarizing technical and academic documents.
    Your task is to create a concise, clear, and meaningful summary of the following text.
    The summary should capture the key points, main arguments, and any important conclusions.
    The summary should be approximately 200-300 words in length.
    Do not include any personal opinions or interpretations.
    The output should be a clean, well-structured summary.

    Here is the text to summarize:
    ---
    {text}
    ---
    """
    response = model.generate_content(prompt)
    
    return response.text