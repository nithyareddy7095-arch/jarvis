from app.schemas.farm import NearbyFarm


class FarmDiscoveryService:
    async def nearby(self, lat: float, lng: float) -> list[NearbyFarm]:
        return [
            NearbyFarm(id=1, name="Sunrise Organic Farm", lat=lat + 0.01, lng=lng + 0.01, specialty="Hydroponics", experience_fee=18.0),
            NearbyFarm(id=2, name="Millet Trails Farm", lat=lat - 0.02, lng=lng + 0.03, specialty="Millet + Beekeeping", experience_fee=25.0),
        ]
