from sqlachemy import create_engine
from sqlachemy.orm import sessionmaker, decalrative_base
from dotenv import load_env
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocmmmit=False)
Base = declarative_base()

