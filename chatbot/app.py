from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv  import load_dotenv

###os.environ["OPEN_API_KEY"]=os.getenv("OPEN_API_KEY")###
#Langsmith Tracking 
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##PRompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant ,Please response to the queries")
        ("user","Questions:{question}")

    ]
)


#streamlit framework

st.title("Langchain demo with openapi")
input_text=st.text_input("search the topic you want")


#OPenAI LLm
llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()

chain= prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))