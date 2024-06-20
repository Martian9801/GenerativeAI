import os
from dotenv import load_dotenv 
load_dotenv()



#data ingestion method 3 (through pdf)
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(r'C:\Users\adnan\LangChain\rag\attention.pdf')
docs = loader.load()
print(docs)


from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
db=FAISS.from_documents(docs[:30],OllamaEmbeddings())
print(db)

query="An attention function can be described as mapping a query "
result=db.similarity_search(query)
result[0].page_content


from langchain_community.llms import Ollama
llm = Ollama(model="lamma2")
llm

#designing chatprompt template
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("""
Answer the following questions based on only the provided context.
think step by step before providing a detailed answer
i will tip you 100$ if user finds it useful
<context>
{context}
</context>
Question:{input}
""")



#craeting stuff chain documents
from langchain.chains.combine_documents import create_stuff_documents_chain

document_chain = create_stuff_documents_chain(llm,prompt)


#retrievers
#its an interface has a backend to retrive an information from vector store

retriever = db.as_retriever()
retriever()

"""
retrival chain : This chain takes in a user query ,which is then passed to a retiver to fetch relevant documents.those documents
(and the original inputs) are then  passed as LLM to generate a response
"""

#creatinig retiever chain

from langchain.chains import create_retrieval_chain
retrieval_chain = create_retrieval_chain(retriever,document_chain)

response = retrieval_chain.invoke({"input":"An attention function can be described as mapping a query"})

response["answer"]

