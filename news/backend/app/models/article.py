from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ARRAY
from sqlalchemny.sql import func
from app.database import Base

class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(Text)
    source = Column(String, index=True)
    url = Column(String, unique=True)
    published_at = (Column(DateTime))
    topics = Column(ARRAY(String))
    bias_score = Column(Float)
    created_at = Column(DateTime, server_default=func.now())