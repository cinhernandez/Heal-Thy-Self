
from sqlalchemy import Column, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Genre_Options(Base):
    __tablename__ = "genre_options"
   
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"

class Artist(Base):
    __tablename__ = "artists"
   
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String()) 
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, genre: {self.genre}"
    

class Accommadation(Base):
    __tablename__ = "accommadations"
   
    id = Column(Integer(), primary_key=True)
    age_limit= Column(String())
    camping_availability = Column(String())
    festival_capacity = Column(Integer())

    def __repr__(self):
        return f"id: {self.id}, age_limit: {self.age_limit}, camping_availability: {self.camping_availability}, festival_capacity: {self.festival_capacity}"
    

class Festival(Base):
    __tablename__ = "festivals"
   
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    date = Column(String()) 
    location = Column(String())
    price = Column(Integer())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, location: {self.location}, date: {self.date}, location: {self.location}, price: {self.price}"
    

class AddToCart(Base):
    __tablename__ = "add_to_carts"

    id = Column(Integer(), primary_key=True)
    festival_id = Column(Integer())


if __name__ == '__main__':
    engine = create_engine('sqlite:///edm.db')
    Base.metadata.create_all(engine)

#-------------------UPDATES ITEMS IN THE TABLE-------------------

    # Session = sessionmaker(bind=engine)
    # session = Session()
    # record = session.query(Artist).filter_by(id=25).first()
    # record.genre = "Dubstep, Future Bass, Melodic Dubs"
    # session.commit()

    # session.close()

#-------------------ADDS ITEMS TO THE TABLE-------------------

    Session = sessionmaker(bind=engine)
    session = Session()

    Seven_lion = Artist(name="Seven Lions", genre="Dubstep, Trance ")
    session.add(Seven_lion)
    session.commit()

    session.close()


    #KIND OF MADE UP WITH BEING ALL AGES AND 16+

    #Breakaway (16+)
    #Sonic Therapy (All ages)
    #Dancefest (All ages)
    #FAM Fest (All ages)
    #Chasing Sunsets (16+)
    #Awakening Music Festival (16+)