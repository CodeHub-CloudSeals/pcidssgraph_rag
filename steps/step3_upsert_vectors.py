import os
from neo4j_graphrag.embeddings import OpenAIEmbeddings
from neo4j_graphrag.indexes import upsert_vectors
from neo4j_graphrag.types import EntityType

def step3_upsert_vectors(driver):
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
    print("\n--- Running Step 3: Upserting vectors ---")
    text = "What are the policies and systems of PCI-DSS."
    embedder = OpenAIEmbeddings(
        model="models/embedding-001",
        api_key=GOOGLE_API_KEY,
        base_url=GEMINI_BASE_URL,
    )
    vector = embedder.embed_query(text)
    upsert_vectors(
        driver=driver,
        ids=["1234"],
        embedding_property="embedding",
        embeddings=[vector],
        entity_type=EntityType.NODE,
    )
    print("Embedding saved to Neo4j.")
