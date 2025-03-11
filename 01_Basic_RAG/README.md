# Basic RAG (Retrieval-Augmented Generation)

This repository contains a Python-based application that allows users to ask questions and get answers based on the content of PDF documents. The system uses **Retrieval-Augmented Generation (RAG)**, a technique that combines retrieval-based methods with generative language models to provide accurate and context-aware answers.

## Overview

The system works as follows:
1. **Load PDF Documents**: The application loads PDF files from a specified directory.
2. **Chunk Text**: The text from the PDFs is split into smaller chunks for efficient processing.
3. **Generate Embeddings**: Text chunks are converted into embeddings using a pre-trained Hugging Face model (`sentence-transformers/all-MiniLM-L6-v2`).
4. **Create Vector Store**: The embeddings are stored in a vector database (Chroma) for fast retrieval.
5. **Set Up LLM**: A language model (LLaMA-2-7B) is used to generate answers based on the retrieved context.
6. **Answer Questions**: Users can ask questions, and the system retrieves relevant text chunks and generates answers using the LLM.

## Key Components

### 1. Retrieval-Augmented Generation (RAG)
RAG is a hybrid approach that combines:
- **Retrieval**: Fetching relevant documents or text chunks from a knowledge base.
- **Generation**: Using a generative language model to produce answers based on the retrieved context.

This approach ensures that the answers are both accurate and contextually relevant.

### 2. Modules
The code is modularized into the following components:
- **`data_loader.py`**: Handles loading and chunking PDF documents.
- **`embeddings.py`**: Downloads and manages Hugging Face embeddings.
- **`vector_store.py`**: Creates and manages the vector database (Chroma).
- **`llm_setup.py`**: Sets up the language model (LLaMA-2-7B) and the QA chain.

### 3. Gradio Interface
The system is wrapped in a Gradio app, providing a user-friendly web interface for interacting with the Q&A system.

---

## How It Works

1. **Load PDFs**:
   - PDF files are loaded from the `Data/` directory using `PyPDFLoader`.
   - The text is extracted and split into smaller chunks for processing.

2. **Generate Embeddings**:
   - Text chunks are converted into embeddings using the `sentence-transformers/all-MiniLM-L6-v2` model.

3. **Create Vector Store**:
   - The embeddings are stored in a Chroma vector database for efficient retrieval.

4. **Set Up LLM**:
   - The LLaMA-2-7B model is downloaded and configured for text generation.
   - A QA chain is set up to retrieve relevant text chunks and generate answers.

5. **Ask Questions**:
   - Users can input questions via the Gradio interface.
   - The system retrieves relevant text chunks and generates answers using the LLM.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-qa-system.git
   cd pdf-qa-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your PDF files in the `Data/` directory.

4. Run the Gradio app:
   ```bash
   python app.py
   ```

5. Open the Gradio interface in your browser (usually at `http://127.0.0.1:7860`).

---

## Usage

1. Launch the Gradio app by running `python app.py`.
2. Enter your question in the input box.
3. The system will retrieve relevant information from the PDFs and generate an answer.

Example Questions:
- "What is the main topic of the document?"
- "Who is the author of the document?"
- "Explain the key findings in the document."

---

## Dependencies

The project relies on the following Python libraries:
- `langchain`: For document loading, text splitting, embeddings, and QA chains.
- `chromadb`: For vector storage and retrieval.
- `sentence-transformers`: For generating text embeddings.
- `ctransformers`: For running the LLaMA-2-7B model.
- `gradio`: For creating the web interface.

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

---

## Customization

- **PDF Directory**: Update the `Data/` directory path in `data_loader.py` to load your own PDFs.
- **Embedding Model**: Change the embedding model in `embeddings.py` to use a different Hugging Face model.
- **LLM**: Modify `llm_setup.py` to use a different language model or adjust parameters like `temperature` and `max_new_tokens`.

---