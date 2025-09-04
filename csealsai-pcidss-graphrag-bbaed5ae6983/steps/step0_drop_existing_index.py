import os
def step0_drop_existing_index(driver):
    INDEX_NAME=os.getenv("INDEX_NAME")
    print("Running step 0: Dropping existing index")
    with driver.session() as session:
        session.run(f"Drop Index {INDEX_NAME} If exists")
    print(f"INDEX '{INDEX_NAME}' DROPPED SUCCESSFULLY")




