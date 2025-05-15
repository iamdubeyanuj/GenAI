import pdfplumber
import os
import requests
import time
import openai
from openai import OpenAIError

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai(prompt):
    retries = 5
    for i in range(retries):
        try:
            response = openai.chat.completions.create(
                model='gpt-4o-latest',
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content.strip()
        except OpenAIError as ex:
            wait_time = 2 ** i
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except Exception as ex:
            print(f"An error occurred: {ex}")
            break
    return "An Error Occured"

def retrieve_external_info(query):
    try:
        search_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        response = requests.get(search_url)
        response.raise_for_status()
        external_info = response.json().get('extract',"No relevent external information found.")
        return external_info
    except requests.RequestException as e:
        print(f"Error retrieving external information: {e}")
        return "No relevent external information found."
    
def process_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def main():
    file_path = input("Enter the path to your PDF file: ")
    pdf_text = process_pdf(file_path)
    print("Extracted Text (first 500 characters):")
    print(pdf_text[:500])

    question = input("Ask a question: ")

    # Retrieve external information
    external_info = retrieve_external_info(question)
    print(f"External Information: {external_info}")

    # Combine PDF content and external info
    if "Failed to retrieve external information" in external_info:
        combined_context = f"Document: {pdf_text[:1000]}\n\nQuestion: {question}\nAnswer:"
    else:
        combined_context = f"Document: {pdf_text[:500]}\n\nExternal Information: {external_info[:500]}\n\nQuestion: {question}\nAnswer:"

    # Query OpenAI
    response = query_openai(combined_context)
    print(f"Answer: {response}")

if __name__ == "__main__":
    main()
    question = "What is the main topic of the document?"
    response = query_openai(question)
    print("Response from OpenAI:")
    print(response)

    external_info = retrieve_external_info("Python_(programming_language)")
    print("External Information:")
    print(external_info)