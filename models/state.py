#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states' 
  #  name = ""
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///your_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
