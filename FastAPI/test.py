import uvicorn
from fastapi import FastAPI
from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLAlCHEMY_BASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLAlCHEMY_BASE_URL)
sessin_local = sessionmaker(autocommit = False,autoflush=False,bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer,primary_key=True,Index=True)
    name = Column(String,index=True)
    description = Column(String,index=True)

