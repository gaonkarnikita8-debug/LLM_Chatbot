# My AI Chatbot

## About the Project
My AI Chatbot is a beginner-friendly AI chatbot built using Python, Streamlit, and Ollama. It runs a local language model to answer questions without requiring a paid AI API.

## Features
- Answers user questions using a local AI model.
- Remembers previous messages during the current chat session.
- Provides example questions to help users get started.
- Includes a Clear Chat button.
- Handles common connection and response errors.
- Uses simple instructions to encourage beginner-friendly explanations.

## Technologies Used
- Python
- Streamlit
- Ollama
- Qwen2.5 1.5B language model
- Requests library

## Requirements
- Python
- Ollama installed and running
- The `qwen2.5:1.5b` model downloaded
- Required Python libraries installed

## How to Run the Project

1. Start Ollama and make sure the model is available.
2. Open the project folder in the terminal.
3. Install the required libraries if they are not already installed:

   ```bash
   pip install streamlit requests
   ```

4. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL displayed in the terminal.

## What I Learned
- Calling a local AI model through an API.
- Writing and using Python functions.
- Handling exceptions.
- Managing chat history with Streamlit session state.
- Building a simple interactive web application.
