import streamlit as st
from search_tool import google_search
from summarizer import summarize_results

st.set_page_config(page_title="Research Assistant Agent", page_icon="🔍", layout="wide")

st.title("🔍 Research Assistant Agent")
st.write("Helping research students by searching, summarizing, and explaining terms mathematically.")

query = st.text_input("Enter a research topic:")

if st.button("Search & Summarize"):
    if query:
        with st.spinner("Searching the web..."):
            results = google_search(query)

        with st.spinner("Summarizing results using Gemini..."):
            summary = summarize_results(query, results)

        st.subheader("📌 Summary")
        st.write(summary)

        st.subheader("🔗 Sources")
        for r in results:
            st.markdown(f"- [{r['title']}]({r['link']})")
    else:
        st.warning("Please enter a topic.")
