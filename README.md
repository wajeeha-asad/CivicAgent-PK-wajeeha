# CivicAgent PK — Task 1: Groq API Foundation

This standalone project is the starting point for Wajeeha's hackathon task.

## Task 1 scope

- Create an isolated Python environment
- Load the Groq API key from `.env`
- Connect to Groq
- Send a system prompt + user complaint to Llama
- Return a clean response
- Keep the code ready for the ChromaDB/RAG work in Tasks 2 and 3

## Current architecture

```text
Citizen complaint
       |
       v
rag/groq_service.py
       |
       v
Groq API -> Llama
       |
       v
CivicAgent response
```

## Safety

- Never commit `.env`.
- Never put the Groq API key directly in Python code.
- Task 1 uses sample prompts only. Real government policies will be added in the RAG task.

## Run

PowerShell:

```powershell
cd path\to\CivicAgent-PK-Task1
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
# Edit .env and add your Groq API key
python test_groq.py
```
