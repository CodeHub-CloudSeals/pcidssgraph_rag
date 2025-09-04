import os
from neo4j_graphrag.llm import OpenAILLM
from utils.pdf_extractor import extract_pdf_text

async def step1_extract_graph_from_pdf(driver, pdf_path):
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
    print("\n--- Running Step 1: Extracting graph from PDF ---")
    llm = OpenAILLM(
        model_name="models/gemini-1.5-flash",
        api_key=GOOGLE_API_KEY,
        base_url=GEMINI_BASE_URL,
    )
    text = extract_pdf_text(pdf_path)
    prompt = f"""
    Extract entities and relationships from the following PCI-DSS text.
    Use JSON with fields: nodes (id, type, name), edges (source, relation, target).
    Text:
    {text[:5000]}
    """
    response = await llm.ainvoke(prompt)
    kg_json = response.content
    with driver.session() as session:
        session.run("MERGE (r:RawExtraction {content:$c})", c=kg_json)
    print("Graph data inserted into Neo4j.")
