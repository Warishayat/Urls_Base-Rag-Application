# Chatbot-RAG-Application

A simple chatbot application built with Streamlit that utilizes LangChain and Google Generative AI for document retrieval and question answering based on provided URLs.

## Overview

This application allows users to input URLs, processes the content of those URLs, and then allows users to ask questions based on the content retrieved from the URLs. It uses a combination of LangChain's document loading, splitting, and retrieval chains, along with Google Generative AI for embeddings and answering user queries.

## Features

- **URL Upload**: Users can input URLs, which are processed to extract text.
- **Text Splitting**: Large texts are split into smaller chunks for efficient retrieval.
- **Question Answering**: Users can ask questions, and the chatbot provides answers based on the content retrieved from the provided URLs.
- **Google Generative AI**: Uses Google's generative model (Gemini) for processing and embedding documents.

## Installation

### 1. Set up a Python Virtual Environment

First, create a virtual environment for your project:

```bash
python -m venv venv
```

Activate the virtual environment:

- For **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- For **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 2. Install Required Dependencies

Install the required libraries by running:

```bash
pip install -r requirements.txt
```

Make sure to create a `requirements.txt` file if it doesn't exist, and add the necessary packages such as:

```
streamlit
langchain
langchain-google-genai
python-dotenv
faiss-cpu
```

### 3. Set up Environment Variables

The application uses `dotenv` to load environment variables. Ensure you have a `.env` file with your API keys or configurations as needed, like this:

```
API_KEY=your_google_api_key
```

### 4. Run the Application

To start the application, run the following command:

```bash
streamlit run app.py
```

This will launch the app in your browser.

## Usage

### 1. Input URLs

- After launching the app, you will see an input field where you can enter the URL(s).
- The URLs will be processed, and the content will be loaded and split into smaller chunks for easier retrieval.

### 2. Ask Questions

- After the URLs are processed, you can ask questions about the content.
- The chatbot will retrieve relevant context from the provided URLs and attempt to answer the question using Google Generative AI.

### 3. Interact with the Chatbot

- The chatbot will provide answers based on the documents retrieved from the URLs.
- If the chatbot cannot find an answer, it will inform you that it doesn't have enough knowledge.

## Example

1. **Enter URL(s)**: `https://example.com`
2. **Ask a Question**: "What is the main topic of this page?"
3. **Receive Answer**: The chatbot will provide an answer based on the extracted content.

## Technologies Used

- **Streamlit**: For building the user interface.
- **LangChain**: For document processing, text splitting, and retrieval.
- **Google Generative AI**: For embeddings and model-based question answering.
- **FAISS**: For efficient similarity search of document embeddings.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:
1. Make sure to include a `requirements.txt` with the necessary dependencies like `streamlit`, `langchain`, `python-dotenv`, `faiss-cpu`, etc.
2. If you're working with any proprietary models or APIs (e.g., Google's Generative AI API), make sure to mention any necessary API keys or credentials setup in the `.env` file.
3. Depending on your project structure, you may need to adjust file names like `app.py` or any other filenames if they differ.
