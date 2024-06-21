#!/usr/bin/python3
"""
This module contains a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], port=3306)
    cur = db.cursor()

    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"

    condition = (argv[4],)

    cur.execute(query, condition)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
