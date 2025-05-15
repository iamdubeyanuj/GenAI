import os
from langchain_openai import OpenAI

llm = OpenAI(
    model="gpt-4o",
    temperature=0.7,
    max_tokens=2000,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
response = llm.invoke("What is the capital of France?")
print(response)