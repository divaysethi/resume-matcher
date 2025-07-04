import fitz  # PyMuPDF
from docx import Document
from typing import Union
from pathlib import Path
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def extract_text_from_file(file_path: Union[str, Path]) -> str:
    path = Path(file_path)
    if path.suffix.lower() == ".pdf":
        doc = fitz.open(str(path))
        return "\n".join(page.get_text() for page in doc)
    elif path.suffix.lower() == ".docx":
        doc = Document(str(path))
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")

def extract_entities(text: str) -> list:
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

def get_structured_resume(resume_text: str) -> dict:
    return {
        "text": resume_text,
        "entities": extract_entities(resume_text)
    }
