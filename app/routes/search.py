from fastapi import APIRouter
from app.services.embedding_service import get_embedding
from app.db import get_conn

router = APIRouter()

@router.get("/search")
def search(q: str):

    conn = get_conn()
    cur = conn.cursor()

    emb = get_embedding(q)

    cur.execute("""
        SELECT name, description
        FROM activities
        ORDER BY embedding <-> %s
        LIMIT 10
    """, (emb,))

    return cur.fetchall()
