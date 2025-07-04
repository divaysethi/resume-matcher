from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from typing import Union, List, Any
import tempfile
import logging
import os

# spaCy NER
import spacy
nlp = spacy.load("en_core_web_sm")

# ✅ Allow Any for flexibility
class ParsedResume(BaseModel):
    name: str
    email: str
    skills: List[str]
    education: Any
    experience: Any

class ResumeParseResult(BaseModel):
    parsed_resume: Union[ParsedResume, str]  # string if error

class ResumeMatchResult(BaseModel):
    match_score: str

class Entity(BaseModel):
    text: str
    label: str

class ResumeEntities(BaseModel):
    entities: List[Entity]

# Module imports
from app.parser import extract_text_from_file
from app.matcher import get_structured_resume, match_resume_to_job
MODULES_AVAILABLE = True

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

@app.get("/")
def root():
    status = "Full functionality" if MODULES_AVAILABLE else "Mock mode"
    return {"message": f"Resume Matcher API is running ({status}). Visit /docs to test endpoints."}

@app.post("/parse", response_model=ResumeParseResult)
async def parse_resume(file: UploadFile = File(...)):
    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        resume_text = extract_text_from_file(tmp_path)
        parsed = get_structured_resume(resume_text)

        os.remove(tmp_path)  # clean up
        return {"parsed_resume": parsed}
    except Exception as e:
        logging.exception("Error in /parse")
        return {"parsed_resume": f"Error parsing resume: {str(e)}"}

@app.post("/match", response_model=ResumeMatchResult)
async def match_resume(file: UploadFile = File(...), job_text: str = Form(...)):
    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        resume_text = extract_text_from_file(tmp_path)
        match = match_resume_to_job(resume_text, job_text)

        os.remove(tmp_path)
        return {"match_score": match}
    except Exception as e:
        logging.exception("Error in /match")
        return {"match_score": f"Error matching resume: {str(e)}"}

@app.post("/ner", response_model=ResumeEntities)
async def extract_ner(file: UploadFile = File(...)):
    try:
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        resume_text = extract_text_from_file(tmp_path)
        doc = nlp(resume_text)
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

        os.remove(tmp_path)
        return {"entities": entities}
    except Exception as e:
        logging.exception("Error in /ner")
        return {"entities": [{"text": f"Error: {str(e)}", "label": "ERROR"}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
