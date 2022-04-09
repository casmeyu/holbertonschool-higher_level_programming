#!/usr/bin/python3
"""Module for printing all the states"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    eng_creation = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng_creation)
    session = Session(engine)

    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()
