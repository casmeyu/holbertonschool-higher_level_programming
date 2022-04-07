#!/usr/bin/env python3
"""Module for printing all the states"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    eng_creation = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng_creation)
    Session = sessionmaker(bind=engine)
    session = Session()

    search = argv[4]
    objs = session.query(State).filter(State.name == search).all()
    if len(objs) > 0:
        for obj in objs:
            print(f'{obj.id}')
    else:
        print('Not found')

    session.close()
