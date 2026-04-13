from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from app.models.entities import CommunityVideo
from app.schemas.video import VideoUploadRequest, VideoUploadResponse


class CommunityService:
    async def upload_video(self, db: AsyncSession, payload: VideoUploadRequest) -> VideoUploadResponse:
        stmt = (
            insert(CommunityVideo)
            .values(
                farmer_id=payload.farmer_id,
                title=payload.title,
                description=payload.description,
                video_url=str(payload.video_url),
            )
            .returning(CommunityVideo.id, CommunityVideo.title, CommunityVideo.video_url)
        )
        row = (await db.execute(stmt)).one()
        await db.commit()
        return VideoUploadResponse(id=row.id, title=row.title, video_url=row.video_url)
