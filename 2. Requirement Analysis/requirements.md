# 2. Requirement Analysis

## Functional Requirements
| ID | Requirement | Module |
|----|-------------|--------|
| FR1 | User can request an explanation of any concept at a chosen level | Explanation Module |
| FR2 | User can ask a free-form question and receive an accurate answer with context | Q&A Module |
| FR3 | User can request an auto-generated multiple-choice quiz on a topic | Quiz Generation Module |
| FR4 | User can paste text and receive a concise bullet-point summary | Summarization Module |
| FR5 | User can request a structured beginner → advanced learning roadmap for a subject | Learning Path Module |
| FR6 | Frontend displays results returned by the backend clearly, per module | Frontend |
| FR7 | Backend routes each request to the correct module based on user selection | FastAPI Backend |

## Non-Functional Requirements
- **Performance:** Responses should return within a few seconds under normal network
  conditions (dependent on Gemini API latency).
- **Usability:** Interactive, single-page interface; no login required for the MVP.
- **Portability:** Must run on Windows, Linux, and macOS, including resource-constrained
  devices such as a Mac M1 (4GB+ RAM).
- **Maintainability:** Each capability is isolated into its own backend module so features
  can be extended independently.
- **Security:** Gemini API key is never hard-coded — stored in a local `.env` file only.

## Skills / Technologies Required
Python (Programming Language) · FastAPI · Generative Artificial Intelligence ·
Natural Language Processing (NLP) · HTML Editor · Prompt Engineering ·
HTML Application · CSS Animations · Google Gemini API · AI/ML Inference

## Hardware Requirements
- Processor: Intel i3/i5 or higher
- RAM: Minimum 4GB (8GB recommended)
- Storage: 10GB free disk space
- Internet connection required (Gemini API calls)

## Software Requirements
- OS: Windows / Linux / macOS
- Python 3.10+
- FastAPI
- Database: SQL / PostgreSQL / SQLite (optional, for future history/logging features)
- Google Gemini API key
- Git & GitHub
- Visual Studio Code / PyCharm

## Out of Scope (MVP)
- User accounts / authentication
- Persisting quiz history or chat history to a database
- Mobile native app (web app only)
