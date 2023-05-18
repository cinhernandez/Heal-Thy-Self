from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import (Base, Artist, Accommadation, Festival)

if __name__ == '__main__':
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    Tchami = Artist(id=1, name="Tchami", genre="House")

