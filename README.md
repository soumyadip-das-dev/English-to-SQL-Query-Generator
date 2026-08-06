# English-to-SQL Generator using Gemini LLM

Convert natural language (English) into SQL queries using Google's Gemini Large Language Model (LLM).

---

## Overview

English-to-SQL Generator is a simple Python command-line application that demonstrates how Large Language Models (LLMs) can translate English instructions into SQL queries.

The application accepts an English query from the user, sends it to the Gemini API, and displays the generated SQL query in the terminal.

This project focuses on understanding LLM integration, prompt engineering, and clean Python programming while keeping the implementation minimal and easy to understand.

---

## Features

- Convert English queries into SQL
- Powered by Google Gemini LLM
- Simple command-line interface (CLI)
- Menu-driven interaction
- Generate multiple SQL queries in one session
- Input validation
- Removes Markdown formatting from generated SQL
- Secure API key management using `.env`

---

## Project Structure

```text
english-to-sql-generator/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Workflow

```text
User
   │
   ▼
Enter English Query
   │
   ▼
Python Application
   │
   ▼
Gemini API
   │
   ▼
Generated SQL
   │
   ▼
Display SQL
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/english-to-sql-generator.git
cd english-to-sql-generator
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
MODEL_NAME=models/gemini-3.6-flash
```

---

## Run the Application

```bash
python main.py
```

---

## Example

### Input

```text
Enter Your English Query:

Show all employees whose salary is greater than 50000.
```

### Output

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

---

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK (`google-genai`)
- python-dotenv

---

## Learning Outcomes

This project helped me understand:

- Large Language Model (LLM) integration
- Prompt engineering
- Environment variables using `.env`
- API communication in Python
- Function-based programming
- Clean and modular code
- Git & GitHub version control

---

## Current Version

**Version:** `v1.0.0-beta`

### Completed

- English → SQL conversion
- Gemini API integration
- Interactive CLI
- Input validation
- Multiple query generation

---

## Future Improvements

- Streamlit web interface
- SQL syntax highlighting
- Copy generated SQL
- Database schema-aware SQL generation
- Database connectivity and SQL execution

---

## Author

**Soumyadip Das**

B.Tech CSE (AI & ML)

---

## License

This project is licensed under the MIT License.