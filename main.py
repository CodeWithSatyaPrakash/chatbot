import streamlit as st
import google.generativeai as genai
import os  # Import OS to load environment variables

# Load API Key from environment variables
API_KEY = os.getenv("GEMINI_API_KEY")  # Use environment variable
if not API_KEY:
    st.error("⚠️ API key is missing! Set GEMINI_API_KEY as an environment variable.")
    st.stop()

# Configure Gemini API securely
genai.configure(api_key=API_KEY)

# Streamlit UI
st.title("🤖 Trivia Chatbot")

# User input field
user_input = st.text_input("You:", placeholder="Type your message here...")

# Generate response
if user_input:
    model = genai.GenerativeModel("gemini-2.0-flash")  # Fast Gemini model
    response = model.generate_content(user_input)

    # Display chatbot response
    st.write("🤖 Chatbot:", response.text)
