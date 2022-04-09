#!/usr/bin/env python3
"""Deletes all entries with and a in the state name"""
from sqlalchemy import (create_engine, delete)
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == '__main__':

    if (len(argv) == 4):
        eng_creat = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
        engine = create_engine(eng_creat)

        stmt = (
            delete(State).
            where(State.name.like('%a%'))
        )
        engine.execute(stmt)
