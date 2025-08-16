from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

GEMINI_API_KEY = "A--------YOUR GEMINI API KEY-------E"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # or gemini-2.0-flash
    api_key=GEMINI_API_KEY
)

def summarize_results(query, search_results):
    context_text = "\n".join([f"Title: {r['title']}\nSnippet: {r['snippet']}" for r in search_results])

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a research assistant.
        Summarize the following search results in a concise way.
        If there are technical terms (like in Artificial Intelligence),
        explain them with mathematical notations if relevant.
        Always return a research-friendly explanation."""),
        ("human", f"Topic: {query}\n\nSearch Results:\n{context_text}")
    ])

    response = llm.invoke(prompt.format_messages())
    return response.content
