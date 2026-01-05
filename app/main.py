# app/main.py
from fastapi import FastAPI
from app.api.v1.tickets import router as tickets_router

app = FastAPI(title="AI Customer Support Backend")

app.include_router(tickets_router)
