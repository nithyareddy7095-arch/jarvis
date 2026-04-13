from pydantic import BaseModel


class PlantDiagnosisResponse(BaseModel):
    disease_type: str
    confidence: float
    recommendation: str
