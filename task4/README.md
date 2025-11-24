# 📘 **Study Notes Summarizer & Quiz Generator**

A complete **AI-powered system** that converts any study-notes PDF into a clean summary and an interactive quiz.  
Built using **Gemini CLI**, **Context7 MCP Server**, **openagents SDK**, and **Gemini-2.0-flash**.

---

## 🚀 **Project Goal**
Turn any uploaded PDF into:
- 🔹 **Bullet-point summary**
- 🔹 **Auto-generated quizzes:**
  - 📝 **Multiple Choice Questions (MCQs)**
  - ✔️ **True / False**
  - ✏️ **Short-answer questions**
- 🔹 **PDF upload history** saved automatically
- 🔹 Click any previous file to view:
  - The PDF
  - Its summary
  - Its quizzes

---

## 🧠 **Core Features**

### 📤 **PDF Upload**
Upload any PDF. The backend stores the file and updates the history list.

### 📄 **Text Extraction**
Text is extracted using **PyPDF2**.  
(Scanned PDF OCR support can be added later.)

### 📝 **Smart Summarization**
Generates a structured **250–400 word bullet-point summary** using **OpenAI gpt-4o-mini**.

### 🧪 **Quiz Generation**
Automatically generates:
- 📝 **5 MCQs** (4 options each + explanation)
- ✔️ **True/False questions**
- ✏️ **3 Short-answer questions**

### 📚 **History Panel**
All uploaded PDFs appear in the sidebar.  
Click any item to instantly load:
- PDF preview
- Summary
- Quiz

### 🏗️ **Long PDF Support**
Handles 100+ page PDFs using automated chunking.

### 🎨 **Streamlit UI**
Includes:
- Cards
- Expanders
- Spinners
- Success alerts
- Sidebar history

---

## 🛠️ **Tech Stack**
| Component | Technology |
|----------|------------|
| **AI Model** | OpenAI gpt-4o-mini |
| **Agents** | openagents SDK |
| **Orchestration** | Context7 MCP Server |
| **Code Generation** | Gemini CLI |
| **UI Framework** | Streamlit |
| **PDF Tool** | PyPDF2 |
| **Package Manager** | uv |
| **Secrets** | .env |

---

## 📁 **Project Structure**
```bash
pdf-study-agent/
├─ app.py
├─ backend/
│  ├─ pipeline.py
│  ├─ agents.py
│  ├─ storage.py
│  └─ utils.py
├─ uploads/
├─ results/
├─ .env
├─ .env.example
└─ README.md
```
## 🤖 **Agents Overview**

### 🔹 **PDF Summarizer Agent**
- Creates **bullet-point summaries**
- Generates metadata like **page count**

### 🔹 **Quiz Generator Agent**
Creates:
- 📝 **MCQs**
- ✔️ **True/False**
- ✏️ **Short-answer questions**

---

## ⚡ **How to Run**
```bash
git clone https://github.com/yourusername/pdf-study-agent.git
cd pdf-study-agent
uv sync
cp .env.example .env
uv run streamlit run app.py
