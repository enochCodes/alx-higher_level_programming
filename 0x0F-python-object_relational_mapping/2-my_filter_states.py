#!/usr/bin/python3
"""
    database connect feach the result wtih N
"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            db=db_name
            )

    cursor = db.cursor()

    cursor.execute("SELECT *FROM states WHERE name LIKE 'N%'")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
