from fastapi import APIRouter
import requests

router = APIRouter()

API_BASE_URL = "http://your-nas-ip:port/api"  # Update this with your NAS API base URL
GOLD_PRICE_API = "https://api.metals.live/v1/spot/gold"  # Example gold price API

@router.get("/gold-price/current", response_model=float)
async def get_current_price():
    try:
        response = requests.get(f"{API_BASE_URL}/gold-price")
        response.raise_for_status()
        data = response.json()
        return data['pricePerGram']
    except Exception as e:
        return {"error": str(e)}

@router.get("/gold-price/historical/{days_back}", response_model=float)
async def get_historical_price(days_back: int):
    try:
        response = requests.get(f"{API_BASE_URL}/gold-price/historical?daysBack={days_back}")
        response.raise_for_status()
        data = response.json()
        return data['pricePerGram']
    except Exception as e:
        return {"error": str(e)}

@router.get("/gold-price/date/{date}", response_model=float)
async def get_price_at_date(date: str):
    try:
        response = requests.get(f"{API_BASE_URL}/gold-price/historical?date={date}")
        response.raise_for_status()
        data = response.json()
        return data['pricePerGram']
    except Exception as e:
        return {"error": str(e)}