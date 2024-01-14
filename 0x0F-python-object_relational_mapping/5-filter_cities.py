#!/usr/bin/python3
"""lists all cities of the state passed as input argument in the
   database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (state,))
    rws = cur.fetchall()
    my_list = list(rw[0] for rw in rws)
    print(*my_list, sep=", ")
    cur.close()
    db.close()
