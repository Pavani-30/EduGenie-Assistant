# 6. Project Testing

## Test Cases

| ID | Module | Input | Expected Result | Status |
|----|--------|-------|------------------|--------|
| TC01 | Explanation | topic="Pythagoras Theorem", level="beginner" | Clear, simple explanation with an example | Pass |
| TC02 | Explanation | topic="" (empty) | 422 validation error (topic required) | Pass |
| TC03 | Q&A | question="Which is the largest ocean?" | Correct answer + educational context | Pass |
| TC04 | Quiz | topic="Pythagoras Theorem", num_questions=5 | 5 MCQs, each with 4 options and an answer key | Pass |
| TC05 | Quiz | num_questions=25 | 422 validation error (max 20) | Pass |
| TC06 | Summarization | text=<paragraph> | Concise bullet-point summary | Pass |
| TC07 | Learning Path | topic="SQL" | Roadmap with Beginner/Intermediate/Advanced sections | Pass |
| TC08 | Backend | GOOGLE_API_KEY missing | 500 error with clear message, no crash | Pass |
| TC09 | Frontend | Switch between all 5 module tabs | Correct panel shown, previous result cleared | Pass |
| TC10 | Frontend | Submit while a request is pending | Button disabled, shows "Thinking..." | Pass |
| TC11 | Health check | GET /health | Returns `{"status": "ok"}` | Pass |

## Testing Approach
- **Unit-level:** Each module function (`explain.py`, `qa.py`, etc.) can be tested by mocking
  `gemini_client.generate` and asserting the prompt sent and the value returned.
- **API-level:** Use FastAPI's `TestClient` to hit each endpoint with valid/invalid payloads.
- **Manual/UI:** Verified each of the 3 core scenarios end-to-end through the browser.

## Sample unit test (pytest)
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_explain_requires_topic():
    response = client.post("/explain", json={})
    assert response.status_code == 422
```
