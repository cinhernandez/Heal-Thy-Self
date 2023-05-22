from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

festival_genre_option = Table(
    'festival_genre_options',
    Base.metadata,
    Column('festival_id', Integer, ForeignKey('festivals.id'), primary_key=True),
    Column('genre_option_id', Integer, ForeignKey('genre_options.id'), primary_key=True)
)

class Festival(Base):
    __tablename__ = "festivals"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    location = Column(String)
    price = Column(Integer)

    add_to_cart_id = Column(Integer, ForeignKey('add_to_carts.id'))
    genres = relationship('Genre_Option', secondary=festival_genre_option, back_populates='festivals')

    def __repr__(self):
        return f'Festival(id={self.id}, ' + \
            f'name={self.name},' + \
            f'date={self.date}, ' + \
            f'location={self.location},' + \
            f'price={self.price})'

class Genre_Option(Base):
    __tablename__ = "genre_options"

    id = Column(Integer, primary_key=True)
    genre = Column(String)
    add_to_carts = relationship('Add_To_Cart', backref='festival')
    festivals = relationship('Festival', secondary=festival_genre_option, back_populates='genres')

    def __repr__(self):
        return f'Genre_Option(id={self.id}, ' + \
            f'genre={self.genre})'

class Add_To_Cart(Base):
    __tablename__ = "add_to_carts"

    id = Column(Integer, primary_key=True)

    festivals = relationship('Festival')
    genre_id = Column(Integer, ForeignKey('genre_options.id'))

    def __repr__(self):
        return f'Add_To_Cart(id={self.id})'


