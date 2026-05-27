# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# from langchain_core.documents import Document

# docs = [
#     Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
#     Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
#     Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
# ]

# embedding_model = OpenAIEmbeddings()

# vectorstore = Chroma.from_documents(
#     documents = docs,
#     embedding= embedding_model,
#     persist_directory= "chroma-db"
# )

# result = vectorstore.similarity_search("what is used for data analysis?",k=2)

# for r in result:
#     print(r.page_content)
#     print(r.metadata)

# retriver = vectorstore.as_retriever()

# docs = retriver.invoke("Explain deep learning")

# for d in docs:
#     print(d.page_content)
















# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

from langchain_core.documents import Document

docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

# ✅ FREE embeddings (NO API KEY)
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma-db"
)

# Similarity search
result = vectorstore.similarity_search(
    "what is used for data analysis?", k=2
)

for r in result:
    print(r.page_content)
    print(r.metadata)

# Retriever
retriever = vectorstore.as_retriever()

docs = retriever.invoke("Explain deep learning")

for d in docs:
    print(d.page_content)