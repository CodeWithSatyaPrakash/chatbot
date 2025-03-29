import streamlit as st
import google.generativeai as genai
import os

# Retrieve API key securely from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Streamlit UI
st.title("🤖 Chatbot")

# User input field
user_input = st.text_input("You:", placeholder="Type your message here...")

# Generate response
if user_input:
    model = genai.GenerativeModel("gemini-2.0-flash")  # Fast Gemini model
    response = model.generate_content(user_input)

    # Display chatbot response
    st.write("🤖 Chatbot:", response.text)
