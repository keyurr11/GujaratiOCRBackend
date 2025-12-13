from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import easyocr
import numpy as np
import cv2

app = FastAPI(title="Gujarati OCR API")

reader = easyocr.Reader(['gu'])

@app.get("/")
def root():
    return {"status": "Gujarati OCR Backend Running"}

@app.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    result = reader.readtext(img, detail=0)
    text = " ".join(result)

    return JSONResponse({"text": text})
