import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_host = os.environ.get('DB_HOST', 'sqlite:///:memory:')

engine = create_engine(db_host)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
