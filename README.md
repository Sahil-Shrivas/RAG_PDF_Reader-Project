# 📚 RAG PDF Reader Project

An advanced **Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents and interact with them using **semantic search**, **vector embeddings**, and **Mistral AI-powered responses** 🤖

This project combines the capabilities of **Large Language Models (LLMs)** with **document retrieval systems** to provide accurate, context-aware answers directly from uploaded PDF documents.

---

# 🔗 GitHub Repository

:contentReference[oaicite:0]{index=0}

---

# 📖 Introduction

Traditional AI chatbots rely only on pretrained knowledge and cannot understand custom documents uploaded by users. This project solves that limitation using the **RAG (Retrieval-Augmented Generation)** architecture.

The application extracts text from PDF documents, converts the text into vector embeddings, stores them inside a vector database, retrieves relevant chunks using semantic similarity search, and generates intelligent responses using **Mistral LLM**.

This creates a powerful AI system capable of understanding and answering questions directly from uploaded PDFs.

---

# 🚀 Features

## 📄 PDF Upload & Processing
- Upload PDF files directly through the Streamlit interface
- Extract text from single or multiple pages
- Process large documents efficiently

## ✂️ Smart Text Chunking
- Splits long documents into manageable chunks
- Maintains semantic context between chunks
- Improves retrieval accuracy

## 🧠 Semantic Search
- Uses embedding-based retrieval
- Finds contextually relevant information
- Better than traditional keyword search

## 🤖 AI-Powered Responses
- Integrates Mistral Large Language Model
- Generates intelligent and human-like responses
- Uses retrieved context to reduce hallucinations

## 🗂️ Vector Database Integration
- Stores embeddings using ChromaDB
- Enables fast retrieval operations
- Persistent local storage support

## ⚡ Fast & Efficient Pipeline
- Optimized retrieval process
- Low response latency
- Efficient document querying

## 🎨 Interactive Streamlit UI
- Clean and responsive user interface
- Easy PDF upload functionality
- Real-time chatbot interaction

## 🔍 Context-Aware Question Answering
- Answers generated directly from uploaded documents
- Accurate responses based on PDF content
- Suitable for educational and enterprise use cases

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| Streamlit | Frontend web framework |
| LangChain | LLM orchestration |
| Mistral AI | Large Language Model |
| HuggingFace Embeddings | Semantic embedding generation |
| ChromaDB | Vector database |
| PyPDFLoader | PDF text extraction |
| Sentence Transformers | Embedding models |

---

# 🏗️ System Architecture

```text
                ┌──────────────────┐
                │   Upload PDF     │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Text Extraction  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │  Text Chunking   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Generate Embeds  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Store in Chroma  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Semantic Search  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │  Mistral AI LLM  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Final Response   │
                └──────────────────┘
```

---

# 📂 Project Structure

```bash
RAG_PDF_Reader-Project/
│
├── Screenshots/
│   ├── RAG1.png
│   ├── RAG2.png
│   ├── Screenshot1.png
│   ├── Screenshot2.png
│   ├── Screenshot3.png
│   └── Screenshot4.png
│
├── document loaders/
│
├── retrievers/
│
├── vector store/
│
├── .gitignore
├── README.md
├── app.py
├── create_database.py
├── main.py
└── requirements.txt
```

---

# 📸 Project Screenshots

## 🏠 Complete Project Structure

![Project Structure](Screenshots/Screenshot1.png)

---

## 🤖 RAG PDF Reader Interface

![RAG Interface](Screenshots/RAG1.png)

---

## 📄 PDF Upload & Question Answering

![PDF Chatbot](Screenshots/RAG2.png)

---

## ⚡ Semantic Search Working

![Semantic Search](Screenshots/Screenshot2.png)

---

## 🧠 AI Response Generation

![AI Response](Screenshots/Screenshot3.png)

---

## 🎨 Streamlit Application UI

