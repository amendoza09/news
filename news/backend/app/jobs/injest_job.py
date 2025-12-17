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
        articles.subjectivity_score = scores["subjectivity"]
        articles.bias_score = compute_bias(
            scores["subjectivity"], scores["polarity"]
        )
    db.commit()
    db.close()
    
scheduler = BackgrundScheduler()
schedular.add_job(run, "interval", minutes = 30)
schedular.start()