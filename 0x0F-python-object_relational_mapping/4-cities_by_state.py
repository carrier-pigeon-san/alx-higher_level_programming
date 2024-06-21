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

    query = "SELECT c.id, c.name, s.name\
        FROM cities c INNER JOIN states s\
            ON c.state_id = s.id ORDER BY id ASC"

    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
