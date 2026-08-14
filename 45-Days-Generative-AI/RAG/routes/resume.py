from fastapi import APIRouter, UploadFile, File, Form
from services.resume_service import analyze_resume_service

router = APIRouter()


@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    result = await analyze_resume_service(
        resume,
        job_description
    )

    return {
        "analysis": result
    }