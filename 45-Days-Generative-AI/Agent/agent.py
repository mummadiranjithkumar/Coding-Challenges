# import os
# from datetime import datetime

# from dotenv import load_dotenv
# from google import genai
# from google.genai import types


# # ==========================================
# # LOAD API KEY
# # ==========================================

# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )


# # ==========================================
# # TOOL 1: CALCULATOR
# # ==========================================

# def calculator(expression: str) -> str:
#     """
#     Calculate a mathematical expression.

#     Args:
#         expression: A mathematical expression such as 25 * 40.

#     Returns:
#         The calculated result.
#     """

#     try:
#         result = eval(expression)
#         return str(result)

#     except Exception:
#         return "Invalid mathematical expression."


# # ==========================================
# # TOOL 2: CURRENT DATE AND TIME
# # ==========================================

# def get_current_datetime() -> str:
#     """
#     Get the current local date and time.

#     Returns:
#         Current date and time.
#     """

#     current_time = datetime.now()

#     return current_time.strftime(
#         "%Y-%m-%d %H:%M:%S"
#     )


# # ==========================================
# # TOOL 3: USER INFORMATION
# # ==========================================

# def get_user_info() -> str:
#     """
#     Get information about the current user.

#     Returns:
#         User information.
#     """

#     return (
#         "Name: Ranjith Kumar\n"
#         "Role: Computer Science Graduate\n"
#         "Learning: Generative AI and AI Agents"
#     )


# # ==========================================
# # TOOL 4: UNIT CONVERTER
# # ==========================================

# def convert_units(
#     value: float,
#     from_unit: str,
#     to_unit: str
# ) -> str:
#     """
#     Convert common units.

#     Args:
#         value: Numeric value to convert.
#         from_unit: Unit to convert from.
#         to_unit: Unit to convert to.

#     Returns:
#         Converted value.
#     """

#     from_unit = from_unit.lower()
#     to_unit = to_unit.lower()

#     # -----------------------------
#     # Kilometer -> Mile
#     # -----------------------------

#     if from_unit in ["km", "kilometer", "kilometers"]:

#         if to_unit in ["mile", "miles", "mi"]:

#             result = value * 0.621371

#             return f"{value} km = {result:.2f} miles"

#     # -----------------------------
#     # Mile -> Kilometer
#     # -----------------------------

#     if from_unit in ["mile", "miles", "mi"]:

#         if to_unit in ["km", "kilometer", "kilometers"]:

#             result = value * 1.60934

#             return f"{value} miles = {result:.2f} km"

#     # -----------------------------
#     # Celsius -> Fahrenheit
#     # -----------------------------

#     if from_unit in ["c", "celsius"]:

#         if to_unit in ["f", "fahrenheit"]:

#             result = (value * 9 / 5) + 32

#             return f"{value}°C = {result:.2f}°F"

#     # -----------------------------
#     # Fahrenheit -> Celsius
#     # -----------------------------

#     if from_unit in ["f", "fahrenheit"]:

#         if to_unit in ["c", "celsius"]:

#             result = (value - 32) * 5 / 9

#             return f"{value}°F = {result:.2f}°C"

#     return (
#         f"I don't currently support conversion "
#         f"from {from_unit} to {to_unit}."
#     )


# # ==========================================
# # TOOLS
# # ==========================================

# tools = [
#     calculator,
#     get_current_datetime,
#     get_user_info,
#     convert_units
# ]


# # ==========================================
# # AGENT
# # ==========================================

# def run_agent(user_input: str) -> str:

#     response = client.models.generate_content(

#         model="gemini-2.5-flash",

#         contents=user_input,

#         config=types.GenerateContentConfig(

#             tools=tools
#         )
#     )

#     return response.text


# # ==========================================
# # MAIN LOOP
# # ==========================================

# print("=" * 60)
# print("DAY 6 - MULTI-TOOL GEMINI AI AGENT")
# print("=" * 60)

# print("\nAvailable tools:")
# print("1. Calculator")
# print("2. Current Date & Time")
# print("3. User Information")
# print("4. Unit Converter")

# print("\nType 'exit' to stop.")


# while True:

#     question = input("\nYou : ")

#     if question.lower() == "exit":
#         print("\nAgent stopped.")
#         break

#     try:

#         answer = run_agent(question)

#         print("\nAgent :", answer)

#     except Exception as e:

#         print("\nError :", e)

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# ==========================================
# LOAD API KEY
# ==========================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


# ==========================================
# TOOL 1: GET USER AGE
# ==========================================

def get_user_age() -> int:
    """
    Get the user's current age.

    Returns:
        The user's current age.
    """

    return 21


# ==========================================
# TOOL 2: CALCULATOR
# ==========================================

def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.

    Args:
        expression: Mathematical expression such as 21 + 1.

    Returns:
        The calculation result.
    """

    try:
        result = eval(expression)

        return str(result)

    except Exception:
        return "Invalid mathematical expression."


# ==========================================
# TOOL 3: UNIT CONVERTER
# ==========================================

def convert_km_to_miles(
    kilometers: float
) -> str:
    """
    Convert kilometers to miles.

    Args:
        kilometers: Distance in kilometers.

    Returns:
        Distance in miles.
    """

    miles = kilometers * 0.621371

    return f"{miles:.2f} miles"


# ==========================================
# AVAILABLE TOOLS
# ==========================================

tools = [
    get_user_age,
    calculator,
    convert_km_to_miles
]


# ==========================================
# AGENT
# ==========================================

def run_agent(user_input: str):

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=user_input,

        config=types.GenerateContentConfig(

            tools=tools
        )
    )

    return response.text


# ==========================================
# MAIN LOOP
# ==========================================

print("=" * 60)
print("DAY 7 - SEQUENTIAL TOOL CALLING AGENT")
print("=" * 60)

print("""
Try:

1. What is my age?
2. What will my age be next year?
3. Convert 10 km to miles.
4. What is Python?
""")

print("Type 'exit' to stop.")


while True:

    question = input("\nYou : ")

    if question.lower() == "exit":

        print("\nAgent stopped.")

        break

    try:

        answer = run_agent(question)

        print("\nAgent :", answer)

    except Exception as e:

        print("\nError :", e)