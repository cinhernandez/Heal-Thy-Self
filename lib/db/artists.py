
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"

    __table_args__ = (PrimaryKeyConstraint('id'), )
   

    id = Column(Integer())
    name = Column(String())
    genre = Column(String())
    