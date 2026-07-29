# English-to-SQL Generator using Gemini LLM

A simple Python application that converts natural language (English) queries into SQL using Google's Gemini Large Language Model (LLM).

## Overview

This project demonstrates how an LLM can understand a user's English query and generate the corresponding SQL statement. It is built as a beginner-friendly project with minimal code and no web framework.

## Features

- Convert English queries into SQL
- Uses Google's Gemini LLM
- Simple command-line interface
- Minimal and easy-to-understand code
- Environment variables for secure API key management

## Project Structure

```
english-to-sql-generator/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/english-to-sql-generator.git
cd english-to-sql-generator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
MODEL_NAME=models/gemini-3.6-flash
```

## Usage

Run the application:

```bash
python main.py
```

Example:

```
Enter Your English Query:

Show all employees whose salary is greater than 50000.
```

Output:

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

## Technologies Used

- Python
- Google Gemini API
- google-genai
- python-dotenv

## Author

**Soumyadip Das**