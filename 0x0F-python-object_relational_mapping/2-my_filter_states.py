#!/usr/bin/python3
"""Module for selecting a state with a given name"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    if len(argv) < 3:
        exit()

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )
    cur = db.cursor()

    cur.execute(f'select * from states\
            where name like binary "{argv[4]}"\
            order by states.id asc')

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
