## Data Ingestion
from langchain_community.document_loaders import TextLoader
loader=TextLoader(r"C:\Users\adnan\LangChain\rag\speech.txt")
text_documents=loader.load()
text_documents
#print(text_documents)


import os
from dotenv import load_dotenv 
load_dotenv()


os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')


#data ingestion method 2 (web based  loader)

from langchain_community.document_loaders import WebBaseLoader
import bs4

#load,chunk and index the content of the html page 
loader = WebBaseLoader(web_path="https://lilianweng.github.io/posts/2023-06-23-agent/",
                       bs_kwargs=dict(parse_only = bs4.SoupStrainer(
                           class_=("post-title","post-content","post-header")
                       )),)

text_documents=loader.load()
print(text_documents)


#data ingestion method 3 (through pdf)
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(r'C:\Users\adnan\LangChain\rag\attention.pdf')
docs = loader.load()
print(docs)

#converting docs into chunks 
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 100,chunk_overlap = 100)
pdf_docs = text_splitter.split_documents(docs)
print(pdf_docs[:5])


#converting it into vectors
#vector embeddings and vector store 
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(pdf_docs[:15],OllamaEmbeddings())

# Chroma vector database
query = "who are the authors of the attention is all you need research paper"
result = db.similarity_search(query)
print(result[0].page_content)


#FAiss vector database 
from langchain_community.vectorstores import FAISS
db1 = FAISS.from_documents(pdf_docs[:5],OllamaEmbeddings())

query1 = "what is attention is all about?"
result1 = db1.similarity_search(query1)
print(result1[0].page_content)


#LanceDB vector database
from langchain_community.vectorstores import LanceDB
db2 = LanceDB.from_documents(pdf_docs[:15],OllamaEmbeddings())

query2 = "what is the reasearch based on ?"
result2=db2.similarity_search_with_score(query2)
print(result2[0].page_content)












