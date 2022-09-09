#!/usr/bin/python3
""" This module contains script lists all states from htbn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MYSQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER by id ASC") # HERE i HAVE to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
