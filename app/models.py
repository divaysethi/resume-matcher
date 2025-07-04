from pydantic import BaseModel

class ResumeParseResult(BaseModel):
    parsed_resume: str

class ResumeMatchResult(BaseModel):
    match_score: str
