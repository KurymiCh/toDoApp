import os
import datetime
import sqlalchemy as sa
from dotenv import load_dotenv
from sqlalchemy import Boolean, Column, DateTime, Integer, String, UUID
from sqlalchemy.orm import sessionmaker
 
load_dotenv()

DB_URL = os.getenv("DB_URL")

engine=sa.create_engine(DB_URL)
session= sessionmaker(bind=engine)
Base=sa.orm.declarative_base()

class Item(Base):
    _tablename_="item"
    id=Column(UUID(as_uuid=True),primary_key=True, index=True)
    title=Column(String)
    desc=Column(String)
    todo=Column(DateTime)
    done=Column(Boolean, default= False)
    created_at=Column(DateTime, default=datetime.datetime.now)
    updated_at=Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    deleted_at=Column(DateTime, nullable=True)
    