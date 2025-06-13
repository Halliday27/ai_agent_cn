import streamlit as st
import google.generativeai as genai

st.title("Gemini Chatbot")
genai.configure(api_key="YOUR_API_KEY")

if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-2.0-flash")
    st.session_state.chat = model.start_chat()
    st.session_state.history = []
    st.session_state.input = ""

def send_message():
    user_input = st.session_state.input
    if user_input:
        response = st.session_state.chat.send_message(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Gemini", response.text))
        st.session_state.input = ""

st.text_input("You:", key="input", on_change=send_message)

for speaker, message in st.session_state.history:
    st.markdown(f"**{speaker}:** {message}")