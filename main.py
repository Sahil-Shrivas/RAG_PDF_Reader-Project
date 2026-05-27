# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain_mistralai import ChatMistralAI
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()

# embedding_model = OpenAIEmbeddings()

# vectorstore = Chroma(
#     persist_directory= "chroma_db",
#     embedding_function=embedding_model
# )

# retriever = vectorstore.as_retriever(
#     search_type = "mmr",
#     search_kwargs = {
#         "k" : 4,
#         "fetch_k":10,
#         "lambda_mult" :0.5
#     }
# )

# llm = ChatMistralAI(model = "mistral-small-2506")

# #prompt template 
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             """You are a helpful AI assistant.

# Use ONLY the provided context to answer the question.

# If the answer is not present in the context,
# say: "I could not find the answer in the document."
# """
#         ),
#         (
#             "human",
#             """Context:
# {context}

# Question:
# {question}
# """
#         )
#     ]
# )

# print("Rag system created ")

# print("press 0 to exit ")

# while True:
#     query = input("You : ")
#     if query == "0":
#         break 
    
#     docs = retriever.invoke(query)

#     context = "\n\n".join(
#         [doc.page_content for doc in docs]
#     )
    
#     final_prompt = prompt.invoke({
#         "context" :context,
#         "question": query
#     })
    
#     response = llm.invoke(final_prompt)

#     print(f"\n AI: {response.content}")
    



















from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ✅ FREE embeddings (no API key needed)
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load vector DB
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

# ✅ Mistral LLM (uses your API key from .env)
llm = ChatMistralAI(
    model="mistral-small-latest"
)

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: I could not find the answer in the document.
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)

print("RAG system created")
print("Press 0 to exit")

# Chat loop
while True:
    query = input("You: ")

    if query == "0":
        break

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    print(f"\nAI: {response.content}")