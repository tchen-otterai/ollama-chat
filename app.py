import streamlit as st
import requests
import json
import os
import time

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/chat"
DATA_DIR = "data"

def stream_response(messages):
    response = requests.post(OLLAMA_API_URL, json={
        "model": "llama3.1",
        "messages": messages,
        "stream": True
    }, stream=True)
    
    for line in response.iter_lines():
        if line:
            yield json.loads(line)

def get_conversations():
    if "conversations" not in st.session_state:
        st.session_state.conversations = load_conversations()
    return st.session_state.conversations

def get_current_conversation():
    if "current_conversation" not in st.session_state:
        st.session_state.current_conversation = "Default"
    return st.session_state.current_conversation

def set_current_conversation(conversation_name):
    st.session_state.current_conversation = conversation_name

def add_message_to_history(role, content):
    current_conversation = get_current_conversation()
    st.session_state.conversations[current_conversation].append({"role": role, "content": content})
    save_conversations()

def clear_conversation():
    current_conversation = get_current_conversation()
    st.session_state.conversations[current_conversation] = []
    save_conversations()

def create_new_conversation(name):
    if name and name not in st.session_state.conversations:
        st.session_state.conversations[name] = []
        set_current_conversation(name)
        save_conversations()

def load_conversations():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    try:
        with open(os.path.join(DATA_DIR, "conversations.json"), "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"Default": []}

def save_conversations():
    with open(os.path.join(DATA_DIR, "conversations.json"), "w") as f:
        json.dump(st.session_state.conversations, f)

def main():
    st.title("Ollama Chat Interface")

    # Sidebar for conversation management
    st.sidebar.title("Conversations")
    
    # Create new conversation
    new_conversation_name = st.sidebar.text_input("New conversation name")
    if st.sidebar.button("Create"):
        create_new_conversation(new_conversation_name)

    # List and select conversations
    conversations = get_conversations()
    current_conversation = get_current_conversation()
    selected_conversation = st.sidebar.selectbox(
        "Select conversation",
        options=list(conversations.keys()),
        index=list(conversations.keys()).index(current_conversation)
    )
    if selected_conversation != current_conversation:
        set_current_conversation(selected_conversation)
        st.experimental_rerun()

    if st.sidebar.button("Clear Current Conversation"):
        clear_conversation()

    # Main chat interface
    chat_container = st.container()

    # Display conversation history
    for message in conversations[current_conversation]:
        with chat_container.chat_message(message["role"]):
            st.write(message["content"])

    # User input
    user_input = st.chat_input("Type your message here...")
    if user_input:
        # Add user message to conversation
        add_message_to_history("user", user_input)
        
        # Display user message
        with chat_container.chat_message("user"):
            st.write(user_input)
        
        # Get AI response
        with chat_container.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for chunk in stream_response(conversations[current_conversation]):
                if 'content' in chunk['message']:
                    full_response += chunk['message']['content']
                    message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        # Add AI response to conversation
        add_message_to_history("assistant", full_response)

if __name__ == "__main__":
    main()