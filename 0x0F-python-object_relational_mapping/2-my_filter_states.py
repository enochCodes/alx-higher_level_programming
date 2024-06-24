#!/usr/bin/python3
"""
    database connect feach the result wtih N serch
"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            db=db_name
            )

    cursor = db.cursor()
    sql_query = (
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        )
    cursor.execute(sql_query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
