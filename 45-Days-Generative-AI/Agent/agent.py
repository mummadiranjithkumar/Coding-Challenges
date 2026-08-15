# import os
# import json
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )

# # -----------------------
# # TOOLS
# # -----------------------

# def calculator(expression):

#     try:
#         result = eval(expression)

#         return f"The answer is {result}"

#     except Exception:

#         return "Invalid mathematical expression."


# def search(query):

#     return f"Searching Google for: {query}"


# def read_pdf(file):

#     return f"Reading PDF: {file}"


# # -----------------------
# # AGENT
# # -----------------------

# def run_agent(user_input):

#     system_prompt = f"""
# You are an AI Agent.

# Your job is to decide which tool should be used.

# Available tools:

# 1. calculator
# Use when mathematical calculations are needed.

# 2. pdf_reader
# Use when the user mentions a pdf.

# 3. search
# Use when user wants latest information.

# 4. llm
# Use when no tool is required.

# Return ONLY valid JSON.

# Example:

# {{
# "tool":"calculator",
# "input":"25+30"
# }}

# User Request:

# {user_input}
# """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=system_prompt
#     )

#     decision = response.text.strip()

#     if decision.startswith("```json"):
#         decision = decision.replace("```json", "").replace("```", "").strip()

#     elif decision.startswith("```"):
#         decision = decision.replace("```", "").strip()

#     tool = json.loads(decision)

#     if tool["tool"] == "calculator":

#         return calculator(tool["input"])

#     elif tool["tool"] == "pdf_reader":

#         return read_pdf(tool["input"])

#     elif tool["tool"] == "search":

#         return search(tool["input"])

#     else:

#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=user_input
#         )

#         return response.text


# # -----------------------
# # MAIN LOOP
# # -----------------------

# print("=" * 60)
# print("FIRST GEMINI AI AGENT")
# print("=" * 60)

# while True:

#     question = input("\nYou : ")

#     if question.lower() == "exit":
#         break

#     answer = run_agent(question)

#     print("\nAgent :", answer)



# import os
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types


# # --------------------------------
# # LOAD API KEY
# # --------------------------------

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )


# # --------------------------------
# # TOOL 1: CALCULATOR
# # --------------------------------

# def calculator(expression: str) -> str:

#     try:
#         result = eval(expression)

#         return str(result)

#     except Exception:
#         return "Invalid mathematical expression."


# # --------------------------------
# # TOOL 2: GET USER NAME
# # --------------------------------

# def get_user_name() -> str:

#     return "Ranjith"


# # --------------------------------
# # FUNCTION DECLARATIONS
# # --------------------------------

# calculator_tool = types.FunctionDeclaration(
#     name="calculator",
#     description="Calculate a mathematical expression.",
#     parameters=types.Schema(
#         type="OBJECT",
#         properties={
#             "expression": types.Schema(
#                 type="STRING",
#                 description="Mathematical expression such as 25 * 40"
#             )
#         },
#         required=["expression"]
#     )
# )


# user_name_tool = types.FunctionDeclaration(
#     name="get_user_name",
#     description="Returns the user's name.",
#     parameters=types.Schema(
#         type="OBJECT",
#         properties={}
#     )
# )


# # --------------------------------
# # TOOL CONFIGURATION
# # --------------------------------

# tools = types.Tool(
#     function_declarations=[
#         calculator_tool,
#         user_name_tool
#     ]
# )


# # --------------------------------
# # AGENT
# # --------------------------------

# def run_agent(user_input):

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=user_input,
#         config=types.GenerateContentConfig(
#             tools=[tools]
#         )
#     )

#     # --------------------------------
#     # CHECK WHETHER GEMINI REQUESTED
#     # A FUNCTION
#     # --------------------------------

#     function_call = None

#     for part in response.candidates[0].content.parts:

#         if part.function_call:
#             function_call = part.function_call
#             break

#     # --------------------------------
#     # NO FUNCTION REQUIRED
#     # --------------------------------

#     if function_call is None:

#         return response.text

#     # --------------------------------
#     # GET FUNCTION NAME
#     # --------------------------------

#     function_name = function_call.name

#     arguments = function_call.args

#     print("\nFunction called:", function_name)
#     print("Arguments:", arguments)

#     # --------------------------------
#     # EXECUTE FUNCTION
#     # --------------------------------

#     if function_name == "calculator":

#         result = calculator(
#             arguments["expression"]
#         )

#     elif function_name == "get_user_name":

#         result = get_user_name()

#     else:

#         result = "Unknown function."

#     print("Function result:", result)

#     # --------------------------------
#     # SEND FUNCTION RESULT
#     # BACK TO GEMINI
#     # --------------------------------

#     function_response = types.Part.from_function_response(
#         name=function_name,
#         response={
#             "result": result
#         }
#     )

#     final_response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=[
#             types.Content(
#                 role="user",
#                 parts=[
#                     types.Part.from_text(
#                         text=user_input
#                     )
#                 ]
#             ),
#             response.candidates[0].content,
#             types.Content(
#                 role="tool",
#                 parts=[function_response]
#             )
#         ],
#         config=types.GenerateContentConfig(
#             tools=[tools]
#         )
#     )

#     return final_response.text


# # --------------------------------
# # MAIN LOOP
# # --------------------------------

# print("=" * 60)
# print("DAY 5 - GEMINI FUNCTION CALLING AGENT")
# print("=" * 60)

# while True:

#     question = input("\nYou : ")

#     if question.lower() == "exit":
#         break

#     answer = run_agent(question)

#     print("\nAgent :", answer)

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


# --------------------------------
# LOAD API KEY
# --------------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


# --------------------------------
# TOOL 1: CALCULATOR
# --------------------------------

def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.

    Args:
        expression: A mathematical expression such as 25 * 40.

    Returns:
        The calculated result.
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception:
        return "Invalid mathematical expression."


# --------------------------------
# TOOL 2: GET USER NAME
# --------------------------------

def get_user_name() -> str:
    """
    Get the user's name.

    Returns:
        The user's name.
    """

    return "Ranjith"


# --------------------------------
# AGENT
# --------------------------------

def run_agent(user_input):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,

        config=types.GenerateContentConfig(
            tools=[
                calculator,
                get_user_name
            ]
        )
    )

    return response.text


# --------------------------------
# MAIN LOOP
# --------------------------------

print("=" * 60)
print("DAY 5 - AUTOMATIC FUNCTION CALLING AGENT")
print("=" * 60)

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    try:

        answer = run_agent(question)

        print("\nAgent :", answer)

    except Exception as e:

        print("\nError :", e)