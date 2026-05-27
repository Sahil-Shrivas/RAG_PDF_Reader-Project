# #load pdf 
# #split into chunks 
# #create the embeddings 
# #store into chroma 
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings 
# from langchain_community.vectorstores import Chroma 
# from dotenv import load_dotenv

# load_dotenv()

# data = PyPDFLoader("document loaders/deeplearning.pdf")
# docs = data.load()

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 1000,
#     chunk_overlap = 200
# )

# chunks = splitter.split_documents(docs)

# embedding_model = OpenAIEmbeddings()

# vectorstore = Chroma.from_documents(
#     documents= chunks,
#     embedding=embedding_model,
#     persist_directory="chroma_db"
# )


















# load pdf 
# split into chunks 
# create embeddings 
# store into chroma 

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma 
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

# Load PDF
data = PyPDFLoader("document loaders/deeplearning.pdf")
docs = data.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

# ✅ FIX: FREE embeddings (no API key)
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Store in Chroma DB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

# Save DB
vectorstore.persist()

print("✅ Vector DB created successfully!")