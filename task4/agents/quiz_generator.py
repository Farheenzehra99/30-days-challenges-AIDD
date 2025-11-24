import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Agent Definition
AGENT = {
    "name": "Quiz Generator Agent",
    "role": "Expert Quiz Creator",
    "instructions": """You are an expert quiz creator agent. Your task is to:
    1. Analyze text content
    2. Identify key concepts
    3. Create comprehensive quizzes
    4. Provide detailed answer keys""",
    "model": "gemini-2.0-flash"
}

def get_quiz(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Text cannot be empty")
    
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel(AGENT["model"])
    
    prompt = f"""
    {AGENT['instructions']}
    
    You are an expert quiz creator. Your task is to create a comprehensive quiz based on the following text.
    The quiz should test the understanding of the key concepts, definitions, and important details in the text.

    Please create a quiz with the following structure:
    1. **Multiple Choice Questions (5 questions):** Each question should have 4 options, with only one correct answer.
    2. **True/False Questions (3 questions):**
    3. **Short Answer Questions (2 questions):** These questions should require a brief explanation (1-2 sentences).

    After the quiz, provide a separate answer key with the correct answers and brief explanations for the multiple-choice and true/false questions.

    Here is the text to create the quiz from:
    ---
    {text}
    ---
    """
    response = model.generate_content(prompt)
    
    return response.text