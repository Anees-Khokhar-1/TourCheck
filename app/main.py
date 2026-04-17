from fastapi import FastAPI
from app.routes.ingest import router as ingest_router
from app.routes.search import router as search_router

app = FastAPI()

app.include_router(ingest_router)
app.include_router(search_router)
