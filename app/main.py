from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
from app.api import gold_purchases, gold_price, settings
from app.models import gold_purchase, settings as settings_model

# Create the FastAPI app
app = FastAPI()

# Allow CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API routers
app.include_router(gold_purchases.router, prefix="/api/gold-purchases", tags=["gold_purchases"])
app.include_router(gold_price.router, prefix="/api/gold-price", tags=["gold_price"])
app.include_router(settings.router, prefix="/api/settings", tags=["settings"])

# Create the database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(gold_purchase.Base.metadata.create_all)
        await conn.run_sync(settings_model.Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "Welcome to the Gold Tracker API!"}