import ollama
import json
import re

def get_structured_resume(resume_text: str) -> dict:
    prompt = f"""
Parse the following resume and return a clean JSON response with these fields:
{{
  "name": "",
  "email": "",
  "skills": [],
  "education": [],
  "experience": []
}}

Resume:
{resume_text}
"""
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    content = response["message"]["content"]

    match = re.search(r"\{[\s\S]*\}", content)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            return {"error": "Invalid JSON", "raw_response": content}
    else:
        return {"error": "No JSON found", "raw_response": content}

def match_resume_to_job(resume_text: str, job_text: str) -> str:
    prompt = f"""
Compare this resume and job description.
Give a match score out of 100 and a brief explanation.

Resume:
{resume_text}

Job:
{job_text}
"""
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
