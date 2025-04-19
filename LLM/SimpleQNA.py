import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

def load_answer(question):
    llm = ChatOpenAI(model = "gpt-4.1",temperature=0)
    answer = llm([HumanMessage(content = question)])
    return answer.content

st.set_page_config(page_title="LangChain Demo",page_icon=":robot:")
st.header("LangChain Demo")

def get_text():
    input_text = st.text_input("You: ",key="input")
    return input_text

user_input = get_text()
submit = st.button("Generate")

if submit and user_input:
    response = load_answer(user_input)
    st.subheader("Answer: ")
    st.write(response)