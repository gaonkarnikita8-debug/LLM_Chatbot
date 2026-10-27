
import streamlit as st
import requests
from datetime import datetime


# Page settings
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖"
)

# Chatbot settings
URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:1.5b"


# Function to get the AI response
def get_ai_response(messages):
    today = datetime.now().astimezone().strftime("%A, %d %B %Y")

    system_message = {
        "role": "system",
        "content": (
            f"Today's date is {today}. "
            "You are a friendly AI assistant and beginner-friendly Python tutor. "
            "Explain technical topics in simple English. "
            "Give small examples when helpful. "
            "If you do not know an answer, say so instead of guessing."
        )
    }

    data = {
        "model": MODEL,
        "messages": [system_message] + messages,
        "stream": False
    }

    try:
        response = requests.post(
            URL,
            json=data,
            timeout=120
        )
        response.raise_for_status()

        result = response.json()
        return result["message"]["content"]

    except requests.exceptions.ConnectionError:
        return "ERROR: Could not connect to Ollama. Please make sure Ollama is running."

    except requests.exceptions.Timeout:
        return "ERROR: The request took too long. Please try again."

    except requests.exceptions.RequestException:
        return "ERROR: A request error occurred."

    except (ValueError, KeyError, TypeError):
        return "ERROR: Could not read the AI response."


# Website heading
st.title("🤖 My AI Chatbot")
st.caption("Your personal AI assistant, powered by Ollama.")


# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Clear chat button
st.sidebar.title("Chat Settings")

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# Welcome screen
if not st.session_state.messages:
    st.markdown("### 👋 Hello! Welcome to My AI Chatbot.")

    st.write(
        "I'm your personal AI assistant. "
        "Ask me questions about Python, programming, "
        "or any topic you want to learn."
    )

    st.markdown("#### Try asking me:")

    if st.button("🐍 Explain Python functions"):
        st.session_state.selected_question = (
            "Explain Python functions in simple English."
        )

    if st.button("🤖 What is an LLM?"):
        st.session_state.selected_question = (
            "What is an LLM? Explain in simple English."
        )

    if st.button("💻 Give me a Python exercise"):
        st.session_state.selected_question = (
            "Give me one beginner-friendly Python exercise."
        )


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Get the user's question
question = st.chat_input("Ask me anything...")

if "selected_question" in st.session_state:
    question = st.session_state.pop("selected_question")


# Process the question
if question and question.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_ai_response(st.session_state.messages)

        if answer.startswith("ERROR:"):
            st.error(answer)
            st.session_state.messages.pop()
        else:
            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })
