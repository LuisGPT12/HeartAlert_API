from fastapi import APIRouter, HTTPException
from typing import List
from Database.database import engine, video
from schemas.video import Video

video_route = APIRouter(
    prefix="/api/heatalert/video",
    tags=["video"]
)

@video_route.post("/", response_model=Video)
def create_video(video_data: Video):
    with engine.connect() as conn:
        query = video.insert().values(**video_data.dict())
        result = conn.execute(query)
        conn.commit()
        video_data.id_video = result.lastrowid
        return video_data

@video_route.get("/", response_model=List[Video])
def get_videos():
    with engine.connect() as conn:
        result = conn.execute(video.select()).fetchall()
        return [Video(**dict(row._mapping)) for row in result]

@video_route.get("/{video_id}", response_model=Video)
def get_video(video_id: int):
    with engine.connect() as conn:
        query = video.select().where(video.c.id_video == video_id)
        result = conn.execute(query).fetchone()
        if result:
            return Video(**dict(result._mapping))
        else:
            raise HTTPException(status_code=404, detail="Video not found")

@video_route.put("/{video_id}", response_model=Video)
def update_video(video_id: int, video_data: Video):
    with engine.connect() as conn:
        query = video.update().where(video.c.id_video == video_id).values(**video_data.dict())
        result = conn.execute(query)
        conn.commit()
        if result.rowcount > 0:
            video_data.id_video = video_id
            return video_data
        else:
            raise HTTPException(status_code=404, detail="Video not found")

@video_route.delete("/{video_id}", response_model=dict)
def delete_video(video_id: int):
    with engine.connect() as conn:
        query = video.delete().where(video.c.id_video == video_id)
        result = conn.execute(query)
        conn.commit()
        if result.rowcount > 0:
            return {"message": "Video deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Video not found")