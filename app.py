from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Gujarati OCR backend is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return JSONResponse({
        "filename": file.filename,
        "status": "File received successfully"
    })
