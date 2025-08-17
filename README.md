# search-agent-llm-summarizer

## 🔍 Research Assistant Agent

A **Streamlit web app** that helps research students by **searching the web, summarizing results using Gemini LLM, and explaining technical terms mathematically**. This project combines **Google Custom Search API** and **Gemini 2.5 Flash** via LangChain to act as a personal **research assistant**.

---

## 🚀 Features

- 🌐 Web search powered by **Google Custom Search API**
- 🧠 Summarization with **Gemini LLM (LangChain integration)**  
- 🔢 Mathematical explanations for technical/AI terms
- 🎨 Simple and interactive **Streamlit UI**

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** – UI
- **Google API Client** – Web search  
- **LangChain** – LLM orchestration
- **Google Generative AI (Gemini)** – Summarization

---

## 📂 Project Structure

```
search-agent-llm-summarizer/
├── app.py              # Main Streamlit application
├── search_tool.py      # Google search helper
├── summarizer.py       # Summarization with Gemini
└── README.md           # Documentation
```

---

## ⚡ Quick Setup



### 1. Install Dependencies
```bash
pip install streamlit google-api-python-client langchain langchain-google-genai
```

### 2. Configure API Keys

**Get API Keys:**
- **Google API Key** and **Custom Search Engine (CSE ID)** → [Setup Guide](https://developers.google.com/custom-search/v1/introduction)
- **Gemini API Key** from [Google AI Studio](https://makersuite.google.com/app/apikey)

**Update API keys in your files:**

```python
# In search_tool.py
GOOGLE_API_KEY = "your-google-api-key"
SEARCH_ENGINE_ID = "your-search-engine-id"

# In summarizer.py  
GEMINI_API_KEY = "your-gemini-api-key"
```

### 3. Run the App
```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the app in your browser (usually `http://localhost:8501`)
2. Enter any research topic in the text input
3. Click **"Search & Summarize"**
4. View the AI-generated summary and original sources

### 📋 Example Queries

- "Machine learning neural networks"
- "Quantum computing algorithms" 
- "Natural language processing transformers"
- "Computer vision deep learning"
- "Reinforcement learning applications"

---

## 🔧 Configuration

### Google Custom Search Setup

1. Go to [Google Custom Search](https://cse.google.com/cse/)
2. Create a new search engine
3. Copy your **Search Engine ID**
4. Enable **Custom Search JSON API** in Google Cloud Console

---

## 🎯 Key Files Overview

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit interface with user input, search trigger, and results display |
| `search_tool.py` | Google Custom Search API integration to fetch web results |
| `summarizer.py` | Gemini LLM integration via LangChain for intelligent summarization |

---

