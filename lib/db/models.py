from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///example.db')

Base = declarative_base()

#EXAMPLE 
class SuperHero(Base):
    __tablename__ = 'super_heroes'

    __table_args__ =(PrimaryKeyConstraint('id'))
    id = Column(Integer()) 
    name - Column(String())
    power = Column(String())
