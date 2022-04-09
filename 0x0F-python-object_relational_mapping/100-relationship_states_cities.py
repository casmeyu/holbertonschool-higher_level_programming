#!/usr/bin/python3
"""Module for the relationship between state and city"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    eng_creat = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng_creat, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    s = Session()

    new_state = State(name='California')
    new_city = City(name='San Fransisco')

    new_state.cities.append(new_city)
    s.add(new_state)
    s.add(new_city)
    s.commit()
    s.close()
