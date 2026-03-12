import streamlit as st
from query_data import query_rag

st.title("AI Business Document Assistant")

question = st.text_input("Ask a question about your documents")

if st.button("Submit"):
    if question:
        response = query_rag(question)
        st.write(response)