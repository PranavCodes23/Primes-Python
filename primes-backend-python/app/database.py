from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib.parse

# Percent encode the password to handle special characters like %
password = urllib.parse.quote_plus("9@wUA%8PQnrpb-")
DATABASE_URL = f"mysql+pymysql://root:{password}@localhost:3306/rail_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
