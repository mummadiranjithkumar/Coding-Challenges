import os
import shutil

from PdfExtractor import extract_text
from clean_text import clean_text
from chunker import create_chunks
from embeddings import create_embeddings
from vector_store import store_embeddings
from retriever import retrieve_chunks
from generator import analyze_resume


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


async def analyze_resume_service(uploaded_file, job_description):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    text = extract_text(file_path)

    cleaned_text = clean_text(text)

    chunks = create_chunks(cleaned_text)

    embeddings = create_embeddings(chunks)

    collection = store_embeddings(
        chunks,
        embeddings
    )

    results = retrieve_chunks(
        collection,
        job_description
    )

    retrieved_chunks = results["documents"][0]

    analysis = analyze_resume(
        job_description,
        retrieved_chunks
    )

    return analysis