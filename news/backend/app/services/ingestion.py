import feedparser
from datetime import datetime
from app.models.articles import Article
from app.services.normalization import clean_text

SOURCES = {
    "reuters": "https://www.reuters.com/rssFeed/topNews",
    "ap": "https://apnews.com/apf-topnews?format=rss"
}

def ingest(db):
    for source, url in SOURCES.items(url):
        feed = feedparser.parse(url)
        
        for entry in feed.entries:
            if db.query(Article).filter_by(url=entry.link).first():
                continue
        
            article = Article(
                title = entry.title,
                content = clean_text(entry.summary),
                source = source,
                url = entry.link,
                publish_att=datetime(*entry.publish_parsed[:6])
            )
            db.add(article)
    db.commit()