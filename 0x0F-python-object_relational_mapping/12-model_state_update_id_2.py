#!/usr/bin/python3
"""Updates the name of the state with id == 2"""
from sqlalchemy import (create_engine, update)
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == '__main__':

    if (len(argv) == 4):
        eng_creat = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
        engine = create_engine(eng_creat)
        s = Session(engine)

        s.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
        s.commit()

        s.close()
