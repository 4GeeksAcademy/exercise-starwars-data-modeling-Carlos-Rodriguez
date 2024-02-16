import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable = False)
    lastname = Column(String(50), nullable = False)
    email = Column(String(50), unique = True, nullable = False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable = False)
    terrain = Column(String(250), nullable = False)
    population = Column(String(250), nullable = False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    gender = Column(String(250), nullable = False)
    birth_date = Column(String(250), nullable = False)
    eye_color = Column(String(250), nullable = False)
    hair_color = Column(String(250), nullable = False)
    height = Column(Integer, nullable = False)
    mass = Column(Integer, nullable = False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable = False)
    

class Favorites (Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable = False)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable = False)
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
