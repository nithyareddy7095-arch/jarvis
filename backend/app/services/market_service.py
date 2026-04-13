from app.schemas.market import MarketPrice


class MarketService:
    async def get_prices(self, crop: str) -> list[MarketPrice]:
        crop_name = crop.title() if crop else "Tomato"
        return [
            MarketPrice(
                crop=crop_name,
                market="Green Valley Mandi",
                conventional_price=24.5,
                organic_price=34.0,
                demand_trend="Rising",
            ),
            MarketPrice(
                crop=crop_name,
                market="River Side Market",
                conventional_price=22.2,
                organic_price=31.8,
                demand_trend="Stable",
            ),
        ]
