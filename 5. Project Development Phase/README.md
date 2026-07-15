# 5. Project Development Phase

This folder contains the actual EduGenie implementation.

```
5. Project Development Phase/
├── backend/
│   ├── main.py                  # FastAPI app + routing (see architecture diagram)
│   ├── requirements.txt
│   ├── .env.example
│   └── modules/
│       ├── gemini_client.py     # shared Gemini API wrapper
│       ├── schemas.py           # Pydantic request models
│       ├── explain.py           # Explanation Module
│       ├── qa.py                # Q&A Module
│       ├── quiz.py              # Quiz Generation Module
│       ├── summarize.py         # Summarization Module
│       └── learning_path.py     # Learning Path Module
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

## Run locally

```bash
cd "5. Project Development Phase/backend"
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then paste your Gemini API key into .env
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** — FastAPI serves the frontend directly, so backend and UI run
from a single command.

## Get a Gemini API key
1. Go to https://aistudio.google.com/app/apikey
2. Create an API key
3. Paste it into `backend/.env` as `GOOGLE_API_KEY=...`
