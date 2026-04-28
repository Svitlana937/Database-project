# https://www.w3schools.com/python/python_mysql_getstarted.asp

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="conference_db"
)
cursor = db.cursor()
