from io import BytesIO
import numpy as np
from PIL import Image

from app.schemas.plant import PlantDiagnosisResponse


class DiseaseDetectionService:
    """CNN inference placeholder (replace with Torch/TFLite model in production)."""

    LABELS = ["Healthy", "Late Blight", "Powdery Mildew", "Leaf Spot"]

    async def diagnose(self, image_bytes: bytes) -> PlantDiagnosisResponse:
        image = Image.open(BytesIO(image_bytes)).convert("RGB").resize((128, 128))
        arr = np.asarray(image).astype("float32") / 255.0

        green_score = float(arr[:, :, 1].mean())
        disease_idx = 0 if green_score > 0.45 else 1
        confidence = round(0.86 if disease_idx else 0.91, 2)

        disease = self.LABELS[disease_idx]
        recommendation = (
            "Crop appears healthy. Continue preventive spray schedule and monitoring."
            if disease == "Healthy"
            else "Possible fungal disease detected. Remove infected leaves and apply copper-based fungicide."
        )

        return PlantDiagnosisResponse(disease_type=disease, confidence=confidence, recommendation=recommendation)
