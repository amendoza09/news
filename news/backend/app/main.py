from fastapi import FastAPI
from app.routes.articles import router as article_router

app = FastAPI(
    title="news",
    description = "shows news and scores articles for neutrality",
    version = "1.0.0"
)

app.include_router(article_router, prefix="/articles")