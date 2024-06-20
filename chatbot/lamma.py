from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os 
from dotenv  import load_dotenv

load_dotenv()

#Langsmith Tracking 
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##PRompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant ,Please response to the queries"),
        ("user","Questions:{question}")

    ]
)


#streamlit framework

st.title("CHAT with LAMMA2 bot")
input_text=st.text_input("search the topic you want")


#Ollama Llama2 LLm
llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain= prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))