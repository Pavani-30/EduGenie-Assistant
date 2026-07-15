# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant designed to simplify and enhance
the learning experience through the power of Generative AI. Developed for students,
self-learners, and educators, EduGenie provides intelligent educational support by helping
users understand concepts, answer questions, generate quizzes, summarize learning
materials, and receive personalized learning recommendations. The platform aims to make
learning more interactive, accessible, and efficient for users across different academic
levels and subject domains.

Built using **FastAPI** for the backend and a responsive **HTML + CSS** frontend, EduGenie
combines the capabilities of lightweight local models and cloud-based AI services to deliver
fast and accurate educational assistance. Its optimized architecture allows it to run
efficiently on resource-constrained devices such as the Mac M1, making it suitable for both
personal learning and educational projects.

## Key Features
- Intelligent Question Answering
- Simplified Concept Explanations
- AI-Powered Quiz Generation
- Educational Text Summarization
- Personalized Learning Path Recommendations
- Interactive and User-Friendly Interface

## Scenarios
- **Scenario 1:** A student wants to learn about oceans and rivers. They ask "Which is the
  largest ocean?" EduGenie instantly provides an accurate answer along with additional
  educational context.
- **Scenario 2:** A student studying the Pythagoras Theorem wants to assess their
  understanding. They select "Generate Quiz," and EduGenie creates topic-specific questions
  for self-evaluation.
- **Scenario 3:** A learner interested in SQL requests a structured learning roadmap.
  EduGenie generates a personalized learning path covering beginner, intermediate, and
  advanced topics with study recommendations and progression guidance.

## Tech Stack
Python · FastAPI · Google Gemini API · Generative AI · NLP · HTML/CSS/JS · Prompt Engineering

## Repository Structure
```
1. Brainstorming & Ideation/
2. Requirement Analysis/
3. Project Design Phase/
4. Project Planning Phase/
5. Project Development Phase/   ← actual backend + frontend code
6. Project Testing/
7. Project Documentation/       ← this file
8. Project Demonstration/
```

## Setup
See `5. Project Development Phase/README.md` for full run instructions. Quick start:

```bash
cd "5. Project Development Phase/backend"
pip install -r requirements.txt
cp .env.example .env   # add your Gemini API key
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000 in your browser.

## Team
Shashank Paladugu (Team Lead) · Jaideep Tammineni · Venkata Krishna Nishanth Gopidesi ·
Muskan Muskan · Yashwanth Rayudu

## License
Educational project — Skill Wallet / Google Cloud Generative AI Track.
