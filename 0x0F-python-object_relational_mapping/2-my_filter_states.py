#!/usr/bin/python3
"""
Script that takes an argument and displays all values of a table where name
matches the argument.
"""

import MySQLdb
import sys
if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    mysql_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_passwd, db=mysql_db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id".
                format(mysql_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] is mysql_name:
            print(row)
    cur.close()
    db.close()
