import os
import streamlit as st
from langchain_openai import ChatOpenAI
from constant import api_key, base_url
from langchain.prompts import PromptTemplate

# Set up API credentials
os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_BASE_URL"] = base_url

# Streamlit UI
st.title("Sportsperson Info Finder")
input_text = st.text_input("Enter a Sportsperson's Name:")

# Initialize LLM
llm = ChatOpenAI(
    model="deepseek/deepseek-r1:free",
    temperature=0.8
)

# Check if input is a sportsperson
check_prompt = PromptTemplate(
    input_variables=["name"],
    template="Is {name} a famous sportsperson? Answer only yes or no."
)

check_chain = check_prompt | llm

# Prompt to get info
info_prompt = PromptTemplate(
    input_variables=["name"],
    template="Tell me about the sportsperson {name}."
)
info_chain = info_prompt | llm

# Final logic
if input_text:
    check_response = check_chain.invoke({"name": input_text})
    if "yes" in check_response.content.lower():
        info_response = info_chain.invoke({"name": input_text})
        st.write(info_response.content)
    else:
        st.write("Please enter the name of a sportsperson only.")
