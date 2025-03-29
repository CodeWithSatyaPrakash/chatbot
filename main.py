import streamlit as st
import google.generativeai as genai

# Get API key from Streamlit secrets
API_KEY = st.secrets[GEMINI_API_KEY]

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Streamlit UI
st.title("🤖 Secure Chatbot")
user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    model = genai.GenerativeModel("gemini-2.0-flash")  
    response = model.generate_content(user_input)
    st.write("🤖 Chatbot:", response.text)
