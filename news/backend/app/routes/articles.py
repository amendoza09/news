from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.articles import Article

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/")
def list_articles(
    topic: str | None = None,
    max_bias: float | None = Query(None, le=1.0),
    db: Session = Depends(get_db)
):
    query = db.query(Article)
    
    if topic:
        query = query.filter(Article.topics.any(topic))
    if max_bias is not None:
        query = query.filter(Article.bias_score <= max_bias)
    
    return query.order_by(Article.published_at.desc()).limit(50).all()