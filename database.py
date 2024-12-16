from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models import  Base

sqlalchemy_database_URL = "sqlite:///./crypto_notifications.db/"
engine = create_engine(sqlalchemy_database_URL )
Session_local = sessionmaker(autoflush=False, bind=engine)

## intilasing the dataabse :

Base.metadata.create(bind=engine)


