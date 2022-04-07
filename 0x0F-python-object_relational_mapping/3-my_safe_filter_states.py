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
    query = f'''select * from states
            where name=%s'''

    cur.execute(query, (argv[4],))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
except Exception as ex:
    print(ex)
