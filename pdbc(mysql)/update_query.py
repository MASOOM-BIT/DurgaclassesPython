import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="sakila")
    cursor=con.cursor()
    increment=int(input("Enter the increment: "))
    query="update actor set actor_id=actor_id+%s"
    cursor.execute(query,increment)
    con.commit()
    print("Data updated successfully")
except mysql.connector.Error as e:
    print("Error updating data",e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()

