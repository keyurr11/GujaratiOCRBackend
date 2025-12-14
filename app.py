import streamlit as st
import pytesseract
from PIL import Image
import tempfile
import os

st.set_page_config(page_title="Gujarati OCR", layout="centered")

st.title("📄 Gujarati OCR App")
st.write("Upload an image and extract Gujarati text")

# Upload image
uploaded_file = st.file_uploader(
    "Upload Gujarati Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        image_path = tmp.name

    image = Image.open(image_path)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.subheader("📝 Extracted Text")

    try:
        text = pytesseract.image_to_string(image, lang="guj")
        st.text_area("Gujarati Text", text, height=250)
    except Exception as e:
        st.error(f"OCR failed: {e}")

    os.remove(image_path)
