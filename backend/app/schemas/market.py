from pydantic import BaseModel


class MarketPrice(BaseModel):
    crop: str
    market: str
    conventional_price: float
    organic_price: float
    demand_trend: str
