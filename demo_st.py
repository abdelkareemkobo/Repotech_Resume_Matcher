import streamlit as st
import PyPDF2
import spacy

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text

# Function for NLP preprocessing
def preprocess_text(text):
    nlp = spacy.load("en_core_web_sm")  # Load English NLP model
    doc = nlp(text)
    processed_text = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return processed_text

# Streamlit UI
st.title("PDF File Upload and NLP Preprocessing")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.subheader("Original Text from PDF")
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.text(pdf_text)

    st.subheader("Processed Text (NLP Preprocessing)")
    processed_text = preprocess_text(pdf_text)
    st.text(processed_text)
