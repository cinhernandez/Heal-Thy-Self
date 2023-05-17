
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Event(Base):
    __tablename__ = "events"

    __table_args__ = (PrimaryKeyConstraint('id'), )
   

    id = Column(Integer())
    name = Column(String())
    genre = Column(String())
    