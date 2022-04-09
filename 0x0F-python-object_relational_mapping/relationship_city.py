#!/usr/bin/python3
"""Module for city model ORM using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """Class for cities model"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
