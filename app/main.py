from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import pandas as pd
from contextlib import asynccontextmanager
from db import creat_table

@asynccontextmanager
async def lifespan(app: FastAPI):
    creat_table()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.post("/upload")
def create_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(detail="The file not provided",status_code=400)
    df = pd.read_csv(file.file)
    
    return {"status": "success",
            "inserted_records":len(df)
            }


if __name__ == "__main__":
     uvicorn.run("main:app",port=8000,host="localhost" ,reload=True)