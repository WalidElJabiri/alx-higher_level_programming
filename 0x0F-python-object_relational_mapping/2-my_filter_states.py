#!/usr/bin/python3
"""
Script that lists all values in the states table of hbtn_0e_0_usa
where name matches the argument state name searched.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name search (str)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_user = sys.argv[1]
    mySQL_pass = sys.argv[2]
    db_name = sys.argv[3]

    search_name = sys.argv[4]

    db = MySQLdb.connect(user=mySQL_user, passwd=mySQL_pass, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
            .format(search_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)
