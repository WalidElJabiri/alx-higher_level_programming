#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_user = sys.argv[1]
    mySQL_pass = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(user=mySQL_user, passwd=mySQL_pass, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT c.id, c.name, s.name \
            FROM cities c INNER JOIN states s \
            ON c.state_id = s.id \
            ORDER BY c.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
