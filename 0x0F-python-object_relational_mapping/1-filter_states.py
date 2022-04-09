#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':
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
        query = '''select * from states
                where name regexp "^N.*"
                order by states.id asc'''

        cur.execute(query)
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

        cur.close()
        db.close()
    except Exception as ex:
        print(ex)
