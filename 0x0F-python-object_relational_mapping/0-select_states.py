#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

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

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
