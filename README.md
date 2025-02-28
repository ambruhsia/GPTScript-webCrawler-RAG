# GPTScript Documentation Crawler & RAG Agent

An advanced documentation crawler and RAG agent powered by Pydantic AI and Supabase. It crawls documentation sites, stores content in a vector database, and intelligently retrieves and analyzes relevant information to answer user queries.

## Features
- 🚀 **Automated Documentation Crawling**: Fetches and chunks documentation content.
- 📚 **Vector Database Storage**: Uses **Supabase** for scalable and efficient document retrieval.
- 🔍 **Semantic Search with OpenAI Embeddings**: Enables intelligent documentation lookup.
- 🤖 **RAG-based Q&A System**: Retrieves and generates answers from stored documentation.
- 💾 **Preserves Code Blocks & Content Structure**: Keeps formatting intact.
- 🎨 **Modern UI with Streamlit**: Interactive querying experience.

---

## Prerequisites
- Python **3.11+**
- **Supabase** account & database
- **OpenAI API Key**
- **Streamlit** (for UI-based querying)

---

## Installation

Clone the repository 

Create a virtual environment and install dependencies:
```sh
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Setup

### Set up .env 

### Database Configuration
Run the SQL script to create the required tables:
1. Navigate to Supabase's **SQL Editor**.
2. Paste and execute the contents of `site_pages.sql`.
3. This will:
   - Create necessary tables.
   - Enable **vector similarity search**. 

 

---

## Usage

### Crawling Documentation
To fetch and store documentation:
```sh
python crawl_gptscript_docs.py
```
- Crawls the documentation website.
- Chunks content while preserving **code blocks and paragraph boundaries**.
- Generates **embeddings** and stores them in Supabase.

### Querying via Streamlit UI
To launch the interactive UI:
```sh
streamlit run streamlit_ui.py
```
![Screenshot 2025-03-01 032615](https://github.com/user-attachments/assets/02854c85-cafc-462e-b4d0-be6141e3be1a)


---

## Credits & Reference
This project is adapted from **[ottomator-agents](https://github.com/coleam00/ottomator-agents/tree/main/crawl4AI-agent)**. A huge thanks to the original developers for their contributions to the documentation crawling and RAG agent framework.

---
