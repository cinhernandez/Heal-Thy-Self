from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import (Base, Artist, Accommadation, Festival, AddToCart, Genre_Options)

engine = create_engine('sqlite:///edm.db')
Session = sessionmaker(bind=engine)
session = Session()

def register():
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")

    