from backend.database import Base
from sqlalchemy import Column, Integer, String, Text


class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    image_url = Column(String)
    tone = Column(String)