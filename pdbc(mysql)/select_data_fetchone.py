import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="sakila")
    query="select * from actor"
    cursor=con.cursor()
    cursor.execute(query)
    row=cursor.fetchone()
    while row is not None:
        print(row)
        row=cursor.fetchone()
except mysql.connector.Error as e:
    print("Error selecting data",e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()