#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    query = "SELECT cities.name FROM cities"
    join_condition = "LEFT JOIN states ON cities.state_id = states.id"
    where_condition = "WHERE states.name = %s"
    exe = "{} {} {}".format(query, join_condition, where_condition)
    cur.execute(exe, (sys.argv[4],))
    rows = cur.fetchall()

    index = 0
    for row in rows:
        if index < len(rows) - 1:
            print(row[0], end=", ")
            index += 1
        else:
            print(row[0], end="")
    print()
    cur.close()
    db.close()
