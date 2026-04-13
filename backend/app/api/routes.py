from fastapi import APIRouter, Depends, File, Query, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.schemas.common import MessageResponse
from app.schemas.farm import NearbyFarm
from app.schemas.market import MarketPrice
from app.schemas.plant import PlantDiagnosisResponse
from app.schemas.video import VideoUploadRequest, VideoUploadResponse
from app.schemas.weather import WeatherResponse
from app.services.bhoomi_service import BhoomiService
from app.services.community_service import CommunityService
from app.services.disease_service import DiseaseDetectionService
from app.services.farm_service import FarmDiscoveryService
from app.services.market_service import MarketService
from app.services.weather_service import WeatherService

router = APIRouter()

bhoomi_service = BhoomiService()
disease_service = DiseaseDetectionService()
weather_service = WeatherService()
market_service = MarketService()
farm_service = FarmDiscoveryService()
community_service = CommunityService()


@router.get("/", response_model=MessageResponse)
async def root() -> MessageResponse:
    return MessageResponse(message="Travel with Farmer API is running.")


@router.post("/bhoomi-chat", response_model=ChatResponse)
async def bhoomi_chat(payload: ChatRequest) -> ChatResponse:
    return await bhoomi_service.ask(payload)


@router.post("/plant-diagnosis", response_model=PlantDiagnosisResponse)
async def plant_diagnosis(file: UploadFile = File(...)) -> PlantDiagnosisResponse:
    image_bytes = await file.read()
    return await disease_service.diagnose(image_bytes)


@router.get("/weather", response_model=WeatherResponse)
async def weather(lat: float = Query(...), lon: float = Query(...)) -> WeatherResponse:
    return await weather_service.get_weather(lat=lat, lon=lon)


@router.get("/market-prices", response_model=list[MarketPrice])
async def market_prices(crop: str = Query(default="Tomato")) -> list[MarketPrice]:
    return await market_service.get_prices(crop)


@router.get("/nearby-farms", response_model=list[NearbyFarm])
async def nearby_farms(lat: float = Query(...), lng: float = Query(...)) -> list[NearbyFarm]:
    return await farm_service.nearby(lat=lat, lng=lng)


@router.post("/upload-video", response_model=VideoUploadResponse)
async def upload_video(payload: VideoUploadRequest, db: AsyncSession = Depends(get_db)) -> VideoUploadResponse:
    return await community_service.upload_video(db=db, payload=payload)
