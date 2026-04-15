from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import io
import RC
import os

app = FastAPI()

FRONT_URL = os.getenv("FRONT_URL")

origins = [
    FRONT_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        
    allow_credentials=True,       
    allow_methods=["POST", "GET"],   
    allow_headers=["*"],          
)

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))  
    return RC.total(df)


