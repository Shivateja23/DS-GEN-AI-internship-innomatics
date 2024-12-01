import streamlit as st
import google.generativeai as ai
from PIL import Image


st.image(r"B:\GENAI-INTERN\GENAI_PROJECTS\ai img.jpg")

# Set the API key directly
api_key1 = "AIzaSyDqJcz2QEMe8Leu2ifhkrhg9l3d8M7k1c0"
ai.configure(api_key=api_key1)

sys_prompt = """You are a helpful AI Tutor for Data Science. 
                Students will ask you doubts related to various topics in data science.
                You are expected to reply in as much detail as possible. 
                Make sure to take examples while explaining a concept.
                In case if a student ask any question outside the data science scope, 
                politely decline and tell them to ask the question from data science domain only."""

# Initialize the model (check if `Generativemodel` is correct; it might vary)
model = ai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                            system_instruction=sys_prompt)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chatbot = model.start_chat(history=[])

st.title("Data Science Tutor Application")

st.chat_message("ai").write("**Hey ! I'm your Data Science Tutor. How can i help you**")

# Collect user input

st.sidebar.title("Chat History")
if st.session_state.chat_history:
    for i, (role, text) in enumerate(st.session_state.chat_history):
        st.sidebar.write(f"**{i + 1}. {role.capitalize()}**: {text}")

user_prompt = st.chat_input("I'm looking for details here...")



if  user_prompt:
    # Generate the response
    st.session_state.chat_history.append(("human", user_prompt))
    st.chat_message("human").write(user_prompt)
    
    # Generate AI response
    response = chatbot.send_message(user_prompt)
    st.session_state.chat_history.append(("ai", response.text))
    st.chat_message("ai").write(response.text)

    # response = model.generate_content(user_prompt)  # Confirm the correct method name here
    # st.session_state.chat_history.append(("ai", response.text))
    # st.write(response.text)
