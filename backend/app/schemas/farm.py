from pydantic import BaseModel


class NearbyFarm(BaseModel):
    id: int
    name: str
    lat: float
    lng: float
    specialty: str
    experience_fee: float
