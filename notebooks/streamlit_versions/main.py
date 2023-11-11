import streamlit as st
from pypdf import PdfReader
from io import BytesIO
from scripts.KeytermsExtraction import KeytermExtractor
from scripts.Extractor import DataExtractor
from scripts.TextCleaner import TextCleaner
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import cohere

st.title("ATS Helper")
st.write(
    "Add your Resume and the job application you want to use, then get the keyword which will increase the similiarty score to be able to paybass the ATS systems with the power of AI generaion power"
)


def read_single_pdf(file_content):
    output = []
    try:
        pdf_stream = BytesIO(file_content.read())
        pdf_reader = PdfReader(pdf_stream)
        count = len(pdf_reader.pages)
        for i in range(count):
            page = pdf_reader.pages[i]
            output.append(page.extract_text())
    except Exception as e:
        print(f"Error reading file '{file_content}': {str(e)}")
    return str(" ".join(output))


uploaded_resume = st.file_uploader("Choose a Resume  PDF file", type=["pdf"])
if uploaded_resume:
    resume_text = read_single_pdf(uploaded_resume)
    print(resume_text)
    st.subheader("Resume Content: ")
    # st.write(resume_text)
else:
    resume_text = st.text_input("Enter the Resume content: ")
    # st.write(resume_text)


uploaded_job_desc = st.file_uploader("Choose Job Description File", type=["pdf"])
if uploaded_job_desc:
    job_desc = read_single_pdf(uploaded_job_desc)
    print(job_desc)
    st.subheader("Job description  Content: ")
    # st.write(job_desc)
else:
    job_desc = st.text_input("Job description  Content: ")
    # st.write(job_desc)

cleaned_resume = TextCleaner(resume_text).clean_text()
resume_keywords = DataExtractor(cleaned_resume).extract_particular_words()
# st.write(cleaned_resume)

cleaned_job_desc = TextCleaner(job_desc).clean_text()
job_desc_keyterms = KeytermExtractor(cleaned_job_desc).get_keyterms_based_on_sgrank()
# st.write(cleaned_job_desc)

# tfidf_vectorizer = TfidfVectorizer()
# tfidf_matrix = tfidf_vectorizer.fit_transform([resume_text, job_desc])
# cosine_sim = cosine_similarity(tfidf_matrix[0],tfidf_matrix[1])
# similarity = cosine_sim[0,0]
# st.write("Similarity Score before updates: {:.2f}".format(similarity))


prompt = f"""
        Suggest keywords or phrases from the following {cleaned_job_desc} to add into my resume {resume_keywords} to increase the cosine similarity and be pass the ATS resume checking. use both long-form and acronym version of keywords(e.g \"Master of Business Administration (MBA)\" or \"Search Engine Optimization(SEO)\") for maximum searchability.
        give me the keywords Make sure you to only return the keywords and say nothing else. For example, don't say:
"Here are the keywords present in the document"
        """
# st.write(job_desc_keyterms)
# st.write("****")
# st.write(resume_keywords)
#! Replace this with your cohere api key 
co = cohere.Client("your_cohere_api_key")
response = co.generate(
    model="command",
    prompt=prompt,
    max_tokens=500,
    temperature=0.9,
    k=1,
    stop_sequences=[],
    return_likelihoods="NONE",
)
# # st.write("Keywords to Add: {}".format(response.generations[0].text))
keywords = response.generations[0].text
st.write(keywords)
# keyword_list = keywords.split(", ")
# st.write("Keywords to Add:")
# for keyword in keyword_list:
    # st.write(f"• {keyword}")

# new_documnt = resume_text + keywords.replace("\n"," ") 
# new_documnt = TextCleaner(new_documnt).clean_text()
# st.write("****")
# tfidf_vectorizer = TfidfVectorizer()
# tfidf_matrix = tfidf_vectorizer.fit_transform([new_documnt, job_desc])
# cosine_sim = cosine_similarity(tfidf_matrix[0],tfidf_matrix[1])
# similarity = cosine_sim[0,0]
# st.write("Similarity Score: {:.2f}".format(similarity))
# st.subheader("We recommend having the exact title of the job for which you're applying in your resume.")







