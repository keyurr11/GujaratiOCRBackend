from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Gujarati OCR Backend Running"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "File received successfully"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
