# 1. Brainstorming & Ideation

## Problem Statement
Students and self-learners often struggle to get quick, reliable, and personalized academic
help. Existing tools are either too generic (plain search) or too narrow (single-purpose
apps for only quizzes, or only summarization). There is a need for one lightweight assistant
that can explain concepts, answer questions, generate quizzes, summarize material, and guide
a learner's study path — all in one place.

## Idea
**EduGenie** — a Google Gemini powered educational assistant that acts as a personal tutor.
A learner types what they need (a concept to understand, a question, material to summarize,
or a subject to plan) and EduGenie routes the request to the right AI-powered module and
returns a clear, structured, study-ready response.

## Target Users
- School and college students revising for exams
- Self-learners picking up a new subject (e.g. SQL) without a structured course
- Educators who want a quick way to generate practice quizzes or explanations

## Why Generative AI
Static content (textbooks, pre-written FAQs) cannot adapt to the exact topic, phrasing, or
level a learner asks about. Gemini lets EduGenie generate explanations, quizzes, summaries,
and roadmaps on demand, for *any* topic, at the level the learner needs.

## Core Use-Case Scenarios
- **Scenario 1:** A student wants to learn about oceans and rivers. They ask "Which is the
  largest ocean?" EduGenie instantly provides an accurate answer with educational context.
- **Scenario 2:** A student studying the Pythagoras Theorem wants to assess their
  understanding. They select "Generate Quiz," and EduGenie creates topic-specific questions
  for self-evaluation.
- **Scenario 3:** A learner interested in SQL requests a structured learning roadmap.
  EduGenie generates a personalized learning path covering beginner, intermediate, and
  advanced topics with study recommendations and progression guidance.

## Chosen Direction
Build EduGenie as a lightweight web app: a FastAPI backend calling the Google Gemini API,
with a simple HTML/CSS frontend, so it can run on modest hardware (e.g. a MacBook Air / M1)
and be demoed easily.
