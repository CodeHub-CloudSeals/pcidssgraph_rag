import os
from neo4j_graphrag.embeddings import OpenAIEmbeddings
from neo4j_graphrag.generation import GraphRAG
from neo4j_graphrag.llm import OpenAILLM
from neo4j_graphrag.retrievers import VectorRetriever

def step4_run_query(driver):
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
    INDEX_NAME = os.getenv("INDEX_NAME")
    print("\n--- Running Step 4: Running a RAG query ---")
    embedder = OpenAIEmbeddings(
        model="models/embedding-001",
        api_key=GOOGLE_API_KEY,
        base_url=GEMINI_BASE_URL,
    )
    retriever = VectorRetriever(driver, INDEX_NAME, embedder)
    llm = OpenAILLM(
        model_name="models/gemini-1.5-flash",
        api_key=GOOGLE_API_KEY,
        base_url=GEMINI_BASE_URL,
        model_params={"max_tokens": 1000},
    )
    rag = GraphRAG(retriever=retriever, llm=llm)
    query_text = "What are the policies of PCI-DSS"
    response = rag.search(query_text=query_text, retriever_config={"top_k": 5})
    print("Answer:", response.answer)
