<p align="center">
  <img src="https://img.icons8.com/external-flat-juicy-fish/64/resume.png" width="100" alt="Resume Matcher Logo">
  <h1 align="center">Resume Matcher API</h1>
  <p align="center">📄→⚙️ AI-Powered Resume Parsing & Matching using FastAPI + LLM</p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/FastAPI-🚀-green?style=flat-square" />
  <img src="https://img.shields.io/github/license/YOUR-USERNAME/resume-matcher?style=flat-square" />
</p>

---

## 🔍 Overview

This project is a FastAPI-based microservice that extracts information from resumes (PDF or DOCX), identifies named entities, and matches resumes against job descriptions using LLM (Ollama/Mistral). Perfect for ATS, recruiters, and hiring platforms.

---

## ⚙️ Features

- 🧠 LLM-powered resume parsing
- ✅ Resume to JD matching score (out of 100)
- 🧾 NER tagging using spaCy
- 🧪 Swagger UI for interactive testing (/docs)

---

## 🚀 Endpoints

| Method | Endpoint     | Description                    |
|--------|--------------|--------------------------------|
| POST   | /parse       | Upload resume and extract data |
| POST   | /match       | Compare resume & JD, get score |
| POST   | /ner         | Named Entity Recognition (NER) |

---
