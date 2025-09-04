import os
import asyncio
import nest_asyncio
from dotenv import load_dotenv
from neo4j import GraphDatabase
from steps.step0_drop_existing_index import step0_drop_existing_index
from steps.step1_extract_graph_from_pdf import step1_extract_graph_from_pdf
from steps.step2_creating_vector_index import step2_creating_vector_index
from steps.step3_upsert_vectors import step3_upsert_vectors
from steps.step4_run_query import step4_run_query
 
# --- Setup ---
load_dotenv()
nest_asyncio.apply()
 
 
# --- Configuration ---
# Neo4j Credentials
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
 
# Other Constants
PDF_PATH = os.getenv("PDF_PATH")
 
# --- Main Execution ---
async def main():
 
    driver = GraphDatabase.driver(
        NEO4J_URI,
        auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
    )
   
    step0_drop_existing_index(driver)
    await step1_extract_graph_from_pdf(driver, PDF_PATH)
    step2_creating_vector_index(driver)
    step3_upsert_vectors(driver)
    step4_run_query(driver)
   
    driver.close()
 
if __name__ == "__main__":
    asyncio.run(main())
 