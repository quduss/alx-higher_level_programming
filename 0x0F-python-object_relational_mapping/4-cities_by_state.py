#!/usr/bin/python3
"""Display the cities with their corresponding states in database
   hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON cities.state_id=states.id
                ORDER BY cities.id""")
    rws = cur.fetchall()
    for rw in rws:
        print(rw)
    cur.close()
    db.close()
