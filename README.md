# Credit Ledger System

A FastAPI-based ledger system for managing credit transactions and ledger operations.

## Technologies

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Alembic (migrations)

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create .env file
```bash
cp .env.example .env
```

4. Create a PostgreSQL database:
```bash
docker run -d \                                                    ✔
  --name my_postgres \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=dbname \
  -p 5432:5432 \
  postgres
```

5. Run the migrations
```bash
alembic upgrade head
```

6. Start the FastAPI server for the `app1` application:
```bash
uvicorn app1.src.main:app --reload
```


### Features
* Core ledger operations (DAILY_REWARD, SIGNUP_CREDIT, CREDIT_SPEND, CREDIT_ADD)
* Application-specific operations (CONTENT_CREATION, CONTENT_ACCESS)
* PostgreSQL database integration
* Pydantic models for data validation
* Extensible ledger operation system

### Testing

1. Create the test database:
```bash
docker run --name test_db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=test_db -p 5432:5432 -d postgres
```
Run tests using pytest:
```bash
pytest tests/test_ledger.py -v
```
