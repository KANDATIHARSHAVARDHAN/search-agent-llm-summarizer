# search-agent-llm-summarizer
# 🔍 Research Assistant Agent

A **Streamlit web app** that helps research students by **searching the web, summarizing results using Gemini LLM, and explaining technical terms mathematically**.  
This project combines **Google Custom Search API** and **Gemini 2.5 Flash** via LangChain to act as a personal **research assistant**.

---

## 🚀 Features
- 🌐 Web search powered by **Google Custom Search API**  
- 🧠 Summarization with **Gemini LLM (LangChain integration)**  
- 🔢 Mathematical explanations for technical/AI terms  
- 🎨 Simple and interactive **Streamlit UI**  

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- [Streamlit](https://streamlit.io/) – UI  
- [Google API Client](https://pypi.org/project/google-api-python-client/) – Web search  
- [LangChain](https://python.langchain.com/) – LLM orchestration  
- [Google Generative AI (Gemini)](https://ai.google.dev/) – Summarization  

---

## 📂 Project Structure
├── app.py # Main Streamlit application
├── search_tool.py # Google search helper
├── summarizer.py # Summarization with Gemini
└── README.md # Documentation

Install Dependencies
pip install streamlit google-api-python-client langchain langchain-google-genai


Configure API Keys

Get a Google API Key and Custom Search Engine (CSE ID) → Setup Guide

Get a Gemini API Key from Google AI Studio

Update inside app.py:

GOOGLE_API_KEY = "your-google-api-key"
SEARCH_ENGINE_ID = "your-search-engine-id"
GEMINI_API_KEY = "your-gemini-api-key"


Run the App
streamlit run app.py
