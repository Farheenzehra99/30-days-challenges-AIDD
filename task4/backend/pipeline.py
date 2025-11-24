from agents.pdf_summarizer import get_summary
from agents.quiz_generator import get_quiz

def run_pipeline(text: str, mode="both") -> str:
    if mode == "summary":
        return get_summary(text)
    elif mode == "quiz":
        return get_quiz(text)
    elif mode == "both":
        summary = get_summary(text)
        quiz = get_quiz(text)
        return f"Summary:\n{summary}\n\nQuiz:\n{quiz}"
    else:
        raise ValueError("Invalid mode. Choose 'summary', 'quiz', or 'both'.")
