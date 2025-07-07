# ShahDec Log Ingestor

🚀 A mini project to accept logs via FastAPI and store them in Elasticsearch.

## Features
- `/log` endpoint to receive logs
- Store logs in `shahdec-logs` index
- Simple Docker setup for Elasticsearch
- Query logs via Kibana or Python client

## Tech Stack
- FastAPI
- Elasticsearch
- Docker
- Python 3.11+

## Getting Started

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/shahdec-log-ingestor.git
cd shahdec-log-ingestor

# Set up virtual env & install
python -m venv env
source env/bin/activate
pip install -r requirements.txt

# Run FastAPI
uvicorn app.main:app --reload
