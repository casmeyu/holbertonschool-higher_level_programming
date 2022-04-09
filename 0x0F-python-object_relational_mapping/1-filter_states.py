#!/usr/bin/python3
"""Module for getting all states that start with a given letter"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )
    cur = db.cursor()

    query = '''select * from states
            where name regexp "^N.*"
            order by states.id asc'''

    cur.execute(query)
    query_rows = cur.fetchall()

    if not query_rows:
        print()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
