# import streamlit as st
# from dotenv import load_dotenv
# import tempfile
# import os

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain_mistralai import ChatMistralAI
# from langchain_core.prompts import ChatPromptTemplate


# load_dotenv()

# st.set_page_config(page_title="RAG Book Assistant")

# st.title("📚 RAG Book Assistant")
# st.write("Upload a PDF and ask questions from the document")

# uploaded_file = st.file_uploader("Upload a PDF book", type="pdf")


# if uploaded_file:

#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         tmp_file.write(uploaded_file.read())
#         file_path = tmp_file.name

#     st.success("PDF uploaded successfully!")

#     if st.button("Create Vector Database"):

#         with st.spinner("Processing document..."):

#             loader = PyPDFLoader(file_path)
#             docs = loader.load()

#             splitter = RecursiveCharacterTextSplitter(
#                 chunk_size=1000,
#                 chunk_overlap=200
#             )

#             chunks = splitter.split_documents(docs)

#             embeddings = OpenAIEmbeddings()

#             vectorstore = Chroma.from_documents(
#                 documents=chunks,
#                 embedding=embeddings,
#                 persist_directory="chroma_db"
#             )

#             vectorstore.persist()

#         st.success("Vector database created!")



# if os.path.exists("chroma_db"):

#     embeddings = OpenAIEmbeddings()

#     vectorstore = Chroma(
#         persist_directory="chroma_db",
#         embedding_function=embeddings
#     )

#     retriever = vectorstore.as_retriever(
#         search_type="mmr",
#         search_kwargs={
#             "k":4,
#             "fetch_k":10,
#             "lambda_mult":0.5
#         }
#     )

#     llm = ChatMistralAI(model="mistral-small-2506")

#     prompt = ChatPromptTemplate.from_messages(
#         [
#             (
#                 "system",
#                 """You are a helpful AI assistant.

# Use ONLY the provided context to answer the question.

# If the answer is not present in the context,
# say: "I could not find the answer in the document."
# """
#             ),
#             (
#                 "human",
#                 """Context:
# {context}

# Question:
# {question}
# """
#             )
#         ]
#     )

#     st.divider()
#     st.subheader("Ask Questions From the Book")

#     query = st.text_input("Enter your question")

#     if query:

#         docs = retriever.invoke(query)

#         context = "\n\n".join(
#             [doc.page_content for doc in docs]
#         )

#         final_prompt = prompt.invoke({
#             "context": context,
#             "question": query
#         })

#         response = llm.invoke(final_prompt)

#         st.write("### AI Answer")
#         st.write(response.content)
















# import streamlit as st
# from dotenv import load_dotenv
# import tempfile
# import os

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# # from langchain_community.vectorstores import Chroma
# from langchain_chroma import Chroma
# from langchain_mistralai import ChatMistralAI
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()

# st.set_page_config(page_title="RAG Book Assistant")

# st.title("📚 RAG Book Assistant")
# st.write("Upload a PDF and ask questions from the document")

# uploaded_file = st.file_uploader("Upload a PDF book", type="pdf")

# # ------------------ CREATE VECTOR DB ------------------

# if uploaded_file:

#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         tmp_file.write(uploaded_file.read())
#         file_path = tmp_file.name

#     st.success("PDF uploaded successfully!")

#     if st.button("Create Vector Database"):

#         with st.spinner("Processing document..."):

#             loader = PyPDFLoader(file_path)
#             docs = loader.load()

#             splitter = RecursiveCharacterTextSplitter(
#                 chunk_size=1000,
#                 chunk_overlap=200
#             )

#             chunks = splitter.split_documents(docs)

#             # ✅ FIX: FREE embeddings
#             embeddings = HuggingFaceEmbeddings(
#                 model_name="all-MiniLM-L6-v2"
#             )

#             vectorstore = Chroma.from_documents(
#                 documents=chunks,
#                 embedding=embeddings,
#                 # persist_directory="chroma_db"
#             )

#             # vectorstore.persist()

#         st.success("Vector database created!")

# # ------------------ LOAD + QA ------------------

# if os.path.exists("chroma_db"):

#     embeddings = HuggingFaceEmbeddings(
#         model_name="all-MiniLM-L6-v2"
#     )

#     vectorstore = Chroma(
#         persist_directory="chroma_db",
#         embedding_function=embeddings
#     )

#     retriever = vectorstore.as_retriever(
#         search_type="mmr",
#         search_kwargs={
#             "k": 4,
#             "fetch_k": 10,
#             "lambda_mult": 0.5
#         }
#     )

#     # ✅ Mistral (API key use karega .env se)
#     llm = ChatMistralAI(
#         model="mistral-small-latest"
#     )

#     prompt = ChatPromptTemplate.from_messages(
#         [
#             (
#                 "system",
#                 """You are a helpful AI assistant.
# Use ONLY the provided context to answer the question.
# If the answer is not present, say:
# I could not find the answer in the document."""
#             ),
#             (
#                 "human",
#                 """Context:
# {context}

# Question:
# {question}
# """
#             )
#         ]
#     )

#     st.divider()
#     st.subheader("Ask Questions From the Book")

#     query = st.text_input("Enter your question")

#     if query:

#         docs = retriever.invoke(query)

#         context = "\n\n".join(
#             [doc.page_content for doc in docs]
#         )

#         final_prompt = prompt.invoke({
#             "context": context,
#             "question": query
#         })

#         response = llm.invoke(final_prompt)

#         st.write("### AI Answer")
#         st.write(response.content)





























import streamlit as st
from dotenv import load_dotenv
import tempfile

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# ------------------ STREAMLIT UI ------------------

st.set_page_config(page_title="RAG Book Assistant")

st.title("📚 RAG Book Assistant")
st.write("Upload a PDF and ask questions from the document")

uploaded_file = st.file_uploader(
    "Upload a PDF book",
    type="pdf"
)

# ------------------ MAIN APP ------------------

if uploaded_file:

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("PDF uploaded successfully!")

    # Create vector DB button
    if st.button("Create Vector Database"):

        with st.spinner("Processing document..."):

            # Load PDF
            loader = PyPDFLoader(file_path)
            docs = loader.load()

            # Split text into chunks
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(docs)

            # Free HuggingFace embeddings
            embeddings = HuggingFaceEmbeddings(
                model_name="all-MiniLM-L6-v2"
            )

            # Create vector store
            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings
            )

            # Create retriever
            retriever = vectorstore.as_retriever(
                search_type="mmr",
                search_kwargs={
                    "k": 4,
                    "fetch_k": 10,
                    "lambda_mult": 0.5
                }
            )

            st.success("Vector database created successfully!")

            # Save retriever in session state
            st.session_state.retriever = retriever

# ------------------ QA SECTION ------------------

if "retriever" in st.session_state:

    retriever = st.session_state.retriever

    # Mistral LLM
    llm = ChatMistralAI(
        model="mistral-small-latest",
        api_key=st.secrets["MISTRAL_API_KEY"]
    )

    # Prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful AI assistant.
Use ONLY the provided context to answer the question.
If the answer is not present in the document, say:
'I could not find the answer in the document.'"""
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

    st.divider()
    st.subheader("Ask Questions From the Book")

    query = st.text_input("Enter your question")

    if query:

        with st.spinner("Generating answer..."):

            # Retrieve relevant docs
            docs = retriever.invoke(query)

            # Create context
            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            # Final prompt
            final_prompt = prompt.invoke({
                "context": context,
                "question": query
            })

            # LLM response
            response = llm.invoke(final_prompt)

            # Show answer
            st.write("### AI Answer")
            st.write(response.content)

