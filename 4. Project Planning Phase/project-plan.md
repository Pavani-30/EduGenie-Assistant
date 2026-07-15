# 4. Project Planning Phase

## Team
| Name | Role |
|------|------|
| Shashank Paladugu | Team Lead |
| Jaideep Tammineni | Member |
| Venkata Krishna Nishanth Gopidesi | Member |
| Muskan Muskan | Member |
| Yashwanth Rayudu | Member |

## Epics
- **Epic 1: Model Selection and Architecture** — Choose Gemini model, design the FastAPI
  routing architecture, define request/response schemas for all five modules.
- **Epic 2: Core Functionalities Development** — Build the Explanation, Q&A, Quiz,
  Summarization, and Learning Path modules against the Gemini API.
- **Epic 3: Frontend Development** — Build the HTML/CSS/JS interface: module navigation,
  input forms, and results display.
- **Epic 4: Deployment** — Package the app, document setup, prepare the demo and GitHub
  submission.

## Kanban Breakdown (Stories & Subtasks)
### Epic 1 — Model Selection and Architecture
- [ ] Evaluate Gemini model options (cost/latency vs. quality) and select `gemini-1.5-flash`
- [ ] Design the FastAPI route → module mapping
- [ ] Define Pydantic request/response schemas

### Epic 2 — Core Functionalities Development
- [ ] Implement shared Gemini client wrapper
- [ ] Implement Explanation Module (`/explain`)
- [ ] Implement Q&A Module (`/qa`)
- [ ] Implement Quiz Generation Module (`/quiz`)
- [ ] Implement Summarization Module (`/summarize`)
- [ ] Implement Learning Path Module (`/learn/recommendations`)
- [ ] Add error handling for missing API key / Gemini failures

### Epic 3 — Frontend Development
- [ ] Build module navigation rail (5 modules)
- [ ] Build input forms per module
- [ ] Wire fetch() calls to backend endpoints
- [ ] Style results panel and loading/error states
- [ ] Responsive layout for mobile

### Epic 4 — Deployment
- [ ] Write README with setup instructions
- [ ] Add `.env.example` and `requirements.txt`
- [ ] Record demo video / prepare live demo
- [ ] Push complete project to GitHub
- [ ] Add demo link and GitHub link to Skill Wallet

## Project Flow
1. Ideation → 2. Requirements → 3. Design → 4. Planning → 5. Development →
6. Testing → 7. Documentation → 8. Demonstration

## Pre-Requisites
- Google Gemini API key
- Python 3.10+ installed
- Git & GitHub account
