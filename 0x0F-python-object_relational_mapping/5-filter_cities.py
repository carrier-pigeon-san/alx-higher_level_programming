#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa:
* The script takes 4 arguments: mysql username, mysql password, database name,
  and state name
* The script uses the module MySQLdb (import MySQLdb).
* The script connects to a MySQL server running on localhost at port 3306.
* Results sre sorted in ascending order by cities.id
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                         database=argv[3], port=3306)
    cur = db.cursor()

    query = "SELECT c.name\
        FROM cities c INNER JOIN states s\
            ON c.state_id = s.id WHERE s.name = %s\
                ORDER BY c.id ASC"

    condition = (argv[4],)

    cur.execute(query, condition)
    rows = cur.fetchall()
    for row in range(len(rows)):
        city = str(rows[row][0])
        if row < len(rows) - 1:
            print(city, end=", ")
        else:
            print(city)
    cur.close()
    db.close()
