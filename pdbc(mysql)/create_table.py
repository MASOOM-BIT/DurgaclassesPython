import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="sakila")
    query="create table employee(id int,name varchar(255),age int)"
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("Table created successfully")
except mysql.connector.Error as e:
    print("Error creating table",e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()





