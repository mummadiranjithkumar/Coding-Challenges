import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def analyze_resume(job_description, retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an expert ATS Resume Analyzer and Senior Technical Recruiter.

Your task is to compare a candidate's resume with the provided Job Description and produce a realistic ATS evaluation.

==================================================
JOB DESCRIPTION
==================================================

{job_description}

==================================================
RESUME
==================================================

{context}

==================================================
GENERAL RULES
==================================================

1. Compare ONLY using the resume.
2. Never invent skills or experience.
3. Never assume work experience.
4. If the candidate is a fresher, treat projects as Project Experience.
5. Skills from projects = Project Experience.
6. Skills from education = Academic Knowledge.
7. Skills currently being learned = Learning.
8. Professional Experience only if explicitly mentioned.

==================================================
STEP 1 : EXTRACT REQUIRED TECHNICAL SKILLS
==================================================

First identify ALL technical skills mentioned in the Job Description.

Technical skills include:

• Programming Languages
• Frameworks
• Libraries
• AI / ML Technologies
• Generative AI Technologies
• Databases
• Cloud Platforms
• DevOps Tools
• APIs
• Software Tools
• Vector Databases
• AI Frameworks

==================================================
VERY IMPORTANT
==================================================

Each skill MUST be:

• 1 to 4 words only
• A technology name
• A framework
• A library
• A platform
• A tool
• A concise capability name

GOOD

Python
FastAPI
React
TensorFlow
PyTorch
LLMs
RAG
LangChain
Docker
Kubernetes
AWS
Azure AI
Snowflake
Snowflake Cortex
MLOps
Prompt Engineering
Semantic Search
Embeddings
Vector Databases
AI Agents
Agentic AI
Conversational AI
Production AI Systems

BAD

Lead AI research and development

Rapidly prototype AI solutions

Experience working with cross-functional teams

Moving prototypes into production

Bachelor's Degree in Computer Science

5+ years experience

Strong communication skills

Financial services experience

==================================================
NORMALIZATION RULES
==================================================

Convert long descriptions into concise industry-standard names.

Examples:

Lead AI research
→ AI Research

Designing agentic workflows
→ Agentic AI

Rapidly prototype solutions
→ Prototyping

Moving AI prototypes into production
→ MLOps

Production AI environments
→ Production AI Systems

Semantic search patterns
→ Semantic Search

Enterprise environments
→ Enterprise Systems

Modern AI libraries
→ AI Libraries

Data-driven systems
→ Data Engineering

Conversational AI experiences
→ Conversational AI

Do NOT return verbs or complete sentences.

==================================================
STEP 2 : MATCH SKILLS
==================================================

Compare ONLY the extracted technical skills with the resume.

Return:

matching_skills

missing_skills

Each matching skill must contain its level.

Levels:

Professional Experience

Project Experience

Academic Knowledge

Learning

==================================================
STEP 3 : ATS SCORE
==================================================

Calculate ATS score using:

• Programming Languages
• Frameworks
• Libraries
• AI Technologies
• Cloud Platforms
• Databases
• DevOps
• Project Relevance

Ignore years of experience for freshers.

Do NOT heavily penalize domain experience.

Score Guide

90-100 Excellent

75-89 Strong

60-74 Good

40-59 Moderate

0-39 Weak

==================================================
STEP 4 : STRENGTHS
==================================================

List genuine strengths from the resume.

==================================================
STEP 5 : WEAKNESSES
==================================================

List genuine technical gaps.

==================================================
STEP 6 : SUGGESTIONS
==================================================

Give practical ATS improvement suggestions.

Examples

Learn Azure AI

Learn Snowflake

Build one MLOps project

Deploy projects using Docker

Improve resume keywords

==================================================
OUTPUT FORMAT
==================================================

Return ONLY valid JSON.

{{
    "match_score": 0,

    "matching_skills": [
        {{
            "skill": "",
            "level": "Professional Experience | Project Experience | Academic Knowledge | Learning"
        }}
    ],

    "missing_skills": [],

    "strengths": [],

    "weaknesses": [],

    "suggestions": [],

    "ats_feedback": {{
        "keywords_found": [],
        "keywords_missing": [],
        "resume_summary": "",
        "ats_rating": "Excellent | Good | Average | Poor"
    }}
}}

Return ONLY JSON.

Do NOT return markdown.

Do NOT use ```json.

Do NOT explain anything.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    result = json.loads(text)

    return result