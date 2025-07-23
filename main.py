from fastapi import FastAPI, Request
from elastic_client import es
from models import LogModel
from datetime import datetime, timezone

app = FastAPI()

@app.post("/log")
async def ingest_log(log: LogModel):
    doc = log.dict()
    doc['timestamp'] = datetime.now(timezone.utc).isoformat()
    doc['@timestamp'] = datetime.now(timezone.utc).isoformat()
    res = es.index(index="shahdec-logs", document=doc)
    return {"status": "stored", "result": res['result']}
