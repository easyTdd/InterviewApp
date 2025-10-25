
import os
import streamlit as st
from backend import get_openai_response

openai_api_key = st.secrets["OPENAI_API_KEY"]    
os.environ["OPENAI_API_KEY"] = openai_api_key

def on_user_input_change():
    if(st.session_state.user_input.strip() == ""):
        return
    
    st.session_state.chat_history.append({"role": "user", "content": st.session_state.user_input})

    response = get_openai_response(
        st.session_state.chat_history,
        parameters=st.session_state.input
    )

    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.session_state.user_input = ""

def on_interview_start():
    st.write(f"Temperature {st.session_state.temperature}, Number of questions {st.session_state.number_of_questions}, Position {st.session_state.position}, Industry {st.session_state.industry}")
    st.session_state.chat_history = []
    st.session_state.in_conversation = True
    st.session_state.user_input = ""
    st.session_state.input = {
        "temperature": st.session_state.temperature,
        "position": st.session_state.position,
        "industry": st.session_state.industry,
        "number_of_questions": st.session_state.number_of_questions
    }

def on_interview_end():
    st.session_state.in_conversation = False
    st.session_state.user_input = ""
    st.session_state.input = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "clear_input" not in st.session_state:
    st.session_state.clear_input = False

if "in_conversation" not in st.session_state:
    st.session_state.in_conversation = False

st.title("Interview Chatbot")

if st.session_state.in_conversation == False:
    st.markdown(f"**Model parameters**")
    st.slider('Temperature', min_value=0.0, max_value=2.0, value=0.7, step=0.1, key="temperature")
    st.markdown(f"**Interview parameters**")
    st.slider('Number of questions', min_value=1, max_value=10, value=3, step=1, key="number_of_questions")
    st.text_input("What position are you interviewing for?", key="position")
    st.text_input("What industry/company is the job in?", key="industry")
    st.button("Start Interview", on_click=on_interview_start)
else:    
    st.button("Start new interview", on_click=on_interview_end)
    st.markdown(f"**Interviewer:** Hi, it’s great to meet you. I’m glad you could make it today. Before we begin, how are you feeling?")

    for msg in st.session_state.chat_history:
        role_display = "Interviewer" if msg['role'] == "assistant" else "You"
        st.markdown(f"**{role_display}:** {msg['content']}")

    st.text_area("Type your message...", key="user_input", on_change=on_user_input_change)

    st.button("Send", on_click=on_user_input_change)

    st.markdown(
        """
        <script>
        document.querySelector('div.st-key-user_input input').focus();
        </script>
        """,
        unsafe_allow_html=True
    )
