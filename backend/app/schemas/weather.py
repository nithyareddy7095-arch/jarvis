from pydantic import BaseModel


class WeatherResponse(BaseModel):
    location: str
    temperature_c: float
    humidity: int
    rainfall_mm: float
    advisory: str
