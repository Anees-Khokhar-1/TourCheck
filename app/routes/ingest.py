from fastapi import APIRouter
from app.services.pipeline import process_activity
from pydantic import BaseModel
from typing import List, Dict, Any

router = APIRouter()

class ActivityList(BaseModel):
    data: List[Dict[str, Any]]

@router.post("/ingest")
def ingest(payload: ActivityList):

    results = []

    for item in payload.data:
        results.append(process_activity(item))

    return results
