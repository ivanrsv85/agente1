import streamlit as st
import requests

API_URL = "https://your-app.onrender.com/chat"  # Replace with your API URL

st.set_page_config(page_title="💬 Mortgage Chatbot", layout="wide")
st.title("🏡 Mortgage Broker Chatbot")

query = st.text_input("Ask a question about mortgage regulations, commissions, or processes:")

if st.button("Get Answer") and query:
    response = requests.get(API_URL, params={"query": query})
    if response.status_code == 200:
        st.write(response.json().get("response", "No response received."))
    else:
        st.error("Error fetching response!")
