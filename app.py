\
    from fastapi import FastAPI, File, UploadFile
    from fastapi.responses import JSONResponse
    import easyocr
    import uvicorn
    import shutil
    import os

    app = FastAPI()

    # Load EasyOCR model (Gujarati + English)
    reader = easyocr.Reader(['gu', 'en'], gpu=False)

    @app.post("/ocr")
    async def ocr_api(file: UploadFile = File(...)):
        try:
            # Save temp file
            temp_path = "temp_image.png"
            with open(temp_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Perform OCR
            result = reader.readtext(temp_path, detail=0)

            # Delete temp
            os.remove(temp_path)

            return {"text": " ".join(result)}

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})


    @app.get("/")
    def home():
        return {"status": "Gujarati OCR API running successfully!"}


    if __name__ == "__main__":
        uvicorn.run("app:app", host="0.0.0.0", port=8000)
