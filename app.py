import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(
    page_title="Gujarati OCR App",
    page_icon="📄",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: white;
}
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 30px;
}
.stButton>button {
    background-color: #22c55e;
    color: black;
    font-size: 18px;
    padding: 10px;
    width: 100%;
    border-radius: 8px;
}
textarea {
    background-color: #1f2937 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='title'>Gujarati OCR App</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload an image and extract Gujarati text</div>", unsafe_allow_html=True)

# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader(
    "Upload Gujarati Image",
    type=["png", "jpg", "jpeg"]
)

# ---------- OCR ----------
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Extracting text..."):
        text = pytesseract.image_to_string(image, lang="guj")

    st.success("Text extracted successfully!")

    st.text_area("Detected Text", text, height=200)

    if st.button("Copy Text"):
        st.write("✔ Text copied (use Ctrl + C)")

