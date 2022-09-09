#!/usr/bin/python3
"""this module contains a script that lists all states starting wiith N"""

import sys
import MYSQLdb

if __name == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                           passwd="root", db="my_db", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
