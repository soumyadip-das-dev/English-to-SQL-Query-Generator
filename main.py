# Import libraries
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# Create Gemini Client
client = genai.Client(api_key=API_KEY)


def generate_sql():
    """Generates SQL query from English input."""

    query = input("\nEnter Your English Query: ").strip()

    if not query:
        print("\nPlease enter a valid query.")
        return

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"""
Convert the following English sentence into an SQL query.

Rules:
- Return only the SQL query.
- Do not explain anything.
- Do not use Markdown.
- Do not use code blocks.

English:
{query}
"""
        )

        sql = response.text.strip()
        sql = sql.replace("```sql", "")
        sql = sql.replace("```", "").strip()

        print("\nGenerated SQL:\n")
        print(sql)

    except Exception as e:
        print(f"\nError: {e}")


def main():
    """Main function of the application."""

    print("=" * 50)
    print("        English to SQL Generator")
    print("=" * 50)
    print(" Convert English into SQL using Gemini LLM")
    print("=" * 50)

    while True:

        generate_sql()

        choice = input("\nGenerate another SQL query? (y/n): ").strip().lower()

        if choice != "y":
            print("\nThank you for using English to SQL Generator!")
            break


if __name__ == "__main__":
    main()