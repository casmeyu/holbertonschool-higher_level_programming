#!/usr/bin/python3
"""Module fot fetch vity by state"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == '__main__':
    if len(argv) == 4:
        eng_creat = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
        engine = create_engine(eng_creat)
        Session = sessionmaker(bind=engine)
        s = Session()

        data = s.query(State, City).filter(State.id == City.state_id).\
            order_by(City.id).all()
        for state, city in data:
            print(f'{state.name}: ({city.id}) {city.name}')

        s.close()
