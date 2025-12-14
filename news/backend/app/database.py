from sqlachemy import create_engine
from sqlachemy.orm import sessionmaker, decalrative_base
import os

DB_URL = os.getenv("https://lvgiwkptombtgodbnbfe.supabase.co")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = decalrative_base()

