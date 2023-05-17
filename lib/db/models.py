# # 1.✅ Build out Model
# # Import from sqlalchemy: PrimaryKeyConstraint, Column, String, Integer
# # Import from sqlalchemy.ext.declarative, declarative_base
# from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
# from sqlalchemy.ext.declarative import declarative_base
# # 1.a ✅ Initialize declarative_base and save it to a variable called Base

# Base = declarative_base()
# # 1.b ✅ Create a class Pet that inherits from Base

# class Artist(Base):
#     __tablename__ = "Artist"
#     # Set the "__tablename__" to 'pets
#     # Add table args for a primary key constraint based off the id
#     __table_args__ = (PrimaryKeyConstraint('id'), )
#     # Create the following columns
#     # id -> type integer
#     # name -> type string
#     # species -> type string
#     # breed -> type string
#     # temperament -> type string

#     id = Column(Integer())
#     name = Column(String())
#     genre = Column(String())
    

#     # add a __repr__ method that returns a string containing the id, name, species, breed and temperament of our class

#     def __repr__(self):
#         return f"id: {self.id}, name: {self.name}, species: {self.species}, breed: {self.breed}, temperament: {self.temperament}"
    
# class Event(Base):
#     __tablename__ = "Events"
#     # Set the "__tablename__" to 'pets
#     # Add table args for a primary key constraint based off the id
#     __table_args__ = (PrimaryKeyConstraint('id'), )
    # Create the following columns
    # id -> type integer
    # name -> type string
    # species -> type string
    # breed -> type string
    # temperament -> type string

    # id = Column(Integer())
    # name = Column(String())
    # genre = Column(String())



# Note: Nothing further goes in this file.
# The following will generate a number of folders and files

# 2.✅ Migrations
# In the app directory run `alembic init migrations`
# Your directory structure should look like the following
# └── migrations
#     └── versions
#     ├── env.py
#     ├── README
#     ├── script.py.mako
# ├── alembic.ini
# ├── console.py
# └── models.py

# 2.b Configuration
    # In alembic.ini, find `sqlalchemy.url`` and set it to `sqlalchemy.url = sqlite:///pet_app.db`
    # In env.py, find `target_metadata` and add `from models import Base` above it. Next, set target_metadata to `target_metadata = Base.metadata`

# 2.c ✅ Generate a migration by running `alembic revision --autogenerate -m "Added Pet model"`
    # pet_app.db should have been added to your file structure

    # Take the time to review the migration and verify the database with SQLite Explorer or DB Browser

# 3✅ Head to debug.py to test out CRUD actions.