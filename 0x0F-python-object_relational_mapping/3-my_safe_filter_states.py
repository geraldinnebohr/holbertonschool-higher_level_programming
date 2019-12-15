#!/usr/bin/python3
"""
Script that is safe from MySQL injections
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
    cur.execute("SELECT * FROM states WHERE name = %(mysql_name)s ORDER BY id",
                {'mysql_name': mysql_name})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
