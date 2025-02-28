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

### Environment Variables 

### Database Configuration
Run the SQL script to create the required tables:
1. Navigate to Supabase's **SQL Editor**.
2. Paste and execute the contents of `site_pages.sql`.
3. This will:
   - Create necessary tables.
   - Enable **vector similarity search**.
   - Apply row-level security (RLS) policies.

#### Table Schema:
```sql
CREATE TABLE site_pages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    url TEXT,
    chunk_number INTEGER,
    title TEXT,
    summary TEXT,
    content TEXT,
    metadata JSONB,
    embedding VECTOR(1536)
);
```

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
- The interface will be available at [http://localhost:8501](http://localhost:8501).

---

## Project Structure
- **`crawl_gptscript_docs.py`** → Documentation crawler and processor.
- **`gptscript_expert.py`** → RAG agent implementation.
- **`streamlit_ui.py`** → Interactive UI for querying.
- **`site_pages.sql`** → Supabase database setup commands.
- **`requirements.txt`** → Project dependencies.

---

## Credits & Reference
This project is adapted from **[ottomator-agents](https://github.com/coleam00/ottomator-agents/tree/main/crawl4AI-agent)**. A huge thanks to the original developers for their contributions to the documentation crawling and RAG agent framework.

---
