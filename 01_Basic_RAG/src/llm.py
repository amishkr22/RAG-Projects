from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from huggingface_hub import hf_hub_download

def setup_llm():
    repo_id = "TheBloke/Llama-2-7B-Chat-GGML"
    filename = "llama-2-7b-chat.ggmlv3.q4_0.bin"
    file_path = hf_hub_download(repo_id=repo_id, filename=filename)
    
    llm = CTransformers(model=file_path,
                        model_type='llama',
                        config={'max_new_tokens':512,
                                'temperature':0.8})
    return llm

def setup_qa_chain(llm, vector_store):
    prompt_template = """
    Use the following pieces of information to answer the user's question.
    If you don't know the answer , just say don't know , don't try to make up an answer.

    Context: {context}
    Question: {question}

    Only return the helpful answer below and nothing else.
    Helpful answer:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])
    chain_type_kwargs = {'prompt': prompt}
    
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs
    )
    return qa