from fastapi import FastAPI

app = FastAPI(
    title="English to SQL Generator API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to English-to-SQL Generator API"
    }


@app.post("/generate-sql")
def generate_sql():
    return {
        "success": True,
        "sql": "SELECT * FROM employees;"
    }