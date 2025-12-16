from appschedular.schedulars.background import BackgorundScheduler
from app.database import SessionLocal
from app.services.ingestion import ingest
from app.services.bias import analyze, compute_bias
from app.models.article import Article

def run():
    db = SessionLocal()
    ingest(db)
    
    articles = db.query(Article).filter(Article.bias_score == None).all()
    
    for article in articles:
        scores = analyze(article.content)
        