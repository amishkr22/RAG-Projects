import gradio as gr
from src.data_loader import load_pdf, text_chunking
from src.embeddings import download_hugging_face_embeddings
from src.vector_store import create_vector_store
from src.llm import setup_llm, setup_qa_chain

# Load and process the PDF data
extracted_data = load_pdf('Data/')
text_chunks = text_chunking(extracted_data)

# Download embeddings
embedding_model = download_hugging_face_embeddings()

# Create vector store
vector_store = create_vector_store(text_chunks, embedding_model)

# Setup LLM and QA chain
llm = setup_llm()
qa_chain = setup_qa_chain(llm, vector_store)

# Define the function to be used by Gradio
def ask_question(question):
    result = qa_chain({'query': question})
    return result['result']

# Create Gradio interface
iface = gr.Interface(fn=ask_question, 
                     inputs="text", 
                     outputs="text", 
                     title="PDF Q&A System",
                     description="Ask any question based on the loaded PDF documents.")

# Launch the app
iface.launch()