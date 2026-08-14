# import ast
# import operator

# # -------------------------
# # Calculator Tool
# # -------------------------

# OPERATORS = {
#     ast.Add: operator.add,
#     ast.Sub: operator.sub,
#     ast.Mult: operator.mul,
#     ast.Div: operator.truediv,
# }


# def calculator_tool(expression):
#     try:
#         node = ast.parse(expression, mode="eval").body

#         if isinstance(node, ast.BinOp):
#             left = node.left.value
#             right = node.right.value

#             operation = OPERATORS[type(node.op)]

#             result = operation(left, right)

#             return {
#                 "tool": "Calculator",
#                 "status": "Success",
#                 "result": result
#             }

#         return {
#             "tool": "Calculator",
#             "status": "Failed",
#             "result": "Invalid expression"
#         }

#     except Exception as e:
#         return {
#             "tool": "Calculator",
#             "status": "Failed",
#             "result": str(e)
#         }


# # -------------------------
# # PDF Tool
# # -------------------------

# def pdf_reader_tool(file_name):

#     return {
#         "tool": "PDF Reader",
#         "status": "Success",
#         "result": f"Reading PDF: {file_name}"
#     }


# # -------------------------
# # Search Tool
# # -------------------------

# def search_tool(query):

#     return {
#         "tool": "Search",
#         "status": "Success",
#         "result": f"Searching for '{query}'..."
#     }


# # -------------------------
# # LLM Tool (Placeholder)
# # -------------------------

# def llm_tool(question):

#     return {
#         "tool": "LLM",
#         "status": "Success",
#         "result": f"I can answer this without any external tool.\nQuestion: {question}"
#     }


# # -------------------------
# # Agent
# # -------------------------

# def ai_agent(user_input):

#     text = user_input.lower()

#     # Calculator

#     if any(op in user_input for op in ["+", "-", "*", "/"]):

#         expression = (
#             user_input
#             .replace("What is", "")
#             .replace("Calculate", "")
#             .strip()
#         )

#         return calculator_tool(expression)

#     # PDF

#     elif ".pdf" in text:

#         return pdf_reader_tool(user_input)

#     # Search

#     elif text.startswith("search"):

#         query = user_input.replace("search", "").strip()

#         return search_tool(query)

#     # LLM

#     else:

#         return llm_tool(user_input)


# # -------------------------
# # Chat Loop
# # -------------------------

# print("=" * 50)
# print("        FIRST AI AGENT")
# print("Type 'exit' to quit")
# print("=" * 50)

# while True:

#     question = input("\nYou : ")

#     if question.lower() == "exit":
#         print("Agent : Goodbye!")
#         break

#     response = ai_agent(question)

#     print("\n----------------------------")
#     print("Tool Used :", response["tool"])
#     print("Status    :", response["status"])
#     print("Response  :", response["result"])
#     print("----------------------------")




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