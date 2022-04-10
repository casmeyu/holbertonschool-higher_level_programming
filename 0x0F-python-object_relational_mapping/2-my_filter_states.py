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

    query = '\
select * from states \
where name like binary "{}" \
order by states.id asc'.format(argv[4])

    cur.execute(query)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
