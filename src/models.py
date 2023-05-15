import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable= False, unique = True)
    password = Column(String(50), nullable = False)
    email = Column(String(50), nullable=False)
    

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column (Integer, nullable = True)
    homeworld_id = Column(Integer, ForeignKey('planet.id'), nullable = False)
    starship = Column(Integer, ForeignKey('starship.id'), nullable = False)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(String(50), nullable=False)
    rotation = Column(Integer, nullable=False)

class Starships(Base):
    __tablename__ = 'starship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    starship_class =Column(String(50), nullable=False)
    length = Column(Integer, nullable=False)
    pilots = Column(String, ForeignKey('character.id'), nullable=True)




class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=False)



    


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
