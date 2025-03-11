from langchain.vectorstores import Chroma

def create_vector_store(text_chunks, embedding_model, persist_directory='db'):
    vector_store = Chroma.from_documents(text_chunks, embedding=embedding_model, persist_directory=persist_directory)
    return vector_store