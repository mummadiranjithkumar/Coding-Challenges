from pydantic import BaseModel


class ResumeRequest(BaseModel):
    pdf_path: str
    job_description: str


class ResumeResponse(BaseModel):
    analysis: str