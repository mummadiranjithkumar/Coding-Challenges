import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -----------------------
# TOOLS
# -----------------------

def calculator(expression):

    try:
        result = eval(expression)

        return f"The answer is {result}"

    except Exception:

        return "Invalid mathematical expression."


def search(query):

    return f"Searching Google for: {query}"


def read_pdf(file):

    return f"Reading PDF: {file}"


# -----------------------
# AGENT
# -----------------------

def run_agent(user_input):

    system_prompt = f"""
You are an AI Agent.

Your job is to decide which tool should be used.

Available tools:

1. calculator
Use when mathematical calculations are needed.

2. pdf_reader
Use when the user mentions a pdf.

3. search
Use when user wants latest information.

4. llm
Use when no tool is required.

Return ONLY valid JSON.

Example:

{{
"tool":"calculator",
"input":"25+30"
}}

User Request:

{user_input}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt
    )

    decision = response.text.strip()

    if decision.startswith("```json"):
        decision = decision.replace("```json", "").replace("```", "").strip()

    elif decision.startswith("```"):
        decision = decision.replace("```", "").strip()

    tool = json.loads(decision)

    if tool["tool"] == "calculator":

        return calculator(tool["input"])

    elif tool["tool"] == "pdf_reader":

        return read_pdf(tool["input"])

    elif tool["tool"] == "search":

        return search(tool["input"])

    else:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        return response.text


# -----------------------
# MAIN LOOP
# -----------------------

print("=" * 60)
print("FIRST GEMINI AI AGENT")
print("=" * 60)

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    answer = run_agent(question)

    print("\nAgent :", answer)