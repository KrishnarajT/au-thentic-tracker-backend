# main.py (snippet)
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import db.config_db as config_db
from router.goldRoutes import router as gold_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await config_db.init_db()
    try:
        yield
    finally:
        await config_db.engine.dispose()


app = FastAPI(lifespan=lifespan)

# CORS - allow your frontend (adjust origins)
app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://your-nas-ip:port"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"], )

# Mount router under /api so frontend's API_BASE_URL + paths match
app.include_router(gold_router, prefix="/api")
