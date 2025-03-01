import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="root")

if con!=None:
    print("Connected to the database")
else:
    print("Not connected to the database")


