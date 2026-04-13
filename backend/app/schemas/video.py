from pydantic import BaseModel, HttpUrl


class VideoUploadRequest(BaseModel):
    farmer_id: int
    title: str
    description: str = ""
    video_url: HttpUrl


class VideoUploadResponse(BaseModel):
    id: int
    title: str
    video_url: str
