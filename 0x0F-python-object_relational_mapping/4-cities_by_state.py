#!/usr/bin/env python3
import MySQLdb
from sys import argv

try:
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()
except Exception as ex:
    print(ex)

try:
    query = f'''select c.id, c.name, s.name from cities as c
            left join states as s
            on s.id = c.state_id'''

    cur.execute(query)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
except Exception as ex:
    print(ex)
