import streamlit as st
import os
import openai
import pdfplumber

import time

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai(prompt):
    retries = 5
    for i in range(retries):
        try:
            response = openai.chat.completions.create(model='chatgpt-4o-latest',
                                                      messages=[
                                                          {"role": "system", "content": "You are a helpful assistant."},
                                                          {"role": "user", "content": prompt}
                                                      ],
                                                      temperature=0.7,max_tokens=2000)
            return response.choices[0].message.content.strip()
        except openai.error.RateLimitError as ex:
            wait_time = 2 ** i
            st.warning(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except Exception as ex:
            st.error(f"An error occurred: {ex}")
            break

st.title("PDF Chat Bot")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    st.text_area("PDF Content", text, height=300)

    question = st.text_area("Ask a question about the PDF content", height=100)

    if st.button("Ask"):
        if question:
            response = query_openai(question)
            st.text_area("Response", response, height=300)
        else:
            st.warning("Please enter a question.")
    else:
        st.warning("Please upload a PDF file and ask a question.")