![Application UI](Screenshots/Screenshot4.png)

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sahil-Shrivas/RAG_PDF_Reader-Project.git
cd RAG_PDF_Reader-Project
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside the root directory and add your Mistral API key:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

# ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, open the local Streamlit URL in your browser.

---

# 🧠 How RAG Works

## Step 1 — Upload PDF
The user uploads a PDF document through the Streamlit interface.

## Step 2 — Extract Text
The application extracts textual content from all pages.

## Step 3 — Text Chunking
Large text is divided into smaller chunks for efficient retrieval.

## Step 4 — Embedding Generation
Each chunk is converted into vector embeddings using HuggingFace models.

## Step 5 — Store in Vector Database
Embeddings are stored inside ChromaDB.

## Step 6 — User Query
The user asks a question related to the uploaded PDF.

## Step 7 — Semantic Retrieval
Relevant chunks are retrieved using similarity search.

## Step 8 — AI Response Generation
Retrieved chunks are passed to Mistral AI for generating final answers.

---

# 📊 Advantages of RAG Architecture

- Improves response accuracy
- Reduces hallucinations
- Supports document-specific QA
- Enables semantic understanding
- Dynamically retrieves external knowledge
- Better than traditional chatbots

---

# 🔥 Real-World Use Cases

## 📚 Educational Assistant
Students can upload notes and ask questions directly from study material.

## 🏢 Enterprise Knowledge Base
Organizations can create internal AI document assistants.

## ⚖️ Legal Document Analysis
Retrieve clauses and summaries from legal PDFs.

## 🩺 Medical Research Assistant
Analyze research papers and medical documents.

## 📑 Research Paper Chatbot
Interact with scientific papers using natural language.

---

# 🌟 Future Improvements

- ✅ Multi-PDF support
- ✅ Conversation memory
- ✅ Source citation support
- ✅ Hybrid Search (BM25 + Vector Search)
- ✅ OCR support for scanned PDFs
- ✅ Authentication system
- ✅ Cloud deployment
- ✅ Docker support
- ✅ Multi-language support
- ✅ Voice assistant integration

---

# 📈 Performance Optimizations

- Efficient chunk overlap strategy
- Faster embedding retrieval
- Optimized vector similarity search
- Lightweight Streamlit frontend
- Persistent vector storage

---

# 🔒 Security Features

- API keys secured using `.env`
- Local vector database storage
- Secure file handling
- No permanent query storage

---

# 🧪 Example Questions

Users can ask:

```text
What is the summary of this document?
Explain chapter 3.
What are the key findings?
Give important points from the PDF.
Summarize the conclusion section.
```

---

# 🤝 Contributing

Contributions are welcome!

## Steps to Contribute

### 1️⃣ Fork the Repository

### 2️⃣ Create a Feature Branch

```bash
git checkout -b feature-name
```

### 3️⃣ Commit Your Changes

```bash
git commit -m "Added new feature"
```

### 4️⃣ Push to GitHub

```bash
git push origin feature-name
```

### 5️⃣ Open Pull Request

---

# 🐛 Bug Reporting

If you discover any bug or issue, feel free to open an issue in the repository.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🙌 Acknowledgements

Special thanks to:

- LangChain
- HuggingFace
- Mistral AI
- ChromaDB
- Streamlit

for providing powerful open-source tools and frameworks.

---

# 👨‍💻 Author

## Sahil Shrivas

Passionate about:
- Generative AI
- NLP
- Machine Learning
- RAG Systems
- Large Language Models
- AI-powered applications

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others  

---

# 📬 Contact

📧 GitHub Profile:  
:contentReference[oaicite:1]{index=1}

---

# 💡 Final Note

This project demonstrates how modern AI systems can combine:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Large Language Models
- Embedding-based Retrieval

to create intelligent document-aware AI applications capable of understanding and answering questions from uploaded PDFs in real time.
