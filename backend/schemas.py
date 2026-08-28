from pydantic import BaseModel


class BlogCreate(BaseModel):
    topic: str
    tone: str


class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    image_url: str
    tone: str

    class Config:
        from_attributes = True