import httpx

from app.core.config import get_settings
from app.schemas.weather import WeatherResponse

settings = get_settings()


class WeatherService:
    async def get_weather(self, lat: float, lon: float) -> WeatherResponse:
        if not settings.openweather_api_key:
            return WeatherResponse(
                location=f"{lat:.3f},{lon:.3f}",
                temperature_c=29.4,
                humidity=74,
                rainfall_mm=8.2,
                advisory="Rain expected in 4 hours. Delay irrigation.",
            )

        params = {"lat": lat, "lon": lon, "appid": settings.openweather_api_key, "units": "metric"}
        async with httpx.AsyncClient(timeout=12) as client:
            response = await client.get(settings.openweather_url, params=params)
            response.raise_for_status()
            data = response.json()["list"][0]

        return WeatherResponse(
            location=f"{lat:.3f},{lon:.3f}",
            temperature_c=float(data["main"]["temp"]),
            humidity=int(data["main"]["humidity"]),
            rainfall_mm=float(data.get("rain", {}).get("3h", 0.0)),
            advisory="Monitor moisture and optimize drip irrigation schedule.",
        )
