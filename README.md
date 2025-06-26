# Electricity Price Api Challenge (FastAPI + Docker)

This coding challenge creates a simple FastAPI web service that calculates the mean price for a given state from a CSV file.

---

## Running the App with Docker

### 1. Build the Docker image

```bash
docker compose build
```

### 2. Run the container
```bash
docker compose up
```

## API Endpoint

### `GET /mean-price`

**Example:**

```
http://localhost:8000/mean_price?state=Vic
```

### Swagger UI:

```
http://localhost:8000/docs
```

## Running Unit Tests Locally

Make sure you have Python and dependencies installed locally.

### 1. Create a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
pip install pytest
```

### 3. Run the tests

```bash
pytest test_main.py
```

## Docker Cleanup

Stop and remove the container:

```bash
docker compose down
```