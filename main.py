import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file (For Local Development)
load_dotenv()

# Get API Key from environment variable or Streamlit secrets
API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

# Error handling for missing API key
if not API_KEY:
    st.error("❌ API Key not found! Set it in a `.env` file (local) or `Streamlit secrets` (cloud).")
    st.stop()

# Configure Google Gemini API
genai.configure(api_key=API_KEY)

# Streamlit UI
st.title("🤖 Secure Chatbot")
user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    model = genai.GenerativeModel("gemini-2.0-flash")  
    response = model.generate_content(user_input)
    st.write("🤖 Chatbot:", response.text)
