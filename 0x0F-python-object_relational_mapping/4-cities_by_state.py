#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities"
    join_condition = "LEFT JOIN states ON cities.state_id = states.id"
    cur.execute("{} {}".format(query, join_condition))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
