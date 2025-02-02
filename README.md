# FastAPI Project

This is a simple FastAPI project with a GET  `/api/classify-number` endpoint. The project also includes CORS support and auto-generated documentation.

## Features

- FastAPI-based web application.
- `/api/classify-number`  that Connects with numbers.com API that takes a number and returns interesting mathematical properties about it, along with a fun fact..
- Automatically generated Swagger and ReDoc documentation.
- CORS enabled for cross-origin requests.

---

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7+
- `pip` (Python package manager)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/busade/first_task

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/scripts/activate  #on cmd env\scripts\activate

3. Install dependencies
    ```bash
    pip install -r requirements.txt


## Usage
1. Run the Application
    ```bash
    fastapi dev main.py
2. Open your browser and navigate to
    Swagger UI: http://127.0.0.1:8000/docs


## Endpoint
The app has only one endpoint `/api/classify-number?number=6`and it will connect with numbers.com API that takes a number and returns interesting mathematical properties about it, along with a fun fact..

### Example
    {
    "number": 6,
    "is_prime": false,
    "is_perfect": false,
    "properties": [
        "armstrong",
        "even"
    ],
    "digit_sum": 6,
    "fun_fact": "6 is the first discrete biprime (2.3) and the first member of the (2.q) discrete biprime family."
}
