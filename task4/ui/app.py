import streamlit as st
import os
import sys

# Path setup
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

from backend.tools import extract_pdf_text
from backend.pipeline import run_pipeline

# -------------------------------
# 🎨 CUSTOM CSS FOR UI BEAUTIFICATION
# -------------------------------

st.markdown("""
    <style>
        /* Gradient Title */
        .title {
            font-size: 60px;
            font-weight: 800;
            background: linear-gradient(90deg, #7B1FA2, #BA68C8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: -10px;
        }

        /* REMOVE grey uploader block */
        .stFileUploader { background: transparent !important; }
        .stFileUploader label { color: black !important; }

        /* Sidebar Name */
        .sidebar-header {
            font-size: 26px;
            font-weight: bold;
            background: linear-gradient(90deg, #7B1FA2, #BA68C8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding: 10px 0;
        }

        /* Glowing Button */
        .stButton>button {
            background: linear-gradient(90deg, #7B1FA2, #BA68C8);
            color: white;
            border-radius: 10px;
            padding: 12px 22px;
            font-size: 18px;
            border: none;
            transition: 0.3s;
            box-shadow: 0px 0px 10px rgba(123, 31, 162, 0.4);
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0px 0px 20px rgba(123, 31, 162, 0.7);
        }

        /* Card */
        .card {
            padding: 20px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(8px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }

        /* History Items */
        .history-item {
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
            background: rgba(123, 31, 162, 0.2);
            cursor: pointer;
            transition: 0.2s;
        }
        .history-item:hover {
            background: rgba(123, 31, 162, 0.4);
            transform: scale(1.02);
        }

        /* Hide grey lines */
        hr { display: none; }

    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 🌟 MAIN UI TITLE
# -------------------------------
st.markdown("<h1 class='title'>Study Notes Assistant</h1>", unsafe_allow_html=True)

# -------------------------------
# 📌 SIDEBAR
# -------------------------------
st.sidebar.markdown("<h2 class='sidebar-header'>🤖 Your Personal AI Study Agent</h2>", unsafe_allow_html=True)
st.sidebar.write("Made by👩‍🎓 **Farheen Zehra**")
st.sidebar.write("---")

# PDF History Storage
if "pdf_history" not in st.session_state:
    st.session_state.pdf_history = []

if "selected_pdf" not in st.session_state:
    st.session_state.selected_pdf = None

# Clickable history items that load PDF
if st.session_state.pdf_history:
    st.sidebar.subheader("📂 PDF History")
    for pdf in st.session_state.pdf_history:
        if st.sidebar.button(pdf, key=f"hist_{pdf}"):
            st.session_state.selected_pdf = pdf
            st.success(f"📄 Loaded from history: {pdf}")
            with open(os.path.join("pdf", pdf), "rb") as file:
                st.download_button(
                    label=f"Open {pdf}",
                    data=file,
                    file_name=pdf,
                    mime="application/pdf"
                )

# -------------------------------
# 📁 PDF Upload
# -------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("📄 Upload your PDF file", type="pdf")
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# 🧠 SUMMARY + QUIZ
# -------------------------------
if uploaded_file is not None:

    if not os.path.exists("pdf"):
        os.makedirs("pdf")

    file_path = os.path.join("pdf", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✔ {uploaded_file.name} uploaded successfully")

    # Save in history
    if uploaded_file.name not in st.session_state.pdf_history:
        st.session_state.pdf_history.append(uploaded_file.name)

    # Generate Summary
    if st.button("✨ Generate Study Notes"):
        with st.spinner("Extracting text & generating summary..."):
            pdf_text = extract_pdf_text(file_path)

            if pdf_text:
                result = run_pipeline(pdf_text)
                st.markdown("### 📘 Summary")
                st.text_area("Summary Results", result, height=400)
            else:
                st.error("⚠ Unable to extract text from PDF")

    # Generate Quiz
    if st.button("📝 Generate Quiz"):
        pdf_text = extract_pdf_text(file_path)

        if pdf_text:
            quiz = run_pipeline(pdf_text, mode="quiz")
            st.markdown("### 🧩 Quiz")
            st.text_area("Quiz Output", quiz, height=350)
        else:
            st.error("⚠ Unable to extract text from PDF")

# END
