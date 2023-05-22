
from sqlalchemy import Column, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

class Genre_Options(Base):
    __tablename__ = "genre_options"
   
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"
    
      #establishes relationship between genre_options and artist
    artists = relationship("Artist", back_populates="genre_option")

class Artist(Base):
    __tablename__ = "artists"
   
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String()) 
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, genre: {self.genre}"
    
        #establishes relationship between artist and genre_options
    genre_option = relationship("Genre_Options", back_populates="artists")
    

class Accommadation(Base):
    __tablename__ = "accommadations"
   
    id = Column(Integer(), primary_key=True)
    age_limit= Column(String())
    camping_availability = Column(String())
    festival_capacity = Column(Integer())

    def __repr__(self):
        return f"id: {self.id}, age_limit: {self.age_limit}, camping_availability: {self.camping_availability}, festival_capacity: {self.festival_capacity}"
    
        #establishes relationship between accommodation and festival
    festival = relationship("Festival", back_populates="accommodations")

    

class Festival(Base):
    __tablename__ = "festivals"
   
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    date = Column(String()) 
    location = Column(String())
    price = Column(Integer())

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, location: {self.location}, date: {self.date}, location: {self.location}, price: {self.price}"
    
    #establishes relationship between festival and artist
    accommodations = relationship("Accommodation", back_populates="festival")
    #establishes relationship between festival and add_to_cart
    add_to_carts = relationship("AddToCart", back_populates="festival")
    

class AddToCart(Base):
    __tablename__ = "add_to_carts"

    id = Column(Integer(), primary_key=True)
    festival_id = Column(Integer())

    #establishes relationship between festival and add_to_cart
    festival = relationship("Festival", back_populates="add_to_carts")

if __name__ == '__main__':
    pass
#-------------------CREATES THE TABLE-------------------
#--------UNCOMMENT THIS TO CREATE THE TABLE-------------------

    # engine = create_engine('sqlite:///edm.db')
    # Base.metadata.create_all(engine)

#-------------------UPDATES ITEMS IN THE TABLE-------------------

    # Session = sessionmaker(bind=engine)
    # session = Session()
    # record = session.query(Artist).filter_by(id=34).first()
    # record.genre = "Hardstyle"
    # session.commit()

    # session.close()

#-------------------ADDS ITEMS TO THE TABLE-------------------

    # Session = sessionmaker(bind=engine)
    # session = Session()

    # Vibra_sphere = Artist(name="Vibra Sphere", genre="Psytrance")
    # session.add(Vibra_sphere)
    # session.commit()
    # session.close()


    #KIND OF MADE UP WITH BEING ALL AGES AND 16+

    #Breakaway (16+)
    #Sonic Therapy (All ages)
    #Dancefest (All ages)
    #FAM Fest (All ages)
    #Chasing Sunsets (16+)
    #Awakening Music Festival (16+)


#-------------------DELETES ITEMS FROM THE TABLE-------------------

    # Session = sessionmaker(bind=engine)
    # session = Session()

    # record = session.query(Genre_Options).filter_by(id=8).first()
    # session.delete(record)

    # session.commit()
    # session.close()

