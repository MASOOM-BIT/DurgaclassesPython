import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="sakila")
    query="drop table employee"
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("Table dropped successfully")
except mysql.connector.Error as e:
    print("Error dropping table",e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()

