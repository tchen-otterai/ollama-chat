# Streamlit Ollama Chat App

This Streamlit application provides a chat interface for interacting with the Ollama AI model. It supports multiple conversations and real-time streaming of responses.

## Prerequisites

- Python 3.8 or higher
- pyenv
- [Ollama](https://ollama.com/) (running locally)

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/TWTimChen/ollama-chat.git
   cd ollama-chat
   ```

2. Set up a Python virtual environment using pyenv:
   ```
   pyenv install 3.9.0  # or your preferred Python version
   pyenv local 3.9.0
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Ensure Ollama is installed and running on your local machine. The app expects Ollama to be available at `http://localhost:11434`.

## Running the App

1. Make sure your virtual environment is activated.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

- The main chat interface is in the center of the screen.
- Use the sidebar to create new conversations or switch between existing ones.
- Type your messages in the input box at the bottom of the chat interface.
- The AI's responses will stream in real-time.
- Use the "Clear Current Conversation" button in the sidebar to reset the current chat.

## Customization

- To change the Ollama model, modify the `"model"` parameter in the `stream_response` function in `app.py`.
- Adjust the `OLLAMA_API_URL` if your Ollama instance is running on a different port or machine.

## Troubleshooting

- If you encounter any issues with Ollama connectivity, ensure that the Ollama service is running and accessible at the specified URL.
- For any Python-related issues, verify that you're using a compatible Python version and that all dependencies are correctly installed in your virtual environment.

## Contributing

Feel free to fork this repository and submit pull requests for any enhancements you develop!

## License

[Specify your license here, e.g., MIT, GPL, etc.]