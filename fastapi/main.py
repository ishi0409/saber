from fastapi import FastAPI, File, UploadFile
import pandas as pd
import io
import RC

app = FastAPI()

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))  
    return RC.total(df)


