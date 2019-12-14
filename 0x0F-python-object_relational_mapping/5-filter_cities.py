#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_passwd, db=mysql_db)
    cur = db.cursor()
    cur.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id ASC;
    """)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
