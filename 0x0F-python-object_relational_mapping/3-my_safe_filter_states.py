#!/usr/bin/python3
"""Display the rows from table states in database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE
                %s ORDER BY id""", (sys.argv[4],))
    rws = cur.fetchall()
    for rw in rws:
        print(rw)
    cur.close()
    db.close()
