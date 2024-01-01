import streamlit as st

from langserve.client import RemoteRunnable

rag_app = RemoteRunnable("http://localhost:8000/rag-chroma")

st.title("Langchain Templates & Chroma RAG Demo")

request = st.text_area('Type a query ! ', height=50)
submit = st.button("submit", type="primary")

if submit and request:
    response = rag_app.invoke(request)
    st.write(response)
