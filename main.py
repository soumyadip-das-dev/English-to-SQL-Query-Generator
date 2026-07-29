# import libraries
from google import genai
from dotenv import load_dotenv
import os

# variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

client = genai.Client(api_key=API_KEY)


def generate_sql():
    query = input("Enter Your English Query: ")

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"""
        Convert the following English sentence into an SQL query.
        English: {query}
        """
    )

    print("Generated SQL: \n", response.text)


generate_sql()