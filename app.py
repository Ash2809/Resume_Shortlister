from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import PyPDF2 as pdf
import os
import streamlit as st

st.title("----RESUME EVALUATER---")
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",temperature = 0)

def pdf_to_text(path):
    reader=pdf.PdfReader(path)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


description = st.text_input("Enter the job description here")

resume = st.file_uploader("Upload your resume")

button_ats = st.button("Check ATS score")
button_help = st.button("Improve your resume")

if button_ats:
    text = pdf_to_text(resume)

    prompt1 = f"""You are a a skilled or very experience ATS(Application Tracking System)
    with a deep understanding of tech field,software engineering,data science ,data analyst
    and big data engineer. Your task is to read the resume and rate it in terms of percentage of keywords 
    matching in the gievn job decription. Description{description} .Resume{text}.answer in terms of percentage only"""

    response = llm.invoke(prompt1).content
    st.write(response)


if button_help:
    text = pdf_to_text(resume)

    prompt2 = f"""You are a smart ATS(Application Tracking System) with a deep understanding of the job fields.
    Based on the job description provide some helpfull insights the candidate can add in the resume.Do not 
    answer more than asked and answer professionally.resume{text} description:{description}"""

    response = llm.invoke(prompt2).content
    st.write(response)


