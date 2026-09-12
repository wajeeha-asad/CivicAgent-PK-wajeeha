# CivicAgent PK 🇵🇰

> An AI-powered civic assistance prototype that uses **Groq/Llama + ChromaDB + Retrieval-Augmented Generation (RAG)** to analyze citizen complaints against a searchable policy knowledge base.

**Project type:** Hackathon project  
**Current status:** Prototype / active development  
**Primary focus:** AI Engineering · RAG · LLM Applications · Python

---

## Overview

CivicAgent PK is being developed as a civic-tech AI system designed to help citizens understand how a reported issue relates to available civic policies and what action may be appropriate.

The current implementation combines:

- **Groq API** for Llama-based language generation
- **ChromaDB** for local vector storage and semantic retrieval
- **RAG** to ground LLM responses in retrieved policy context
- **Structured JSON responses** for downstream application integration
- A modular Python architecture separating ingestion, retrieval, prompting, and generation

The repository currently contains my independently maintained implementation of the completed hackathon tasks. The final team repository may contain additional components contributed by other team members.

> **Important:** The policy records currently included in `data/civic_policies.json` are prototype/sample records for development and testing. They should not be treated as official legal or government guidance. They will be replaced or expanded with verified project data as it becomes available.

---

## Architecture

```text
Citizen Complaint
       │
       ▼
Policy Knowledge Base
(data/civic_policies.json)
       │
       ▼
ChromaDB Vector Store
       │
       ▼
Semantic Retrieval
(top-k relevant policies)
       │
       ▼
RAG Prompt Construction
       │
       ▼
Groq API → Llama
       │
       ▼
Structured AI Analysis
       │
       ▼
CivicAgent Response
```

---

## Current Features

### 1. Groq / Llama Integration

- Loads credentials securely from `.env`
- Configurable Groq model
- System + user prompt architecture
- Low-temperature generation for more consistent responses
- Structured JSON response parsing

### 2. Policy Knowledge Base

- Policy records stored as JSON
- Metadata for title, category, authority, source type, and source
- Designed to be replaced with verified project policy data

### 3. ChromaDB Retrieval

- Persistent local ChromaDB collection
- Semantic search over civic policy documents
- Configurable `top_k` retrieval
- Returns policy metadata, document text, IDs, and retrieval distances

### 4. RAG Pipeline

The main pipeline follows:

```text
Complaint
   ↓
Retrieve relevant policies
   ↓
Build grounded prompt
   ↓
Generate structured LLM response
   ↓
Validate grounding status
   ↓
Return analysis + retrieved policies
```

The response includes a grounding status such as:

- `supported`
- `partially_supported`
- `insufficient`

This helps distinguish between answers supported by the retrieved context and cases where the available policy evidence is insufficient.

---

## Project Structure

```text
CivicAgent-PK-wajeeha/
│
├── data/
│   ├── civic_policies.json       # Prototype policy knowledge base
│   └── README.md
│
├── rag/
│   ├── __init__.py
│   ├── api.py                    # Public RAG entry point
│   ├── chroma_service.py         # ChromaDB client/collection
│   ├── groq_service.py           # Groq/Llama integration
│   ├── prompts.py                # LLM and RAG prompts
│   ├── rag_service.py            # End-to-end RAG pipeline
│   └── retriever.py              # Policy retrieval
│
├── ingest_policies.py            # Load policies into ChromaDB
├── test_groq.py                  # Groq integration test
├── test_retrieval.py             # Retrieval test
├── test_rag_retrieval.py         # RAG retrieval test
├── test_rag.py                   # End-to-end RAG test
├── test_api.py                   # API-level test
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core implementation |
| Groq API | LLM inference |
| Llama | Language model |
| ChromaDB | Vector database / semantic retrieval |
| python-dotenv | Environment configuration |
| RAG | Grounding LLM responses in retrieved context |
| JSON | Prototype policy data format |

---

## Setup

### 1. Clone the repository

```powershell
git clone https://github.com/wajeeha-asad/CivicAgent-PK-wajeeha.git
cd CivicAgent-PK-wajeeha
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` from `.env.example`:

```powershell
Copy-Item .env.example .env
```

Then add your own Groq API key to `.env`.

**Never commit `.env` or expose API keys publicly.**

### 5. Ingest the policy data

```powershell
python ingest_policies.py
```

This creates the local ChromaDB data under `chroma_db/`.

### 6. Test the RAG pipeline

```powershell
python test_rag.py
```

You can also run the individual retrieval/API tests:

```powershell
python test_retrieval.py
python test_rag_retrieval.py
python test_api.py
```

---

## Example Pipeline Input

```text
There has been a problem with the water supply in our area.
```

The system retrieves relevant policy records from ChromaDB and passes the retrieved context to Llama through a grounded RAG prompt. The resulting structured response contains the AI analysis together with the policies used as context.

---

## Security

- API credentials are loaded from environment variables.
- `.env` is excluded through `.gitignore`.
- Local ChromaDB data is excluded from version control.
- No API keys or secrets should be committed to this repository.

---

## Development Status

This project is under active hackathon development.

Current milestone:

- [x] Groq API foundation
- [x] ChromaDB policy storage
- [x] Semantic policy retrieval
- [x] RAG pipeline
- [x] Structured AI response generation
- [ ] Integration with the complete team application
- [ ] Replace prototype policy records with verified project data
- [ ] Production deployment

---

## Team / Collaboration Note

This repository is a personal development repository containing my implementation and working history for the CivicAgent PK hackathon project. The final team repository will serve as the consolidated project repository after team integration.

---

## Disclaimer

CivicAgent PK is a hackathon prototype for educational and technical demonstration purposes. It is **not a substitute for official government, legal, or emergency guidance**. Always verify civic or legal information through the relevant official authority.

---

## Author

**Wajeeha Asad**  
Computer Science Student · AI Engineer & Full-Stack Developer

- GitHub: [@wajeeha-asad](https://github.com/wajeeha-asad)
- LinkedIn: [Wajeeha Asad](https://www.linkedin.com/in/wajeehaasad/)
