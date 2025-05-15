import os
import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    st.markdown("<h1 style='text-align: center;'>LLM Blog Generator</h1>", unsafe_allow_html=True)
    st.sidebar.info("An AI Tool to Generate Blog Posts")
    st.sidebar.info("Starts with the first option\n before you proceed to text")

    op = st.sidebar.selectbox("Select an option", ["Topic", "Section","Content"])

    if op == "Topic":
        topics()
    elif op == "Section":
        sections()
    elif op == "Content":
        content()

def BlogTopics(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7)

    return response.choices[0].message.content.strip()

def topics():
    st.info("To generate a blog topic, please enter a keyword or phrase.")
    prompt = st.text_area("Write your words",height=100,value="Generate blog topics on python data science")
    if st.button("Send"):
        st.text(BlogTopics(prompt))


def BlogSections(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7)

    return response.choices[0].message.content.strip()

def sections():
    st.info("To generate a blog section, please enter a keyword or phrase.")
    prompt = st.text_area("Write your words",height=100,value="Generate blog sections on python data science")
    if st.button("Send"):
        st.text(BlogSections(prompt))

def BlogContent(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7)

    return response.choices[0].message.content.strip()

def content():
    st.info("To generate blog content, please enter a keyword or phrase.")
    prompt = st.text_area("Write your words",height=100,value="Generate blog content on python data science")
    if st.button("Send"):
        st.text(BlogContent(prompt))

if __name__ == "__main__":
    main()