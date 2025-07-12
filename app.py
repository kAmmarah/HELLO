import streamlit as st
from gemini_agent import ask_gemini  # Make sure this import works

st.title("Gemini Agentic AI by Ammara Dawood")

prompt = st.text_area("Enter your prompt:")
if st.button("Ask Gemini"):
    if prompt.strip():
        response = ask_gemini(prompt)
        st.write("**Response:**")
        st.write(response)
    else:
        st.warning("Please enter a prompt.")