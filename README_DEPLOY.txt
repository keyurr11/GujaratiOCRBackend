GujaratiOCRBackend - Ready-to-deploy FastAPI backend for Gujarati OCR (EasyOCR)

Files included:
- app.py           : FastAPI application exposing POST /ocr
- requirements.txt : Python packages required
- runtime.txt      : Python runtime (for some hosts)

Deployment notes:
- This project uses EasyOCR which downloads models on first run and may take some time.
- If deploying to Render or Railway, create a new service and point it to this repository.
- Render: create a new web service from a public GitHub repo or ZIP; build command: 'pip install -r requirements.txt', start command: 'uvicorn app:app --host 0.0.0.0 --port $PORT'
- Railway: similar; ensure GPU is not required (we used gpu=False).
- If you prefer Tesseract instead, I can provide an alternate Dockerfile and app.py.
