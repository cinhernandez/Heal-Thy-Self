
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3')
Base = declarative_base()


class Genre(Base):
    __tablename__ = "genres"

    __table_args__ = (PrimaryKeyConstraint('id'), )
   

    id = Column(Integer())
    name = Column(String())
    genre = Column(String())
    