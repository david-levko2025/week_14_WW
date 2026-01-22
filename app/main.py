from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import pandas as pd
from db import DBConnection 
from models import DataProcessing

    

app = FastAPI()


@app.post("/upload")
def create_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(detail="The file not provided",status_code=400)
    df = DataProcessing.main_function(file)
    insert_message = DBConnection.insert_data()
    return {"status": 'insert_message',
            "inserted records": len(df)}


if __name__ == "__main__":
    db_message = DBConnection.create_db()
    print (db_message)
    table_message = DBConnection.create_table()
    print(table_message)
    uvicorn.run("main:app",port=8000,host="localhost" ,reload=True)








    db_message = dc.create_db()
    print (db_message)
    table_message = dc.create_table()
    print(table_message)
