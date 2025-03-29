import streamlit as st
import google.generativeai as genai

# Configure Gemini API (Use your API key from https://aistudio.google.com/)
genai.configure(api_key="AIzaSyAA2ulJlwwje5y-D4xztAU7x0yrZZx16Cw")

# Streamlit UI
st.title("🤖  Chatbot")

# User input field
user_input = st.text_input("You:", placeholder="Type your message here...")

# Generate response
if user_input:
    model = genai.GenerativeModel("gemini-2.0-flash")  # Fast Gemini model
    response = model.generate_content(user_input)

    # Display chatbot response
    st.write("🤖 Chatbot:", response.text)

