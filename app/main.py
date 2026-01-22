from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn




app = FastAPI()

@app.post("/upload")
def create_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(detail="The file not provided",status_code=400)
    return {"The weapon list": file.file}


if __name__ == "__main__":
     uvicorn.run("main:app",port=8000,host="localhost" ,reload=True)