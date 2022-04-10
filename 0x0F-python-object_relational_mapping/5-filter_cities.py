#!/usr/bin/python3
"""Filter all the cities from a state in a formatted String"""
import MySQLdb
from sys import argv

import MySQLdb
from sys import argv

# j code

if __name__ == "__main__":
    if (len(argv) > 3):
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cmd = "SELECT cities.name FROM cities INNER JOIN states ON \
cities.state_id = states.id WHERE states.name LIKE BINARY %s"
        cur.execute(cmd, (argv[4], ))
        rows = cur.fetchall()
        if (len(rows) != 0):
            res = ''
            for idx in range(len(rows)):
                if idx != 0:
                    res += f', {rows[idx][0]}'
                else:
                    res += rows[idx][0]

            print(res)
        else:
            print()

        cur.close()
        db.close()

"""
my code

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()

    if len(argv) == 5:
        query = f'''select c.name from states as s
                inner join cities as c
                on c.state_id = s.id
                where s.name like binary %s'''

        cur.execute(query, (argv[4],))
        query_rows = cur.fetchall()

        if len(query_rows) == 0:
            print()
        else:
            res = ''
            for idx in range(len(query_rows) - 1):
                row = query_rows[idx][0]
                if idx != 0:
                    res += (', ' + row)
                else:
                    res += (row)

            print(res)

        cur.close()
        db.close()
"""
