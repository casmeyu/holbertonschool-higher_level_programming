#!/usr/bin/python3
"""Module for listing all the cities"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


if __name__ == '__main__':
    eng_creat = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng_creat)

    s = Session(engine)

    for city in s.query(City).all():
        state = s.query(State).where(State.id == city.state_id).first()
        print(f'{city.id}: {city.name} -> {state.name}')
