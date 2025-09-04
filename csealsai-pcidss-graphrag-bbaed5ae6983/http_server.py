import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from steps.step0_drop_existing_index import step0_drop_existing_index
from steps.step1_extract_graph_from_pdf import step1_extract_graph_from_pdf
from steps.step2_creating_vector_index import step2_creating_vector_index
from steps.step3_upsert_vectors import step3_upsert_vectors
from steps.step4_run_query import step4_run_query

# --- Setup ---
load_dotenv()

# --- Configuration ---
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
PDF_PATH = os.getenv("PDF_PATH")

# --- Neo4j Driver ---
driver = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global driver
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    yield
    if driver:
        driver.close()

# --- FastAPI App ---
app = FastAPI(lifespan=lifespan)

# --- API Endpoints ---
@app.post("/run/step0_drop_existing_index")
async def run_step0():
    return {"status": "Step 0 dummy response"}

@app.post("/run/step1_build_graph")
async def run_step1():
    return {"status": "Step 1 dummy response"}

@app.post("/run/step2_create_index")
async def run_step2():
    return {"status": "Step 2 dummy response"}

@app.post("/run/step3_upsert_vectors")
async def run_step3():
    return {"status": "Step 3 dummy response"}

@app.post("/run/step4_run_query")
async def run_step4():
    return {"status": "Step 4 dummy response"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("http_server:app", host="0.0.0.0", port=8000, reload=True)