import os
from neo4j_graphrag.indexes import create_vector_index

def step2_creating_vector_index(driver):
    INDEX_NAME = os.getenv("INDEX_NAME")
    print("\n--- Running Step 2: Creating vector index ---")
    create_vector_index(
        driver,
        INDEX_NAME,
        label="Chunk",
        embedding_property="embedding",
        dimensions=768,
        similarity_fn="euclidean",
    )
    print("Vector index created.")
