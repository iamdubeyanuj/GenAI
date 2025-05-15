import os
import openai
import pandas as pd

from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

df = pd.read_csv('Insurance+Data+Analysis+Dataset.csv')
df.head(5)

agent = create_csv_agent(
    OpenAI(temperature=0),'Insurance+Data+Analysis+Dataset.csv',verbose=True,allowdangerous_code=True
)

responses = [
    agent.run('how many records are there'),
    agent.run('how many females are there'),
    agent.run('how many records are there with bmi value greater than 30'),
    agent.run('how many obese people are there in the dataset')
]
for response in responses:
    print(response)