
import streamlit as st
from backend import get_openai_response

def on_user_input_change():
    if(st.session_state.user_input.strip() == ""):
        return
    
    st.session_state.chat_history.append({"role": "user", "content": st.session_state.user_input})

    response = get_openai_response(
        st.session_state.chat_history,
        temperature=st.session_state.temperature
    )

    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.session_state.user_input = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "clear_input" not in st.session_state:
    st.session_state.clear_input = False

st.title("Interview Chatbot")

st.slider('Temperature', min_value=0.0, max_value=2.0, value=0.7, step=0.1, key="temperature")

st.markdown(f"**Interviewer:** Hi, it’s great to meet you. I’m glad you could make it today. Before we begin, how are you feeling?")

for msg in st.session_state.chat_history:
    role_display = "Interviewer" if msg['role'] == "assistant" else "You"
    st.markdown(f"**{role_display}:** {msg['content']}")

st.text_input("Type your message...", key="user_input", on_change=on_user_input_change)

st.button("Send", on_click=on_user_input_change)

st.markdown(
    """
    <script>
    document.querySelector('div.st-key-user_input input').focus();
    </script>
    """,
    unsafe_allow_html=True
)
