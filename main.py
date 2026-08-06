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
def show_menu():
    print("\n" + "=" * 50)
    print(" English to SQL Generator ")
    print("=" * 50)
    print("1. Generate SQL")
    print("2. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            generate_sql()
        elif choice == "2":
            print("\nThank you for using English to SQL Generator.")
            break
        else:
            print("\nInvalid choice. Please try again.")
            
if __name__ == "__main__":
    main()