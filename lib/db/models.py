
from sqlalchemy import (PrimaryKeyConstraint, Table, Column, String, Integer, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()



class Artist(Base):
    __tablename__ = "artists"

    __table_args__ = (PrimaryKeyConstraint('id'), )
   
    id = Column(Integer())
    name = Column(String())
    genre = Column(String()) 
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, genre: {self.genre}"
 

class Accommadation(Base):
    __tablename__ = "accommadations"

    __table_args__ = (PrimaryKeyConstraint('id'), )
   
    id = Column(Integer())
    age_limit= Column(String())
    camping_availability = Column(String())
    festival_capacity = Column(Integer())

    def __repr__(self):
        return f"id: {self.id}, age_limit: {self.age_limit}, camping_availability: {self.camping_availability}, festival_capacity: {self.festival_capacity}"
    

class Festival(Base):
    __tablename__ = "festivals"

    __table_args__ = (PrimaryKeyConstraint('id'), )
   
    id = Column(Integer())
    name = Column(String())
    date = Column(Date()) 
    location = Column(String())
    price = Column(Integer())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, location: {self.location}, date: {self.date}, location: {self.location}, price: {self.price}"